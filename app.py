# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 01:58:14 2021

@author: Admin
"""

from flask import Flask, render_template, request, url_for, redirect

import datafilteration as fdb

app = Flask(__name__)

clangs = fdb.getallclang()
datas = fdb.getalldata().head(10).to_records()

@app.route("/")
def maintemp():
    global clangs, datas
    return render_template("index.html", clangs=clangs[0:12], datas=datas)

@app.route("/news")
def main():
    global clangs, datas
    clangs = fdb.getallclang()
    if len(request.args)>0:
        lang = request.args["reqlang"]
        datas = fdb.getallbycodelang(lang, "TrendStar").head(10).to_records()
    else:
        datas = fdb.getalldata().head(10).to_records()
    return redirect(url_for("maintemp"))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
