# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 00:18:21 2021

@author: Meghani M. Mehboob

"""

import urbandb_template as db
import pandas as pd

sheetdf = db.readsheet()[0]

def getallbycodelang(codelang, sortby):
    resdf = sheetdf.loc[sheetdf["TrendCodeLanguage"] == codelang]
    resdf = resdf.sort_values(by=[sortby], ascending=False, inplace=False)

getallbycodelang("python","TrendStar")


# if __name__ == "__main":
#     main()