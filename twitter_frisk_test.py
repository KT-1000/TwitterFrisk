import unittest
import twitter_frisk as fts
import secrets as sec

# TWITTER SEARCH API BEST PRACTICES
# https://dev.twitter.com/rest/public/search
#   1. Ensure all parameters are properly URL encoded.
#   2. Limit your searches to 10 keywords and operators.
#   3. Queries can be limited due to complexity. If this happens the Search API will respond with the error:
#       {"error":"Sorry, your query is too complex. Please reduce complexity and try again."}.
#   4. The Search API is not complete index of all Tweets, but instead an index of recent Tweets.
#       At the moment that index includes between 6-9 days of Tweets.


class TestReturnTweets(unittest.TestCase):

    def test_return_exists(self):
        """ Search must return at least one tweet. """
        s = "cat"
        status, tweet_list, hashtags = fts.frisk_tweets(s)
        self.assertIsNotNone(tweet_list, self)


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
        status, tweets, hashtags = fts.frisk_tweets(s)
        self.assertEqual(status, "OK")


class TestTwitterAPI(unittest.TestCase):

    def test_failed_authentication(self):
        """ Bad authentication returns an empty string as a bearer token. """
        bearer_token = fts.frisk_tweets_auth("", "")
        self.assertEqual(bearer_token, "")

    def test_passed_authentication(self):
        """ Note that this app uses Application-Only Authentication (vs Application-User Authentication)
        https://dev.twitter.com/oauth/application-only
        """
        bearer_token = fts.frisk_tweets_auth(sec.CONSUMER_KEY, sec.CONSUMER_SECRET)
        self.assertNotEqual(bearer_token, "")

    def test_list_tweets_returned(self):
        """ A user string should return a list of tweets. """
        s = "Brexit"
        status, tweets, hashtags = fts.frisk_tweets(s)
        self.assertGreaterEqual(len(tweets), 0)
        self.assertEqual(status, "OK")


if __name__ == '__main__':
    unittest.main()
