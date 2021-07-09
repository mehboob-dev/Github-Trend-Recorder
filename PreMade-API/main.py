from datetime import datetime
import requests
import db
import pandas as pd
import json

sheetdata, sheet = db.readsheet()
base_url = "https://gh-trending-api.herokuapp.com/repositories/"
configfile = "../main.json"
with open(configfile) as config:
    config = json.load(config)

codelang = config["codelanglist"]
since = "daily"
spoken_lang = "en"
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

for code_lang in codelang:
    main_url = f"{base_url}{code_lang}?since={since}&spoken_language_code={spoken_lang}"
    response = requests.get(main_url)
    fetch_data = response.json()
    # print(fetch_data)

    for i in range(len(fetch_data)):
        data = pd.DataFrame.from_dict({k: [str(v)] for k, v in fetch_data[i].items()}, orient="columns").loc[0].tolist()
        data.append(timestamp)
        db.append_row(data, sheetdata, sheet)
