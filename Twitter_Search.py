# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:42:10 2023

@author: kalya
"""

import tweepy
import configparser
import pandas as pd
#Read config
import datetime
from tweepy import Cursor
import urllib
from sqlalchemy import create_engine
#import pyodbc

#Defining Timeline
today = datetime.date.today()
#yesterday= today - datetime.timedelta(days=7)

#Read config

config= configparser.ConfigParser()  #configparser instace

config.read('Config.ini')

api_key = config['twitter']['api_key']

api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']

access_token_secret = config['twitter']['access_token_secret']

client = tweepy.Client(bearer_token='bearer_token')

#authentication

auth = tweepy.OAuthHandler(api_key,api_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)   #instance

api = tweepy.API(auth)

keywords = 'Chewy'

columns = ['Id','Date', 'Tweet', 'Location','Retweet Count','Favorite Count']
data = []

  
            
for tweet in tweepy.Cursor(api.search_tweets, q=keywords, tweet_mode='extended').items(2000):
    if not hasattr(tweet, 'retweeted_status'):
    
        data.append([tweet.id,tweet.created_at, tweet.full_text, tweet.user.location, tweet.retweet_count, tweet.favorite_count])
        df = pd.DataFrame(data,columns=columns) 


    
    
df = pd.DataFrame(data,columns=columns)

df.to_csv('Chewy_{}.csv'.format(pd.datetime.now().strftime("%Y-%m-%d %H%M%S")))






# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\kalya\TwitterSentiment\Database1.accdb;')
# cursor = conn.cursor()
# cursor.execute('select * from tweet_info')
# for row in cursor.fetchall():
#     print (row)
