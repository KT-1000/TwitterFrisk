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
import unittest
import twitter_frisk as fts


class TestReturnTweets(unittest.TestCase):

    def test_return_exists(self):
        """ Search must return at least one tweet. """
        s = "cat"
        status, tweet_list = fts.frisk_tweets(s)
        self.assertIsNotNone(tweet_list, self)

# TWITTER SEARCH API BEST PRACTICES
# https://dev.twitter.com/rest/public/search
#   1. Ensure all parameters are properly URL encoded.
#   2. Limit your searches to 10 keywords and operators.
#   3. Queries can be limited due to complexity. If this happens the Search API will respond with the error:
#       {"error":"Sorry, your query is too complex. Please reduce complexity and try again."}.
#   4. The Search API is not complete index of all Tweets, but instead an index of recent Tweets.
#       At the moment that index includes between 6-9 days of Tweets.


class TestSearchEncoding(unittest.TestCase):

    def test_encoding(self):
        """ Make sure query string can be encoded successfully. """
        s = "it's balloonicorn!"
        encoded = fts.encode_search_string(s)
        self.assertEqual(encoded, "it%27s+balloonicorn%21")


class TestSearchString(unittest.TestCase):

    def test_search_length(self):
        """ Best practice: must be no more than 10 keywords and operators per search. """
        s = '1 2 3 4 5 6 7 8 9 10'
        status, tweet_list = fts.frisk_tweets(s)
        self.assertLessEqual(status, "OK")

# TODO Limit Query complexity test.


class TestTwitterAPI(unittest.TestCase):

    def test_failed_authentication(self):
        """ Bad authentication returns error code 215. """
        s = "it%27s+balloonicorn%21"
        code, tweets = fts.frisk_tweets_encoded(s)
        self.assertEqual(code, 215)

if __name__ == '__main__':
    unittest.main()

