#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, url, get, post, response, error
from requests_oauthlib import OAuth1Session
import json
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

@route("/")
def html_index():
    return template("index")

@route("/static/<filepath:path>", name="static_file")
def static(filepath):
    return static_file(filepath, root="./static")


@route("/show", method="GET")
def search_twitter():

    search_words = request.query.search_words

    C_KEY = "45jdaVys8C2BI6Db1qKB2mlvP"
    C_SECRET = "8wIjPoy1dobrUpTRgGA4YdPz11FHw1ngEDwo5YHI3e5iUKBERA"
    A_KEY = "2605089648-cizYH4DNgYhAHoW5SdgMzS5vaAd9S1nTg2aAI9O"
    A_SECRET = "F1YO38we9K3v65HHTOz2jiJKz7eoFxY6snZqkz8X71C1U"

    url = "https://api.twitter.com/1.1/search/tweets.json?"

    params = {
            "q": (search_words, "utf-8"),
            "lang": "ja",
            "result_type": "mixed",
            "count": "100"
            }
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.get(url, params = params)
    tweets = json.loads(req.text)

    if req.status_code == 200:
        for tweet in tweets["statuses"]:
            created_at = (tweet["created_at"])
            User = (tweet["user"]["screen_name"].encode("utf-8"))
            U_Name = (tweet["user"]["name"].encode("utf-8"))
            U_img = (tweet["user"]["profile_image_url"])
            Text = (tweet["text"].encode("utf-8"))

    return template("show",
                # Text=Text,
                # User=User,
                # U_Name=U_Name,
                # U_img=U_img,
                # created_at=created_at,
                # url=url
                tw=tw,
                req=req,
                tweets=tweets
                )
run(host="localhost", port=8080, debug=True, reloader=True)
