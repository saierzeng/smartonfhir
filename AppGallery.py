# -*- coding: utf-8 -*-
"""
App Gallery Scraping

"""

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

quote_page = ['https://apps.smarthealthit.org/apps/page/1', 'https://apps.smarthealthit.org/apps/page/2', 'https://apps.smarthealthit.org/apps/page/3']
appended_df = []

for pg in quote_page:
    page = urlopen(pg)
    soup = BeautifulSoup(page,"html.parser")
    
    # SINGLE FIND
    #name_box = soup.find('h3', attrs={'class': '_3EIwz'})
    #name = name_box.text.strip()


    # App Name
    data = []
    for name_box in soup.find_all('h3', attrs={'class': '_3EIwz'}):
        name = name_box.text.strip()
        print(name)
        data.append(name)
    df = pd.DataFrame(data)
    df.columns = ['App']
  

    # Company
    data = []  
    for name_box in soup.find_all('h4', attrs={'class': 'Hk23d'}):
        name = name_box.text.strip()
        print(name)
        data.append(name)
    df['Company'] = data


    # Description
    data = []  
    for name_box in soup.find_all('p', attrs={'class': '_2J297'}):
        name = name_box.text.strip()
        print(name)
        data.append(name)
    df['ShortDesc'] = data


    # User (Designed for:)
    data = []  
    for name_box in soup.find_all('div', attrs={'class': '_1odWS'}):
        name = name_box.text.strip()
        name1 = name.split(': ')
        print(name1[1])
        data.append(name1[1])
    df['User'] = data


    # Website abbr: after clicking into an app, the tail of the web url
    data = []  
    for name_box in soup.find_all('a', attrs={'href': re.compile("/app/")}):
        print(name_box['href'])
        data.append(name_box['href'])
    df['pg.abbr'] = data[1:]
    
    df
    # store DataFrame in list
    appended_df.append(df)

appended_df = pd.concat(appended_df, axis=0)
# write DataFrame to an excel sheet 
appended_df.reset_index().to_excel('All Apps.xlsx')
