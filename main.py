# Importation of Libraries
import re
import tweepy
import pandas as pd
import numpy as np
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

# Twitter Authentication
CONSUMER_KEY = 
CONSUMER_SECRET =  
ACCESS_KEY = 
ACCESS_SECRET = 

# Create Authentication Object
auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
# Setting Access Tokens and Access Token Secret
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Create an API Object 
api = tweepy.API(auth, wait_on_rate_limit = True)

# Receiving 100 Tweets from user
# For screen_name, you must use the Twitter users user's handle. For example
posts = api.user_timeline(screen_name = "ellis_alcantara", count = 100, lang = "en", tweet_mode = "extended")