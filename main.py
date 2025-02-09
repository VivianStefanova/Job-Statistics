from src.MITM_scraper import get_response as mi
from src.API_scraper import get_response as api
import src.data_menager as sql


# response = mi(2)
# response2 = api(2)

# #print(response[0])  
# print(response[1])   
# print(".........................................................................................")
# print(response2[6])
# #print(response)
#sql.start_SQL("py_test", "py_table")
#data = mi(1,"", 20)
data1 = api(1, 20)
sql.insert_values(data1, True, "py_test", "py_table");


print("end")