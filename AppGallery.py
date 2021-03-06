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
# To reset index column
appended_df = appended_df.reset_index(drop=True)

# Long Description
# Unorganized
source = 'https://apps.smarthealthit.org'

data = []
for abbr in appended_df['pg.abbr']:
    app_url = source + abbr
    app_pg = urlopen(app_url)
    app_soup = BeautifulSoup(app_pg,"html.parser")
    data.append(app_soup.find_all('div', attrs={'class': '_3tpF_'})[0].text)
    
appended_df['Long Description'] = data

# write DataFrame to an excel sheet 
appended_df.to_excel('All Apps.xlsx')

