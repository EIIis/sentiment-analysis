# PLEASE READ THE README.MD FILE FOR FURTHER NOTICES ABOUT THIS PROJECT. IT'S NOT FULLY COMPLETE
# AND I INTENTED TO ADD MORE DATA VISUALIZATION FEATURES IN THE FUTURE

# Importation of Libraries
import re
import tweepy
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt


# Twitter Authentication

# Must use your own personal Twitter developer keys. For testing purposes I used a variable. Id
# Recommend using an enviormental variable or using a file to import your keys in rather than typing
# your own personal data keys.
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

# Receiving 100 Tweets from user, you could chnage the number of tweets you pull by changing count
# For twitterUser, you must use the Twitter users user's handle. For e
twitterUser = input("Please enter the user's twitter handle, without the @: ")
posts = api.user_timeline(screen_name = twitterUser, count = 100, lang = "en", tweet_mode = "extended")

# Creating datafram w/ a column called 'Tweets'
dataframe = pd.DataFrame([tweets.full_text for tweets in posts], columns=["Tweets"])

# Cleaning up text (eg: #'s, @'s, image/GIF links)
def cleanTweet(text):
  text = re.sub(r"@[A-za-z0-9]+", "", text) #Removes @
  text = re.sub(r"#", "", text) # Removes #
  text = re.sub(r"RT[\s]+", "", text) #Removes retweets
  text = re.sub(r"https?:\/\/\S+", "", text) # Removes Image/GIF links
  
  return text

# Creating table of 'cleaned' tweets
dataframe["Tweets"] = dataframe["Tweets"].apply(cleanTweet)

# Determining the subjectivity of a tweet
def subjectivity(text):
  return TextBlob(text).sentiment.subjectivity

# Determining the polarity of a tweet
def polarity(text):
  return TextBlob(text).sentiment.polarity

# Creating two new columns to include subjectivity and polarity
dataframe["Subjectivity"] = dataframe["Tweets"].apply(subjectivity)
dataframe["Polarity"] = dataframe["Tweets"].apply(polarity)

# Determining if a tweet's tone is positive, negative, or neutral
def analysis(polarity):
  if polarity > 0:
    return "Positive"
  elif polarity < 0:
    return "Negative"
  else:
    return "Neutral"

dataframe['Analysis'] = dataframe['Polarity'].apply(analysis)


# Creating a visualization of the sentimental analysis of the user's tweets
dataframe["Analysis"].value_counts()

plt.title("Sentiment Analysis of Twitter user @" + twitterUser)
plt.xlabel("Sentiment")
plt.ylabel("Values")
dataframe["Analysis"].value_counts().plot(kind = "pie")
plt.show()