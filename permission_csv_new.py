# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:56:13 2019

@author: Priyotosh PC
"""

from bs4 import BeautifulSoup
import requests
import csv
    
for i in range(1,2610):    
    with open(str(i)+".html",errors='ignore') as html_file:
        soup = BeautifulSoup(html_file,'lxml')
    
        permission_list = open('permission_list1.txt','r')
        permission_list_arr=[]
        for x in permission_list:
            permission_list_arr.append(x.strip())
        #print(permission_list_arr)
        
        match = soup.find(id="permission-table")
        #print(match)
        
        t_body = match.tbody
        #print(t_body)
        
        find_tr = t_body.findAll('tr')
        
        parsed_arr=[]
        for x in find_tr:
            parsed_arr.append(x.td.text)
        
        flag_arr=[]    
        for x in permission_list_arr:
            flag = 0
            for y in parsed_arr:
                if x==y:
                    flag=1
                    break
                elif x!=y:
                    flag=0
            flag_arr.append(flag)
        #print(flag_arr)
        
        with open('document.csv','a') as fd:
            writer=csv.writer(fd)
            writer.writerow(flag_arr)