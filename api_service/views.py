from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Cars
from .serializers import CarsSerializer
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain import hub
from pydantic import BaseModel

load_dotenv()

# Set up the OpenAI client and database connection
openai_api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")

# Connect to the SQLite database
db = SQLDatabase.from_uri("sqlite:///db.sqlite3")  # Adjust URI as needed
# db = SQLDatabase.from_uri("sqlite:///Chinook_Sqlite.sqlite")

# Load the SQL query prompt
query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

# Create your views here.
class QueryOutput(BaseModel):
    query: str

# Define the NLP Query View
class NLPQueryView(APIView):
    @swagger_auto_schema(
        operation_description="Accepts a natural language query and returns the result of the SQL query execution.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description='Natural language query'),
            },
            required=['question'],
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'answer': openapi.Schema(type=openapi.TYPE_STRING, description='Answer to the query'),
                },
            ),
            400: "Bad Request",
        },
    )
    def post(self, request):
        question = request.data.get('question', '').strip()
        if not question:
            return Response({"error": "Question is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Generate the SQL query
            prompt = query_prompt_template.invoke(
                {
                    "dialect": db.dialect,
                    "top_k": 10,
                    "table_info": db.get_table_info(),
                    "input": question,
                }
            )
            structured_llm = llm.with_structured_output(QueryOutput)
            result = structured_llm.invoke(prompt)
            sql_query = result.query

            # Execute the SQL query
            execute_query_tool = QuerySQLDataBaseTool(db=db)
            query_result = execute_query_tool.invoke(sql_query)

            # Generating the final response with the LLM
            response_prompt = (
                "Given the following user question and SQL result, provide a natural language response:\n\n"
                f"Question: {question}\n"
                f"SQL Result: {query_result}"
            )
            response = llm.invoke(response_prompt)

            return Response({"answer": response.content}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def nlp_ui_view(request):
    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if "clear_chat" in request.POST:
            # Clear chat history
            request.session["chat_history"] = []
            return render(request, "nlpui.html", {"chat_history": []})

        if not question:
            return render(request, "nlpui.html", {"error": "Please enter a valid question.", "chat_history": request.session.get("chat_history", [])})

        try:
            # Generate the SQL query
            prompt = query_prompt_template.invoke(
                {
                    "dialect": db.dialect,
                    "top_k": 10,
                    "table_info": db.get_table_info(),
                    "input": question,
                }
            )

            # Configure the LLM to use the structured model
            structured_llm = llm.with_structured_output(QueryOutput)
            result = structured_llm.invoke(prompt)
            sql_query = result.query

            # Execute the SQL query
            execute_query_tool = QuerySQLDataBaseTool(db=db)
            query_result = execute_query_tool.invoke(sql_query)

            # Generating the final response with the LLM
            response_prompt = (
                "Given the following user question and SQL result, provide a natural language response:\n\n"
                f"Question: {question}\n"
                f"SQL Result: {query_result}"
            )
            response = llm.invoke(response_prompt)

            # Save chat history in session
            chat_history = request.session.get("chat_history", [])
            chat_history.append({"user": question, "agent": response.content})
            request.session["chat_history"] = chat_history

            # Render with updated history
            return render(request, "nlpui.html", {"chat_history": chat_history})

        except Exception as e:
            # Handling errors and updating history
            chat_history = request.session.get("chat_history", [])
            chat_history.append({"user": question, "agent": f"Error: {str(e)}"})
            request.session["chat_history"] = chat_history
            return render(request, "nlpui.html", {"chat_history": chat_history, "error": str(e)})

    # For GET requests, show history if it exists
    return render(request, "nlpui.html", {"chat_history": request.session.get("chat_history", [])})


#RESTful views
class CarsList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer