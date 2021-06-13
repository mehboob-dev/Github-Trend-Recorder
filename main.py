# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:13:06 2021

@author: Meghani M. Mehboob

"""

import requests
from bs4 import BeautifulSoup
import emoji as moji
import fetchfilters as ff
import json

configfile = "main.json"
with open(configfile) as config:
    config = json.load(config)
if config["searchparticular"]:
    URL = config["url"]+"/"+config["codelang"]+"?spoken_language_code="+config["spokenlang"]
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="js-pjax-container")

allTrending = results.find_all(class_="Box-row")
for trend in allTrending:
    try:
        trendtitle = moji.demojize(trend.find("p", class_="col-9 color-text-secondary my-1 pr-4").get_text().strip())
        if not trendtitle == None:
            trendlinks = trend.find(class_="h3 lh-condensed")
            trenddata = trend.find_all(class_="f6 color-text-secondary mt-2")[0]
            trendstar = trenddata.contents[3].get_text().strip()
            trendforked = trenddata.contents[5].get_text().strip()
            trendlink = "https://www.github.com"+trendlinks('a', href=True)[0]["href"]
            print("Title :",trendtitle)
            print("Nos. of Star :",trendstar)
            print("Nos. of Forked :",trendforked)
            print("Link :",trendlink)
            print("\n")
    except:
        continue