import pytest


"""Here we test the binary search for blind sqli tacking the parameter in order the test correctly"""

result_bool = True
operator1 = '>'
hight = 25
low = 0 
binary_average = 12
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

hight,low,binary_average = binary_search_for_blind_sqli(result_bool, operator1, hight, low, binary_average)
print(f"hight : {hight}, low: {low}, binary_average: {binary_average}")