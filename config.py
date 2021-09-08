import os
import tweepy
import logging
from dotenv import load_dotenv

logger = logging.getLogger()
load_dotenv()

def create_api():
    """
    Returns tweepy api object if successfully authenticated else an exception will be raised.
    """
    
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    consumer_key = os.environ.get("CONSUMER_KEY")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # Authenticating credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    # Verify the supplied user credentials are valid.
    if api.verify_credentials():
        logger.info("API created!✅")
        return api
    else:
        logger.error("Error creating API.❌")
        raise ValueError("Invalid credentials!")
