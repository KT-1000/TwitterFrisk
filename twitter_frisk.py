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

from urllib.parse import quote_plus


error_long_search = "Error: Invalid search. Please use ten or fewer words and operands."
success_search = "OK"


def encode_search_string(user_str):
    """ Helper function. Takes user-entered search string and returns that string encoded for use as params in URL. """
    encoded_search_str = quote_plus(user_str)

    return encoded_search_str


def frisk_tweets_encoded(encoded_str):
    """ Takes an encoded string, returns a status code and list of tweets. """
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
    # TODO insert actual twitter calls here

    return status, tweet_list


