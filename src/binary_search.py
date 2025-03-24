
"""
    Here the function use to do the binary search using the operator parameter (for the time-based blind SQLi)
    
"""
result_bool = False
status_code = 200
operator1 = ">"
high_bound = 25
low_bound = 0
mid_point = int((high_bound+low_bound)//2)


def binary_search_for_blind_sqli(result_bool: bool, operator1: str, hight: int, low: int, binary_average: int):
    if result_bool == True and operator1 =='<':
        hight = binary_average - 1
    if result_bool == True and operator1 =='>':
        low = binary_average + 1
    if result_bool == False and operator1 == '>':
        hight = binary_average - 1
    if result_bool == False and operator1 == '<':
        low = binary_average + 1
    return hight,low,binary_average 

def binary_search_for_error_sqli(status_code: int, operator1: str, hight: int, low: int, binary_average: int):
    if status_code != 200 and operator1 =='<':
        hight = binary_average - 1
    if status_code != 200 and operator1 =='>':
        low = binary_average + 1
    if status_code == 200 and operator1 == '>':
        hight = binary_average - 1
    if status_code == 200 and operator1 == '<':
        low = binary_average + 1
    return hight,low,binary_average 

high_bound, low_bound, mid_point = binary_search_for_blind_sqli(result_bool, operator1, high_bound, low_bound, mid_point)

print(f"Hight: {high_bound}, Low: {low_bound}, Binary Average: {mid_point}")