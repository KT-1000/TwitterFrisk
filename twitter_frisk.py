# Coding Challenge
# Implement a twitter search engine that displays tweets containing a
#     user submitted query string.

# For each result tweet,
    # display the name of the person who tweeted it,
    # the content of the tweet,
    # and the number of times it was favorited.

# Separate from the list of tweets above,
    # display a sidebar containing a list of hashtags present in the result set
    # along with a count for number of times it was present for each hashtag.

# The UI layout can be kept simple and is entirely up to you.

# Please use Python/Flask along with the Twitter API for this exercise,
# and stick to Python/Flask and code organization/design best practices as much as you can.

from urllib import quote_plus
import urllib3
import json
import base64
import secrets as sec


class FriskTweet(object):
    """ A Tweet Object consists of
        an author name,
        the body of the tweet,
        and the number of times the tweet was favorited.
    """
    def __init__(self, name, content, num_faves=0):
        self.name = name
        self.content = content
        self.favorited = num_faves

    def display_frisk_tweet(self):
        print 'Author: %s  Content: %s Favorited: %d' % (self.name, self.content, self.favorited)


def encode_search_string(user_str):
    """ Helper function. Takes user-entered search string and returns that string encoded for use as params in URL. """
    encoded_search_str = quote_plus(user_str)

    return encoded_search_str


def frisk_tweets_auth(consumer_key, secret_key):
    """ Takes in a consumer key and a secret key, returns a bearer token to be used in Twitter API calls.
    Note that this is necessary for the Twitter Search API:
    APPLICATION-ONLY AUTHENTICATION: https://dev.twitter.com/oauth/application-only
    """
    bearer_token = ""
    if consumer_key == "" or secret_key == "":
        return bearer_token

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
    bearer_token = json.loads(response.data.decode("utf-8"))

    return bearer_token


def frisk_auth_tweets_list(encoded_user_str):
    """ Takes an encoded string, and returns a status code and list of tweets. """
    # get bearer token
    bearer_token = frisk_tweets_auth(sec.CONSUMER_KEY, sec.CONSUMER_SECRET)

    # List of tweets aka statuses according to Twitter
    status_list = []

    # Each hashtag in result set is a key,
    # and the value will be a count of that hashtag incremented with each occurrence
    counted_hashtags = {}

    if bearer_token == "":
        return status_list, counted_hashtags

    # Create an HTTP connection pool manager
    manager = urllib3.PoolManager()

    # Format the Twitter URL appropriately
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + encoded_user_str

    # Set the Authorization header using the value of the bearer_token key
    http_headers = {'Authorization': 'Bearer %s' % bearer_token['access_token']}

    # Send the request
    r = manager.urlopen('GET', url, headers=http_headers)

    # Jsonify the request, so we can make each tweet
    json_statuses = json.loads(r.data)

    # Grab the values from json's statuses dict to create a new FriskTweet object
    for status in json_statuses["statuses"]:
        author = status["user"]["name"]
        content = status["text"]
        num_faves = status["favorite_count"]
        status_list.append(FriskTweet(author, content, num_faves))

        # hashtag list contains dictionaries with keys 'indices' and 'text'
        hashtag_list = status["entities"]["hashtags"]
        for hashtag_dict in hashtag_list:
            try:
                hashtag = hashtag_dict["text"]
                if hashtag in counted_hashtags:
                    counted_hashtags[hashtag] += 1
                else:
                    counted_hashtags[hashtag] = 1
            except IndexError as e:
                print e, hashtag_dict
                continue

    return status_list, counted_hashtags


def frisk_tweets(search_str):
    """ Takes in user-entered search string, returns a status message and list of tweets. """
    error_long_search = "Error: Invalid search. Please use ten or fewer words and operands."
    success_search = "OK"

    # by default, the search status is OK
    status = success_search

    # get list of words and operands from search string to make sure they meet Twitter's limit of 10
    words = search_str.split()
    if len(words) > 10:
        status = error_long_search

    # encode the search string to be used as params in URL
    encoded_search = encode_search_string(search_str)

    # get code, tweets, and hashtag dictionaries
    status_list, counted_hashtags = frisk_auth_tweets_list(encoded_search)

    return status, status_list
