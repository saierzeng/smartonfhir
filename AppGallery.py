# -*- coding: utf-8 -*-
"""
App Gallery Scraping

"""

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('https://apps.smarthealthit.org/apps').read()

soup = BeautifulSoup(page,"html.parser")
print(soup)

#name_box = soup.find('h3', attrs={'class': '_3EIwz'})
#name = name_box.text.strip()

data = []
for name_box in soup.find_all('h3', attrs={'class': '_3EIwz'}):
    name = name_box.text.strip()
    print(name)
    data.append(name)
df = pd.DataFrame(data)
df.columns = ['App']
  
data = []  
for name_box in soup.find_all('h4', attrs={'class': 'Hk23d'}):
    name = name_box.text.strip()
    print(name)
    data.append(name)
df['Company'] = data

data = []  
for name_box in soup.find_all('p', attrs={'class': '_2J297'}):
    name = name_box.text.strip()
    print(name)
    data.append(name)
df['ShortDesc'] = data



