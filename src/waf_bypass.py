import requests
import re

from dataclasses import dataclass
from abc import ABC, abstractmethod

"""
    Here you will see different method to bypass WAF. From basic url encoding to playing with URL
    following the language use in the backend, you can perform different type of encoding payload automation. Of course, you can
    use it with other function on PuzzleSQL or you're own function. Make sure to see the documentation to use it correctly.
    Like the other function, the function here will be very simple.    

"""


class Encoding(ABC):
    @abstractmethod
    def simple_encoding():
        pass

    @abstractmethod
    def double_encoding():
        pass



class URL_encoding(Encoding): 
    
    def simple_enconding(sql_payload: str) -> str:
        new_sql = sql_payload.replace(" ", "+")
        new_sql = new_sql.replace("=","%3D")
        new_sql = new_sql.replace("'","%27")
        new_sql = new_sql.replace("(","%28")
        new_sql = new_sql.replace(")","%29")
        return new_sql

    def double_encoding(sql_payload:str) -> str:
        new_sql = sql_payload.replace(" ", "+")
        new_sql = new_sql.replace("=","%253D")
        new_sql = new_sql.replace("'","%2527")
        new_sql = new_sql.replace("(","%2528")
        new_sql = new_sql.replace(")","%2529")
        return new_sql
    


class HTML_encoding(Encoding):
        pass
    
    

class SQL_cha(Encoding):
        pass


#https://portswigger.net/web-security/essential-skills/obfuscating-attacks-using-encodings#obfuscation-via-xml-encoding
#https://www.yeswehack.com/fr/learn-bug-bounty/web-application-firewall-bypass
#https://www.picussecurity.com/resource/blog/waf-bypass-using-json-based-sql-injection-attacks


#based on https://owasp.org/www-community/attacks/SQL_Injection_Bypassing_WAF poru exemple.
