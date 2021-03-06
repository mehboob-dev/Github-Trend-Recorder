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


def fixstringfordb(rawtext):
    return rawtext.replace(",", "")


def scrapper(alltrending, url, codelang, spokenlang, sheetdata, sheet):
    for trend in alltrending:
        try:
            trendtitle = trend.find("p", class_="col-9 color-text-secondary my-1 pr-4").get_text().strip()
            trendtitle = moji.demojize(trendtitle)
            if trendtitle is not None:
                trendlinks = trend.find(class_="h3 lh-condensed")
                trenddata = trend.find_all(class_="f6 color-text-secondary mt-2")[0]
                trendstar = trenddata.contents[3].get_text().strip()
                trendforked = trenddata.contents[5].get_text().strip()
                trendlink = "https://www.github.com" + trendlinks('a', href=True)[0]["href"]
                trendid = str(json.loads(trendlinks("a")[0]["data-hydro-click"])["payload"]["record_id"])
                print("Title :", trendtitle)
                print("Nos. of Star :", trendstar)
                print("Nos. of Forked :", trendforked)
                print("Link :", trendlink)
                print("CodeLang :", codelang)
                print("ID :", trendid)
                print("\n")
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                dbdata = [trendid, timestamp, fixstringfordb(trendtitle), fixstringfordb(trendstar),
                          fixstringfordb(trendforked), codelang, spokenlang, trendlink, url]
                db.append_row(dbdata, sheetdata, sheet)
        except Exception as e:
            print(e)
            continue


def param(url, codelang, spokenlang, sheetdata, sheet):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="js-pjax-container")
    alltrending = results.find_all(class_="Box-row")
    scrapper(alltrending, url, codelang, spokenlang, sheetdata, sheet)


def main():
    configfile = "main.json"
    with open(configfile) as config:
        config = json.load(config)

    if config["searchparticular"]:
        codelang = config["codelang"]
        spokenlang = config["spokenlang"]
        url = config["url"] + "/" + codelang + "?spoken_language_code=" + spokenlang + "?since=daily"
        sheetdata, sheet = db.readsheet()
        param(url, codelang, spokenlang, sheetdata, sheet)
    else:
        codelanglist = config["codelanglist"]
        spokenlanglist = config["spokenlanglist"]
        sheetdata, sheet = db.readsheet()
        for codelang in codelanglist:
            for spokenlang in spokenlanglist:
                url = config["url"] + "/" + codelang + "?spoken_language_code=" + spokenlang + "?since=daily"
                try:
                    param(url, codelang, spokenlang, sheetdata, sheet)
                except Exception as e:
                    print("Unable to Fetch from URL")
                    print(url)
                    print(e)
                    continue


if __name__ == "__main__":
    main()
