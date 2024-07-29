from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Path to the CSV file
CSV_FILE_PATH = 'Data example - Python Coding Challenge - GraphQL.csv'

# Create your views here.
@csrf_exempt
def nlp_endpoint(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)

        # Normalize the query to lowercase
        query = query.lower()

        # Check if the query specifies a column and value
        if ':' in query:
            column_name, value = map(str.strip, query.split(':', 1))

            # Load the data
            data = pd.read_csv(CSV_FILE_PATH)

            # Check if the specified column exists in the dataset
            if column_name not in data.columns:
                return JsonResponse({'error': f'Column "{column_name}" not found in dataset.'}, status=400)

            # Convert both dataset and value to lowercase for case-insensitive matching
            data[column_name] = data[column_name].astype(str).str.lower()
            value = value.lower()

            # Filter rows based on the column value
            matching_rows = data[data[column_name].str.contains(value, na=False)]

        else:
            # General search across all columns
            doc = nlp(query)
            keywords = [ent.text.lower() for ent in doc.ents]

            # If no entities are recognized, use the entire query as a keyword
            if not keywords:
                keywords = query.lower().split()

            # Load the data
            data = pd.read_csv(CSV_FILE_PATH)

            # Function to check if any keyword is in the row
            def row_contains_keywords(row):
                row_data = ' '.join(row.astype(str).str.lower().values)
                return any(keyword in row_data for keyword in keywords)

            # Apply the function to filter rows
            results = data.apply(row_contains_keywords, axis=1)
            matching_rows = data[results]

        # Convert results to a list of dictionaries
        response_data = matching_rows.to_dict(orient='records')

        # Add total results count
        response_data = {
            'total_results': len(response_data),
            'results': response_data
        }

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)