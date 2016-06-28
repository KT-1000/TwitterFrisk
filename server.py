from flask import Flask, render_template, redirect, request, flash
import twitter_frisk as fts

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/search')
def search():
    search_str = request.args.get("search-term")
    status, tweets, hashtags = fts.frisk_tweets(search_str)

    return render_template("index.html",
                           hashtags=hashtags,
                           status_list=tweets)

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=True)
