# -*- coding: utf-8 -*-
"""
Created on

@author: MMApps
@contact: mehboob_dev@mmappps.in
@ProjectName: UrbanDBCrossPlatform-MMApps
Contact for Getting Subscription. Many More Method on Way..!!
"""

import os
import requests
import pandas as pd

SHEETNAME = "Sheet1"
API = "Get you API from https://urbandb.mmapps.in"

def request_url():
    """

    Returns
    -------
    url
        INTERNAL FUNCTION.

    """
    return "https://urbandb.mmapps.in/"+API+"/"+SHEETNAME

def get_all_rows():
    """

    Returns
    -------
    JSON
        IT WILL RETURN COMPLETE SHETE IN A JSON FORMAT.

    """
    return pd.DataFrame.from_dict(requests.get(request_url()+"/getAllRows").json())

def get_row(rowindex):
    """

    Parameters
    ----------
    rowindex : INT
        PASS THE INDEX OF ROW OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    JSON
        IT WILL RETURN THE ROW AT THE ENTERED INDEX IN JSON FORMAT.

    """
    return requests.get(request_url()+"/getRow/"+str(rowindex+1)).json()

def get_column(columnindex):
    """

    Parameters
    ----------
    columnindex : INT
         PASS THE INDEX OF COLUMN OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    JSON
        IT WILL RETURN ROW DATA AT THE ENTERED INDEX IN JSON FORMAT.

    """
    return requests.get(request_url()+"/getColumn/"+str(columnindex)).json()

def get_cell(rowindex, columnindex):
    """
    Parameters
    ----------
    rowindex : INT
        PASS THE INDEX OF ROW OF WHICH YOU REQUIRED DATA.
        .
    columnindex : INT
        PASS THE INDEX OF COLUMN OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    STRING
        IT WILL RETURN THE CELL VALUE FROM THE ENTERED CORDINATES

    """
    celladdress=str(rowindex+1)+"/"+str(columnindex)
    return requests.get(request_url()+"/getCell/"+celladdress).json()

def get_header():
    """

    Returns
    -------
    LIST
        IT WILL RETURN HEADER IN A LIST FORMAT

    """
    return requests.get(request_url()+"/getHeader").json()

def append_row(rowdata):
    """

    Parameters
    ----------
    rowdata : STRING
        EXAMPLE ("THIS,IS,A,SAMPLE,STRING")
        ENTER THE STRING WITH COMMA SEPRETED STYLE WITH INCERTED COMMA AT START AND END.

    Returns :
    -------
    JSON
        IT WILL RETURN INFORMATION WITH CORDINATES OF UPLOADED DATA.

    """
    return requests.get(request_url()+"/appendRow?data="+str(','.join(rowdata))).json()

def append_rows(rowsdata):
    """

    Parameters
    ----------
    rowsdata : STRING
        EXAMPLE ("THIS,IS,A,SAMPLE,STRING>>P,Y,T,H,O,N>>I,S>>P,O,W,E,R")
        ENTER THE STRING WITH COMMA SEPRETED STYLE WITH INCERTED COMMA AT START AND ENDFOR EACH ROW.
        SEPERATE ROW USING >>

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return requests.get(request_url()+"/appendRows?data="+str(','.join(rowsdata.split(",")))).json()

def upload_file(filepath):
    """

    Parameters
    ----------
    filepath : STRING
        ENTER THE FILE LOCATION.

    Returns
    -------
    JSON
        RETURN THE MESSAGE WHEATHER UPLOAD IS SUCESSFUL OR NOT.

    """
    payload = {}
    files = [
      ('file', open(filepath,'rb'))
    ]
    headers= {}
    reqdest = "https://urbandb.mmapps.in/"+API+"/upload"
    response = requests.request("POST", reqdest, headers=headers, data = payload, files = files)
    return response.text#.encode('utf8')

def download_file(filename, downloadpath=""):
    """

    Parameters
    ----------
    filename : STRING
        ENTER THE FILE NAME DURING UPLOAD.
    downloadpath : PATH, optional
        PATH TO DOWNLOAD LOCATION, DO NOT PASS ANY VALUE
        IF YOU WANT TO DOWNLOAD ON ROOT DIRECTORY OF CODE. The default is "".

    Returns
    -------
    None.

    """
    reqfile = requests.get("https://urbandb.mmapps.in/getupload/"+API+"/"+str(filename)).url
    response=requests.get(reqfile)
    with open(os.path.join(downloadpath,reqfile.split("/")[-1]), 'wb') as downloadfile:
        downloadfile.write(response.content)
    return "Download Done"

def verify_user(idcolumn,userid,passwordcolumn):
    """

    Parameters
    ----------
    idcolumn : STRING
        ENTER THE COLUMNNAME IN WHICH USERID EXIST.
    userid : STRING
        ENTER THE USERID WHICH YOU NEED TO VERIFY.
    passwordcolumn : STRING
        ENTER THE PASSWORD COLUMN NAME TO GET PASSWORD FROM DATABASE.

    Returns
    -------
    STRING
        IT RETURNS USER PASSWORD.

    """
    args = ((idcolumn,userid,passwordcolumn))
    return requests.get(request_url()+"/verifyuser/"+"/".join(args)).text


# print(get_all_rows())
# print(get_row(1))
# print(get_column(1))
# print(get_cell(1, 1))
# print(append_row("p,y,t,h,o,n"))
# print(get_header())
# print(append_rows("p,y,t,h,o,n>>i,s>>p,o,w,e,r"))
# print(upload_file("path/to/file"))
# print(download_file("0.jpg"))#.text
# print(verify_user("Rep", "Howard", "OrderDate"))