GraphQL NLP API
This project is a Django application called api_service within the graphql_nlp_api project. It features GraphQL and NLP functionalities to handle and process data from a CSV file.

Project Setup
Prerequisites
Python 3.11.9
Django 4.2
Docker (optional, for containerization)

Clone the Repository
git clone https://github.com/nicoCalde/project_python_graphql_nlp.git
cd project_python_graphql_nlp

Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies
pip install -r requirements.txt

Database Setup
Note: The settings are configured for development (DEBUG=True). For production, use a more secure configuration and a robust database like PostgreSQL or MySQL.

Superuser already created
Username: admin
Password: 123

Running the Project

Local Development
python manage.py runserver

Docker Setup
Build Docker Image
docker build -t image_name .

Run Docker Container
docker run -p 8888:8000 image_name

Clean Up Docker
To delete the container and the image, use Docker Desktop:
Delete the Container
Delete the Image

Run the following commands to clear the Cache:
docker system prune

Additional Information
Ensure that the necessary environment variables are added before running the application.