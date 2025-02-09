import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_table(year:str="2023") -> pd.DataFrame:
    index= {"2023": 1 , "2021":2 ,"2020":3, "2019":4, "2018":4}
    page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue")

    soup = BeautifulSoup(page.text,features="html.parser")

    tables = soup.find_all('table')

    table = tables[index[year]]
    table_titles = [i.text.strip() for i in table.find_all('th')] # type: ignore

    values=[]
    for data in table.find_all('tr')[1:]: # type: ignore
        row_data = [i.text.strip() for i in data.find_all('td')] # type: ignore
        values.append(row_data)

    return pd.DataFrame(values,columns = table_titles)