# Data Engineering Job Pipeline

This Python project is designed to help you find and filter data engineering job postings from a job board. It leverages the RapidAPI service to search for job postings on "https://jsearch.p.rapidapi.com/search." The project includes the extraction of job data using the provided query strings, data cleaning, and loading the cleaned data into a PostgreSQL database. The following dependencies are required to run this project:

- [Requests](https://docs.python-requests.org/en/master/): A library for making HTTP requests in Python.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library.
- [SQLAlchemy](https://www.sqlalchemy.org/): A SQL toolkit and Object-Relational Mapping (ORM) library.
- [Psycopg2](https://pypi.org/project/psycopg2/): A PostgreSQL adapter for Python.

You can install these dependencies using `pip`:

```bash
pip install requests
pip install pandas
pip install SQLAlchemy
pip install psycopg2
```

## Project Overview

The goal of this project is to automate the process of searching for data engineering job postings and storing them in a PostgreSQL database for further analysis or tracking. Here's how the project works:

1. **Job Search and Data Extraction:** The project sends HTTP requests to the "https://jsearch.p.rapidapi.com/search" API, providing query strings to search for data engineering job postings. It retrieves the job data in JSON format.

2. **Data Cleaning:** The extracted data is cleaned, and certain data fields are converted to the appropriate data types. For example, date fields may be converted to datetime objects.

3. **Database Loading:** The cleaned data is loaded into a PostgreSQL database. The database connection is established using SQLAlchemy and Psycopg2.

## Configuration

Before running the project, you should configure the following settings:

1. **API Key:** You will need a RapidAPI API key to access the job board. Replace `YOUR_API_KEY` in the script with your actual API key.

2. **Database Connection:** Configure the connection details for your PostgreSQL database in the script. Update the `create_engine` call with your database URL, username, and password.

## Project Structure

The project structure may look like this:

```
data-engineering-job-pipeline/
│
├── job_pipeline.py          # Python script for the job pipeline
├── README.md                # Project README file
├── requirements.txt         # Dependencies for the project
├── .gitignore               # Gitignore file
```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/data-engineering-job-pipeline.git
   ```

2. Change your working directory to the project folder:

   ```bash
   cd data-engineering-job-pipeline
   ```

3. Configure the API key and database connection settings in the script.

4. Run the Python script to start the job pipeline:

   ```bash
   python job_pipeline.py
   ```

## Database Schema

The script will create a PostgreSQL table to store the job postings. The database schema should be defined in the script and will typically include fields such as job title, company, location, publication date, and job description.

## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb
