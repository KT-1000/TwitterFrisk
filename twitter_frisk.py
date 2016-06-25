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


def frisk_tweets(search_str):
    """ Takes in user-entered search string, returns list of tweets. """
    # by default, the search status is OK
    status = "OK"

    # get list of words and operands from search string to make sure they meet Twitter's limit of 10
    words = search_str.split()
    if len(words) > 10:
        status = "Error: Invalid search. Please use ten or fewer words and operands."

    tweet_list = []
    # TODO insert actual twitter calls here
    return status, tweet_list
