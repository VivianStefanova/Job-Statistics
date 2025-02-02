import requests
import re
from typing import List
def get_response(page:int=1, searchWord:str="", pageSize:int=20) -> dict:
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8,bg-BG;q=0.7,bg;q=0.6',
        'origin': 'https://www.dice.com',
        'priority': 'u=1, i',
        'referer': 'https://www.dice.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8',
    }

    params = {
        'q': searchWord,
        'locationPrecision': 'Country',
        'latitude': '42.733883',
        'longitude': '25.48583',
        'countryCode2': 'BG',
        'radius': '30',
        'radiusUnit': 'mi',
        'page': page,
        'pageSize': pageSize,
        'facets': 'employmentType|postedDate|workFromHomeAvailability|workplaceTypes|employerType|easyApply|isRemote|willingToSponsor',
        'fields': 'id|jobId|guid|summary|title|postedDate|modifiedDate|jobLocation.displayName|detailsPageUrl|salary|clientBrandId|companyPageUrl|companyLogoUrl|companyLogoUrlOptimized|positionId|companyName|employmentType|isHighlighted|score|easyApply|employerType|workFromHomeAvailability|workplaceTypes|isRemote|debug|jobMetadata|willingToSponsor',
        'culture': 'en',
        'recommendations': 'true',
        'interactionId': '0',
        'fj': 'true',
        'includeRemote': 'true',
    }

    response = requests.get('https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search', params=params, headers=headers)       
    if(response.status_code != 200):
        print(f"Scraper failiure: {response.status_code}")
        raise Exception(f"Scraper failiure: {response.status_code}")
    return response.json()["data"]        
def cleanSalary(salary:str) -> List[int]:
#-1 means Dependent on experience
#-2 means Not specified
    salary=salary.lower()
    if("experience" in salary or "doe" in salary or "exp" in salary):
       return [-1]
    numbers = re.findall('[\d,]+(\.\d+)?', salary)
    if(len(numbers) == 0 or len(numbers) > 2):
        return [-2]
    for i in numbers:
        numbers[i].replace(",","")
        numbers[i]=int(float(numbers[i]))
        if(numbers[i]<300):
            #Annual salary = hourly wage × hours per week × weeks per year(40 hours and 50 weeks)
            numbers[i]*=2000
    if(numbers[0] <1):
        return [-2]    
    return numbers
