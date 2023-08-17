from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
import requests
import pandas as pd
from sqlalchemy import create_engine


# Function to get Data from API
def get_data_from_api():
    #VARIABLES DECLARATION
    url = "https://randomuser.me/api/"
    
    response = requests.get(url)
    user_data = response.json()
    return user_data


# Function to extract relevant credentials
def extract_relevant_credentials(data,nr_calls):
    first_name=[]
    last_name=[]
    gender=[]
    email=[]
    date_of_birth=[]
    country=[]
    street_address=[]
    city=[]
    state=[]
    postcode=[]
    phone=[]
    cell=[]
    
    for i in range (nr_calls):
        first_name.append(data[i]['results'][0]['name']['first'])
        last_name.append(data[i]['results'][0]['name']['last'])
        gender.append(data[i]['results'][0]['gender'])
        email.append(data[i]['results'][0]['email'])
        # Format date to datetime object  "yyyy-mm-dd" 
        date_string = data[i]['results'][0]['dob']['date']
        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        # Parse the string into a datetime object
        parsed_date = datetime.strptime(date_string, date_format)
        # Extract and format the date
        # use this if you want the date in string format formatted_date = parsed_date.strftime('%Y-%m-%d') 
        formatted_date = parsed_date.date()
        date_of_birth.append(formatted_date)  
        country.append(data[i]['results'][0]['location']['country'])
        #Format street address in a string "House {number}, {street name}"
        street_string = f"House {data[i]['results'][0]['location']['street']['number']}, {data[i]['results'][0]['location']['street']['name']}"
        street_address.append(street_string)
        city.append(data[i]['results'][0]['location']['city'])
        state.append(data[i]['results'][0]['location']['state'])
        postcode.append(data[i]['results'][0]['location']['postcode'])
        phone.append(data[i]['results'][0]['phone'])
        cell.append(data[i]['results'][0]['cell'])
    return first_name,last_name,gender,email,date_of_birth,country,street_address,city,state,postcode,phone,cell
   
# Function to translate extractions to Dataframe
def translate_extractions_to_dataframe(first_name,last_name,gender,email,date_of_birth,country,street_address,city,state,postcode,phone,cell):   
    #placing values into columns
    user_dict = {"first_name": first_name,"last_name":last_name,
        "gender":gender,
        "email":email,
        "date_of_birth":date_of_birth,
        "country":country,
        "street_address":street_address,
        "city":city,
        "state":state,
        "postcode":postcode,
        "phone": phone,
        "cell": cell}
    user_df = pd.DataFrame(user_dict)
    return user_df

# Function to create a table in Postgres
def to_sql_task(df,table_name):
    engine = create_engine('postgresql://airflow:airflow@host.docker.internal:5436/postgres')
    df.to_sql(table_name, engine)

# nr_calls determines number of records to be extracted(Amount of times the API endpoint gets called)
nr_calls = 5
data=[]
for i in range (nr_calls):
    data.append(get_data_from_api())

first_name,last_name,gender,email,date_of_birth,country,street_address,city,state,postcode,phone,cell=extract_relevant_credentials(data,nr_calls)
df = translate_extractions_to_dataframe(first_name,last_name,gender,email,date_of_birth,country,street_address,city,state,postcode,phone,cell)


default_args={
    'owner':'mujjeeb',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
    
}

with DAG(
    dag_id='random_user_v2',
    description='Random user: an ETL pipeline',
    start_date=datetime(2023,16,1),
    schedule_interval='@daily',
    default_args = default_args    
    )as dag:
    
    get_data_fromapi = PythonOperator(
        task_id = 'get_data_from_api',
        python_callable = get_data_from_api
        
    )
    
    
    extract_relevant_credential = PythonOperator(
        task_id = 'extract_relevant_credentials',
        python_callable = extract_relevant_credentials,
        provide_context = True,
        op_args=[data,nr_calls]
        
    )    

    load_db=PythonOperator(
        task_id='load_db',
        python_callable=to_sql_task,
        op_args=[df,'random_user']
        
    )
    
    # Define the task dependencies

get_data_fromapi >> extract_relevant_credential  >> load_db