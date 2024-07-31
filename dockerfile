FROM python:3.11-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /project_python_graphql_nlp

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# Use JSON arguments for CMD to avoid potential issues
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]