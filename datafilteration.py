# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 00:18:21 2021

@author: Meghani M. Mehboob

"""

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
