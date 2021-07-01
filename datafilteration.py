# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 00:18:21 2021

@author: Meghani M. Mehboob

"""
import pandas as pd

import urbandb_template as db

sheetdf = db.readsheet()[0]


def getallclang():
    return sheetdf["TrendCodeLanguage"].unique().tolist()


def getallbycodelang(codelang, sortby):
    resdf = sheetdf.loc[sheetdf["TrendCodeLanguage"] == codelang]
    resdf = resdf.sort_values(by=[sortby], ascending=False, inplace=False)
    return resdf


def getalldata():
    resdf = sheetdf.sort_values(by=["Timestamp"], ascending=False, inplace=False)
    return resdf


def getUniqueTrending():
    lang_list = getallclang()
    maindflist = []
    for lang in lang_list:
        tempdf = sheetdf.loc[sheetdf["TrendCodeLanguage"] == lang]
        tempdf_top = tempdf.sort_values(by=["TrendStar", "TrendForked"], ascending=False, inplace=False).head(1)
        maindflist.append(tempdf_top)
    resdf = pd.concat(maindflist)
    return resdf
