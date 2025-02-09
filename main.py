from src.MITM_scraper import get_response as mi
from src.API_scraper import get_response as api
from src.bs_scraper import get_table
import src.data_manager as dm
import streamlit as st
import pandas as pd

st.title("Job Statistics")
st.subheader("Largest technology companies by revenue")
selected_year = st.selectbox("Select year", ["2023", "2021", "2020", "2019"])
st.write(get_table(selected_year))

st.subheader("Please enter nedded data")
api_id=st.text_input("Enter API ID")
api_key=st.text_input("Enter API key")
sql_host=st.text_input("Enter SQL host")
sql_user=st.text_input("Enter SQL user")
sql_password=st.text_input("Enter SQL password")

if st.button("Save inputs"):
    with open(".env", "w") as f:
        f.write(f"API_ID={api_id}\n")
        f.write(f"API_KEY={api_key}\n")
        f.write(f"SQL_HOST={sql_host}\n")
        f.write(f"SQL_USER={sql_user}\n")
        f.write(f"SQL_PASSWORD={sql_password}\n")
        st.write("Please restart the app to apply changes")

try:
    response = api()
    response2=mi()
except:
    st.write("API request failed. Change inputs.")

@st.cache_resource
def initialization_function():
    dm.start_SQL()    
    for i in range(1,10):
        dm.insert_values(api(i), True)
        dm.insert_values(mi(i), False)
if st.button("Create database and insert values"):        
    initialization_function()        

number_entries= dm.get_number_of_entries()
st.write(f"Number of entries in database: {number_entries}")

st.subheader("Company listings")
company = dm.get_company_data()
for i in company:
    st.write(i)

st.subheader("Salary data by month")
salary_data = pd.DataFrame(dm.get_salary_data(), columns=["posted_date", "salary_min", "salary_max"])
st.write(salary_data)

    