import tweepy
from time import sleep
from config import create_api
from settings import FOLLOW, LIKE, HANDLER, SLEEP_TIME
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info("Twitter bot which retweet and like tweets of a users's 20 recent tweets.🤖")
logger.info("Bot Settings")
logger.info(f"Like Tweets : {LIKE}")
logger.info(f"Follow users : {FOLLOW}")

api = create_api()

# Returns the 20 most recent statuses posted from the user specified.
tweets = api.user_timeline(HANDLER)
for tweet in tweets:
    try:
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
        print()
    
    except KeyboardInterrupt:
        logger.info("Bot has been interrupted.😵")
        break