from flask import Flask, render_template, redirect, request, flash
import twitter_frisk as fts

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/search')
def search():
    status, tweets, hashtags = fts.frisk_tweets("cats")
    # tweets = request.args.get()
    hashtag_count = [11, 75, 99]
    status_list = [99, 0, 241234234, 66]

    return render_template("index.html",
                           hashtag_count=hashtags,
                           status_list=tweets)

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=True)
