# Coding Challenge
# Implement a twitter search engine that displays tweets containing a
#     user submitted query string.

# For each result tweet,
    # display the name of the person who tweeted it,
    # the content of the tweet,
    # and the number of times it was favored.

# Separate from the list of tweets above,
    # display a sidebar containing a list of hashtags present in the result set
    # along with a count for number of times it was present for each hashtag.

# The UI layout can be kept simple and is entirely up to you.

# Please use Python/Flask along with the Twitter API for this exercise,
# and stick to Python/Flask and code organization/design best practices as much as you can.

from urllib import quote_plus
import urllib3
import requests
import json
import base64
error_long_search = "Error: Invalid search. Please use ten or fewer words and operands."
success_search = "OK"


def encode_search_string(user_str):
    """ Helper function. Takes user-entered search string and returns that string encoded for use as params in URL. """
    encoded_search_str = quote_plus(user_str)

    return encoded_search_str


def frisk_tweets_auth(consumer_key, secret_key):
    """ Takes in a consumer key and a secret key, returns a bearer token to be used in Twitter API calls.
    Note that this is necessary for the Twitter Search API:
    APPLICATION-ONLY AUTHENTICATION: https://dev.twitter.com/oauth/application-only
    """
    # Create an HTTP connection pool manager
    manager = urllib3.PoolManager()

    # Twitter OAuth 2 endpoint
    oauth_url = 'https://api.twitter.com/oauth2/token'

    # Set the HTTP request headers, including consumer key and secret
    http_headers = {'Authorization': "Basic %s" % base64.b64encode("%s:%s" % (consumer_key, secret_key)),
                    'Content-Type': 'application/x-www-form-urlencoded'}

    # Set the payload to the required OAuth grant type, in this case client credentials
    request_body = "grant_type=client_credentials"

    # Send the request
    response = manager.urlopen("POST", oauth_url, headers=http_headers, body=request_body)

    # Read the response as JSON
    app_token = json.loads(response.data.decode("utf-8"))

    return app_token


def frisk_tweets_encoded(encoded_str):
    """ Takes an encoded string, returns a status code and list of tweets. """
    code = 0
    tweets = []
    # format the twitter api search url
    search_root = "https://api.twitter.com/1.1/search/tweets.json?q="
    search_url = search_root + encoded_str
    r = requests.get(search_url)
    # HTTP 400 Bad Request
    if r.status_code == 400:
        r_json = r.json()
        code = r_json["errors"][0]['code']
    return code, tweets


def frisk_tweets(search_str):
    """ Takes in user-entered search string, returns list of tweets. """
    # by default, the search status is OK
    status = success_search

    # get list of words and operands from search string to make sure they meet Twitter's limit of 10
    words = search_str.split()
    if len(words) > 10:
        status = error_long_search

    # encode the search string to be used as params in URL
    encoded_search = encode_search_string(search_str)

    tweet_list = []

    return status, tweet_list


