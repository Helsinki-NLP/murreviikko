
# import
import tweepy as tw
import pandas as pd
import numpy as np

# your Twitter API key and API secret
my_api_key = YOURKEY
my_api_secret = YOURSECRET
# authenticate
auth = tw.AppAuthHandler(my_api_key, my_api_secret)

bearer_token=YOURBEARERTOKEN
access_token=YOURACCESSTOKEN
access_token_secret=YOURACCESSTOKENSECRET

client = tw.Client(bearer_token=bearer_token, consumer_key=my_api_key, consumer_secret=my_api_secret, access_token=access_token, access_token_secret=access_token_secret)

# set up query
search_query = "#murreviikko OR murreviikko -is:retweet"

# get tweets from the API

tweets20 = client.search_all_tweets(
              query=search_query,
              tweet_fields=['id', 'geo', 'text'],
              expansions=['author_id', 'geo.place_id'],
              user_fields=['name', 'username', 'location'],
              place_fields=['place_type','geo', 'full_name'],
              start_time="2020-09-01T00:00:00.00Z",
              end_time="2020-11-01T00:00:00.00Z",
              max_results=500)

tweets21 = client.search_all_tweets(
              query=search_query,
              tweet_fields=['id', 'geo', 'text'],
              expansions=['author_id', 'geo.place_id'],
              user_fields=['name', 'username', 'location'],
              place_fields=['place_type','geo', 'full_name'],
              start_time="2021-09-01T00:00:00.00Z",
              end_time="2021-11-01T00:00:00.00Z",
              max_results=500)

tweets22 = client.search_all_tweets(
              query=search_query,
              tweet_fields=['id', 'geo', 'text'],
              expansions=['author_id', 'geo.place_id'],
              user_fields=['name', 'username', 'location'],
              place_fields=['place_type','geo', 'full_name'],
              start_time="2022-09-01T00:00:00.00Z",
              end_time="2022-10-26T00:00:00.00Z",
              max_results=500)
              
# create a list of records without geo information
tweet_info_ls = []

# iterate over each tweet and corresponding user details
for tweet, user in zip(tweets20.data, tweets20.includes['users']):
    tweet_info = {
        'text': tweet.text,
        'id': tweet.id,
        'geo': tweet.geo,
        'name': user.name,
        'username': user.username,
        'location': user.location,
    }
    tweet_info_ls.append(tweet_info)

# iterate over each tweet and corresponding user details
for tweet, user in zip(tweets21.data, tweets21.includes['users']):
    tweet_info = {
        'text': tweet.text,
        'id': tweet.id,
        'geo': tweet.geo,
        'name': user.name,
        'username': user.username,
        'location': user.location,
    }
    tweet_info_ls.append(tweet_info)

# iterate over each tweet and corresponding user details
for tweet, user in zip(tweets22.data, tweets22.includes['users']):
    tweet_info = {
        'text': tweet.text,
        'id': tweet.id,
        'geo': tweet.geo,
        'name': user.name,
        'username': user.username,
        'location': user.location,
    }
    tweet_info_ls.append(tweet_info)
    
# create dataframe from the extracted records
tweets_df = pd.DataFrame(tweet_info_ls)
# There are retweets which we did not want, let's get rid
tweets_df = tweets_df[tweets_df["text"].str.contains("RT")==False].reset_index(drop=True)
# write to csv
tweets_df.to_csv('murreviikko_tweets.csv')
