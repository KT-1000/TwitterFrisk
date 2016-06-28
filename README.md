# TwitterFrisk

TwitterFrisk is a search engine that uses the Twitter API to return tweets given a user-entered string. It also displays any hashtags used in the returned tweets, along with a count of how many times that hastag occurred.

![TwitterFrisk in action](/static/images/TwitterFrisk.PNG?raw=true "TwitterFrisk")

## <a name="technologiesused"></a>Technologies Used
- [Python](https://www.python.org/)
- [Flask](https://www.djangoproject.com/)
- [Twitter API](https://dev.twitter.com/rest/public/search)
- [Bootstrap](http://getbootstrap.com/)

## <a name="features"></a>Features
- [X] Displays Tweets containing a user submitted query string.
- [X] For each Tweet, displays the name of the person who tweeted, the content of the tweet, and the number of times the Tweet was favorited.
- [X] Sidebar displays a list of hashtags present in the result set, including number of times each hashtag was used in the results.

## <a name="Installation"></a>Installation

The (literal) key(s) to getting TwitterFrisk to run locally, aside from installing the dependencies listed in requirements.txt, is to create a secrets.py file. To get the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_TOKEN_SECRET contained in your personal secrets.py file, create a [Twitter application] (https://apps.twitter.com/). These keys will be used to generate the bearer token necessary to make Twitter Search API requests.

![Twitter App](/static/images/TwitterAppAccess.PNG?raw=true "Twitter App Access")

## <a name="Testing"></a>Testing

TwitterFrisk was created using Test-Driven Development.

