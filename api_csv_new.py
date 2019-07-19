# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 23:43:37 2019

@author: Priyotosh PC
"""

from bs4 import BeautifulSoup
import requests
import csv

for i in range(1,2610):    
    with open(str(i)+".html",errors='ignore') as html_file:
        soup = BeautifulSoup(html_file,'lxml')
    
        api_list = open('api_list.txt','r')
        api_list_arr=[]
        for x in api_list:
            api_list_arr.append(x.strip())
        #print(api_list_arr)
            
        find_div=soup.find(id="api-info-container")
        #print(find_div)
        
        find_ul=find_div.findAll('ul')
        #print(find_ul)
        
        parsed_arr=[]
        for x in find_ul:
            #print(x.li.text)
            parsed_arr.append(x.li.text)
        #print(parsed_arr)
        
        flag_arr=[]    
        for x in api_list_arr:
            flag = 0
            for y in parsed_arr:
                if x==y:
                    flag=1
                    break
                elif x!=y:
                    flag=0
            flag_arr.append(flag)
        #print(flag_arr)
        
        with open('api.csv','a') as fd:
            writer=csv.writer(fd)
            writer.writerow(flag_arr)