

from dataclasses import dataclass

"""
    Here the function use to do the binary search using the operator parameter (for the time-based blind SQLi)
    

The binary search is used to accelerate the research. The parameter are used in other function/file. Do not change the type of the value "result_bool"
is here to make the difference between good payload and bad payload in the blind_time_based SQLi.

"""

@dataclass
class BinarySearch:
    
    result_bool : bool 
    status_code : int = 200
    operator1 : str
    high_bound : int 
    low_bound : int
    mid_point : int 
        
    def binary_search_boolean(self, result_bool, operator1, hight, low, binary_average) -> int:
        if self.result_bool == True and self.operator1 =='<':
            hight = binary_average - 1
        if self.result_bool == True and self.operator1 =='>':
            low = binary_average + 1
        if self.result_bool == False and self.operator1 == '>':
            hight = binary_average - 1
        if self.result_bool == False and self.operator1 == '<':
            low = binary_average + 1
        return hight,low,binary_average 


    """
            The second function is a binary search function for the error SQLI. The status_code is the response of the response web page.
            Like you can read, they are no treatment of the web page have a reponse number != 200. 

    """

    def binary_search_coderr(self, status_code, operator1, hight, low, binary_average) -> int:
        if self.status_code != 200 and self.operator1 =='<':
            hight = binary_average - 1
        if self.status_code != 200 and self.operator1 =='>':
            low = binary_average + 1
        if self.status_code == 200 and self.operator1 == '>':
            hight = binary_average - 1
        if self.status_code == 200 and self.operator1 == '<':
            low = binary_average + 1
        return hight,low,binary_average 

#high_bound, low_bound, mid_point = binary_search_for_blind_sqli(result_bool, operator1, high_bound, low_bound, mid_point)

#print(f"Hight: {high_bound}, Low: {low_bound}, Binary Average: {mid_point}")

