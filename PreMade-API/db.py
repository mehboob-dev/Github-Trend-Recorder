import time
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("../quickstart-1595793576826-f44fe7bdc04e.json", scope)
client = gspread.authorize(creds)

def readsheet():
    spreadsheet = client.open("Git-API -Recorder")
    sheet = spreadsheet.worksheet("c")
    sheetdata = pd.DataFrame(sheet.get_all_records())
    return sheetdata, sheet

def updaterow(sheet, cell_list, data):
    for i in range(len(cell_list)):
        cell_list[i].value = data[i]
    resp = sheet.update_cells(cell_list)
    return resp

def append_row(data, sheetdata, sheet):
    ind = sheetdata.index[sheetdata["url"] == data[3]]+2
    resp = "No Update Need"
    if not len(ind)>0:
        resp = sheet.append_row(data, value_input_option='RAW', insert_data_option="INSERT_ROWS", table_range=None)
    else:
        cell_list = sheetdata.iloc[ind[0]-2].to_list()
        if not str(cell_list[7]) == data[7] and str(cell_list[8]) == data[9] and str(cell_list[9]) == data[4]:
            cell_list = sheet.range("A" + str(ind[0]) + ":" + "I" + str(ind[0]))
            resp = updaterow(sheet, cell_list, data)
    time.sleep(1)
    print(resp)