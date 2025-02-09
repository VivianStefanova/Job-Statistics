from typing import List, Tuple
import src.MITM_scraper as mi
import src.API_scraper as api

def clean_date(date:str) -> str:
    return date.split('T')[0]

def clean_contract_time(contract_time:str) -> str:
    contract_time=contract_time.lower()
    if("full" in contract_time):
        return "full_time"
    if("part" in contract_time):
        return "part_time"
    if("contract" in contract_time):
        return "contract"
    if("third" in contract_time):
        return "third_party"
    return "unknown"

def has_data(data:dict, data_name:str) -> str:
    if(data_name in data and data[data_name] != None):
        return data[data_name]
    return "unknown"

def get_insert_values_MITM_scraper(data:dict) -> Tuple[str]:
    
    res = []
    res.append(has_data(data, "title"))
    res.append(has_data(data, "companyName"))
    res.append(clean_date(data["postedDate"]))
    if("salary" in data):
        sal = mi.clean_salary(data["salary"])
        if(len(sal) == 1):
            res.append(sal[0])
            res.append(sal[0])
        else:   
            res.append(sal[0])
            res.append(sal[1])    
    else:
        res.append(-2)
        res.append(-2)
    if("jobLocation" in data):
        res.append(data["jobLocation"]["displayName"].split(",")[1].strip())
    else: res.append("unknown")       
    if("employmentType" in data):
        res.append(clean_contract_time(data["employmentType"]))
    else: res.append("unknown")
    res.append(has_data(data, "isRemote"))
    return tuple(res)

def get_insert_values_API_scraper(data:dict) -> Tuple[str]:
    res = []
    res.append(has_data(data, "title"))
    if("company" in data):
        res.append(data["company"]["display_name"])
    else: res.append("unknown")    
    res.append(clean_date(data["created"]))
    if("salary_min" in data):
        res.append(api.clean_salary(data["salary_min"]))
    else: res.append(-2)
    if("salary_max" in data):
        res.append(api.clean_salary(data["salary_max"]))
    else: res.append(-2)    
    if("location" in data):
        res.append(data["location"]["area"][0])
    else: res.append("unknown")       
    if("contract_time" in data):
        res.append(clean_contract_time(data["contract_time"]))
    else: res.append("unknown")
    res.append("unknown")
    return tuple(res)

