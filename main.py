from src.MITM_scraper import get_response as mi
from src.API_scraper import get_response as api
import src.data_menager as sql
import mysql.connector
# response = get_response(1,10)
# for i in response:
#     if("salary_min" in i):
#         print(i["salary_min"])
#     else : print("No salary")    

# response = get_response(2,10);
# for i in response:
#     if("salary_min" in i):
#         print(i["salary_min"])
#     else : print("No salary")   

# response = mi(2)
# response2 = api(2)

# #print(response[0])  
# print(response[1])   
# print(".........................................................................................")
# print(response2[6])
# #print(response)
sql.start_SQL("py_test", "py_table")


print("end")