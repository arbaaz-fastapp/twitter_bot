import tweepy
from time import sleep
from config import create_api
from settings import QUERY, FOLLOW, LIKE, SLEEP_TIME
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info("Twitter bot which retweets,like tweets and follow users.🤖")
logger.info("Bot Settings")
logger.info(f"Like Tweets : {LIKE}")
logger.info(f"Follow users : {FOLLOW}")

api = create_api()

# Loop through all tweets that contain QUERY keyword.
# You can provide an integer argument to items() to get that much tweets.
for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    print(tweet.retweeted)
    try:
        logger.info(f"Tweet by: @{tweet.user.screen_name}, tweet id: {tweet.id}")
        # Retweet the tweet
        tweet.retweet()
        logger.info("Retweeted the tweet")

        # Favorite(Like) the tweet
        if LIKE:
            tweet.favorite()
            logger.info("Favorited the tweet")

        # Follow the user who tweeted
        if FOLLOW:
            # Check that bot is not already following the user
            if not tweet.user.following:
                tweet.user.follow()
                logger.info("Followed the user")

        logger.info(f"Waiting for {SLEEP_TIME} seconds....")
        sleep(SLEEP_TIME)
        print()

    except tweepy.TweepError as e:
        logger.info(e.reason)

    except KeyboardInterrupt:
        logger.info("Bot has been interrupted.😵")
        break
