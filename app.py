# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 01:58:14 2021

@author: Admin
"""

from flask import Flask, render_template

import datafilteration as fdb

app = Flask(__name__)

@app.route("/")
def main():
    clangs = fdb.getallclang()
    datas = fdb.getalldata().head(10).to_records()
    return render_template("index.html", clangs=clangs[0:10], datas=datas)


@app.route("/clang/<lang>")
def clang(lang):
    langs = [lang]
    datas = fdb.getallbycodelang(lang, "TrendStar").head(10).to_records()
    return render_template("index.html", clangs=langs, datas=datas)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
