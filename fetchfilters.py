import requests
from bs4 import BeautifulSoup
import emoji as moji

URL = "https://github.com/trending/python?since=daily&spoken_language_code=en"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="js-pjax-container")

def codelangfunc():
    codelanglist = []
    defaultlist = results.find_all(class_="Box-header d-md-flex flex-items-center flex-justify-between")
    codelangs = defaultlist[0].find("div", id="languages-menuitems").find_all(class_="select-menu-item-text")
    for lang in codelangs:
        clang = lang.get_text().strip()
        if not clang == "Clear language":
            codelanglist.append(clang)
    print(codelanglist)
    return codelanglist

def spokenlangfunc():
    spokenlanglist = {}
    defaultlist = results.find_all(class_="Box-header d-md-flex flex-items-center flex-justify-between")
    spokenlangs = defaultlist[0].find_all("div", {"data-filterable-for": "text-filter-field-spoken-language"})[0].find_all("a", "select-menu-item", href=True)
    for lang in spokenlangs:
        slangname = lang.get_text().strip()
        slangcode = lang["href"].split("spoken_language_code=")[1]
        if not slangname == "Clear spoken language":
            spokenlanglist[slangname]=slangcode
    print(spokenlanglist)
    return spokenlanglist

if __name__=="__main__":
    codelangfunc()
    spokenlangfunc()