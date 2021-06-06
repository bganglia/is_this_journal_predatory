# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:16:14 2020

@author: Mike Brennan
"""

import requests
from bs4 import BeautifulSoup
#import json

URL = 'https://predatoryjournals.com/journals/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
uls = soup.find_all('ul')
journalNames = []
journalUrls = []
for ul in uls:
    lis = ul.find_all('li')
    for li in lis:
        a = li.find('a', href=True)
        if a is not None:
            journalName = a.text.encode('utf-8')
            journalUrl = a['href'].encode('utf-8')
            if(len(journalName)>3):
                journalNames.append(journalName)
                journalUrls.append(journalUrl)
                
        
