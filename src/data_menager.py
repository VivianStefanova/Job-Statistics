import mysql.connector
import os
import dotenv

dotenv.load_dotenv()

SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

def start_SQL(database:str = "job_statistics", table:str = "job_data",
              mhost:str|None = SQL_HOST, muser:str|None = SQL_USER, mpassword:str|None = SQL_PASSWORD) ->None:
    try:
        mydb = mysql.connector.connect(
            host = mhost,
            user = muser,
            password = mpassword,
            use_pure=True
            )
    except:
        print("Connection to SQL failed")
        raise Exception("Connection to SQL failed")
   
    cursor = mydb.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    mydb.close()

    mydb = mysql.connector.connect(
        host = mhost,
        user = muser,
        password = mpassword,
        database = database,
        use_pure=True
        )

    cursor = mydb.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table} (title VARCHAR(255), company VARCHAR(255),
                        posted_date DATE, salary_min INT, salary_max INT, location VARCHAR(255),
                         contract_time VARCHAR(255), remote VARCHAR(10))""")
    mydb.close()
    print("Database and table created")

def insert_values(data:list, is_API:bool, database:str = "job_statistics", table:str = "job_data",
              mhost:str|None = SQL_HOST, muser:str|None = SQL_USER, mpassword:str|None = SQL_PASSWORD) ->None:
    if(is_API):
       from src.SQL_utils import get_insert_values_API_scraper as get_insert_values
    else:
        from src.SQL_utils import get_insert_values_MITM_scraper as get_insert_values  

    mydb = mysql.connector.connect(
        host = mhost,
        user = muser,
        password = mpassword,
        database = database,
        use_pure=True
        )
    values = [get_insert_values(i) for i in data]
    print (values)
    cursor = mydb.cursor()
    for i in values:
        print(len(i))
    insert_sting = f"""INSERT INTO {table} (title, company,
                        posted_date, salary_min, salary_max, location,
                         contract_time, remote) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.executemany(insert_sting, values)
    mydb.commit()
    mydb.close()
    print("Values inserted")

       
   
    