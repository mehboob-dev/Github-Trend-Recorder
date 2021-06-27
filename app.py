# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 01:58:14 2021

@author: Admin
"""

from flask import Flask, render_template, request, url_for, redirect

import datafilteration as fdb

app = Flask(__name__)

clangs = fdb.getallclang()
datas = fdb.getUniqueTrending().to_records()
footer = [
    "© 2021 MM Apps",
    "https://www.facebook.com/www.mmapps.in",
    "https://www.twitter.com/_mm_apps_",
    "https://www.instagram.com/mm.apps",
    "https://www.linkedin.com/in/mm-apps",
    "https://github.com/mehboob-dev/Github-Trend-Recorder"
]


@app.route("/")
def template_renderer():
    global clangs, datas
    return render_template("index.html", clangs=clangs, datas=datas, footer=footer)


@app.route("/news")
def main():
    global clangs, datas
    clangs = fdb.getallclang()
    if len(request.args) > 0:
        lang = request.args["reqlang"]
        datas = fdb.getallbycodelang(lang, "TrendStar").to_records()
    else:
        datas = fdb.getUniqueTrending().to_records()
    return redirect(url_for("template_renderer"))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
