import os
from typing import List

import requests
import dotenv
dotenv.load_dotenv()

API_ID1 = os.getenv("API_ID")


def get_response(page:int = 1, page_size:int = 20, id = '') -> List[dict]:
    dotenv.load_dotenv()

    API_ID = os.getenv("API_ID")
    print(API_ID)
    API_KEY = os.getenv("API_KEY")
    if(id == ''): id = API_ID

    if not API_KEY or not API_ID:
        raise ValueError("No API key or ID provided!")
    params = {
    'app_id': id,
    'app_key': API_KEY,
    'results_per_page': page_size,
    'category': 'it-jobs',
    }
    try:
        response = requests.get(f'https://api.adzuna.com/v1/api/jobs/gb/search/{page}', params=params)
    except:
        raise Exception("API request failed")
    if(response.status_code != 200):
        print(f"Scraper failiure: {response.status_code}")
        raise Exception(f"Scraper failiure: {response.status_code}")
    return response.json()["results"]  
   
def clean_salary(salary:str) -> int:
    return int(float(salary))