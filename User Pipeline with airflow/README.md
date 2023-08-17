# Random User ETL Pipeline



This project implements a robust Extract, Transform, and Load (ETL) pipeline that extracts, processes, and stores random user data. 

## Project Overview

The Random User ETL Pipeline ETL Pipeline aims to automate the process of gathering user data from Random User Generator API, performing data transformations, and storing the processed data in a PostgreSQL database. The structured data is enriched with extracted elevant information from the user record.

## How it Works

1. **Data Extraction**: The pipeline queries a reputable "Random User Generator" API endpoint to fetch random user data. The data is fetched daily to ensure real-time information.

2. **Data Transformation**: The extracted data is meticulously processed and transformed into a structured DataFrame. 

3. **Data Loading**: The structured and enriched data is securely loaded into a dedicated PostgreSQL database table named "random_user_table" The PostgreSQL database acts as a centralized repository for easy access and analysis.

## Key Features

- **Dynamic Scheduling**: The pipeline is orchestrated to run daily, ensuring the database is always up-to-date with the latest job vacancies.

- **Error Resilience**: To ensure a seamless data extraction process, the pipeline is configured with robust error handling mechanisms. Failed tasks are automatically retried up to five times with a short delay between retries.


## Requirements

- Python 3.x
- Airflow
- Requests
- Pandas
- SQLAlchemy
- PostgreSQL

## Usage

1. Start up Airflow as configured in the docker-compose file using `docker-compose up -d`.

2. Set up a PostgreSQL database with credentials and ensure the connection URL is correctly provided in the script.

3. Choose a nr_calls

4. Run the pipeline with Airflow using the provided DAG, ensuring that the required connections and variables are properly configured.

## Contribution and Feedback

Contributions are welcomed to enhance and extend this ETL pipeline further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project

github: https://github.com/mujjeeb

