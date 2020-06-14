# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

  
import time 
from datetime import datetime as dt 
  
# change hosts path according to your OS 
# The following path is for Windows system
hosts_path = "C:\Windows\System32\drivers\etc\hosts"

# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block 
website_list = ["www.facebook.com","facebook.com","fb.com","www.amazon.in","amazon.in"] 
  
while True: 
    # work durations
    # In the following code restriction has been imposed 
    # from 5-22 (5AM - 10PM)
    if dt(dt.now().year, dt.now().month, dt.now().day,5) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22): 
        print("Can't access site in working hours") 
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in website_list: 
                if website in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + website + "\n") 
    else: 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 
  
            # removing hostnmes from host file 
            file.truncate() 
  
        print("Enjoy your unrestriced access") 
    time.sleep(5) 
