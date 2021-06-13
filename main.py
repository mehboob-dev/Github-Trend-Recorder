# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:13:06 2021

@author: Meghani M. Mehboob

"""

import json
from datetime import datetime

import emoji as moji
import requests
from bs4 import BeautifulSoup

import urbandb_template as db

configfile = "main.json"
with open(configfile) as config:
    config = json.load(config)
# noinspection SpellCheckingInspection
if config["searchparticular"]:
    url = config["url"] + "/" + config["codelang"] + "?spoken_language_code=" + config["spokenlang"]
else:
    url = ""
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="js-pjax-container")

allTrending = results.find_all(class_="Box-row")
for trend in allTrending:
    try:
        trendtitle = moji.demojize(trend.find("p", class_="col-9 color-text-secondary my-1 pr-4").get_text().strip())
        if trendtitle is not None:
            trendlinks = trend.find(class_="h3 lh-condensed")
            trenddata = trend.find_all(class_="f6 color-text-secondary mt-2")[0]
            trendstar = trenddata.contents[3].get_text().strip()
            trendforked = trenddata.contents[5].get_text().strip()
            trendlink = "https://www.github.com" + trendlinks('a', href=True)[0]["href"]
            print("Title :", trendtitle)
            print("Nos. of Star :", trendstar)
            print("Nos. of Forked :", trendforked)
            print("Link :", trendlink)
            print("\n")
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            db.append_row(
                [timestamp, trendtitle.replace(",", ""), trendstar.replace(",", ""), trendforked.replace(",", ""),
                 trendlink])
    except Exception as e:
        print(e)
        continue
