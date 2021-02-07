import tweepy 
import json
from random import sample

with open("twitter-credentials.json") as json_file:
  credentials = json.load(json_file)

consumer_key = credentials["API_KEY"]
consumer_secret = credentials["API_KEY_SECRET"]

access_token = credentials["ACCESS_TOKEN"]
access_token_secret = credentials["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = credentials["user"]

exclamations = ["OUTRAGEOUS.", "UNBELIEVABLE.", "UNACCEPTABLE.", 
                "I bet their boss will be proud.",
                "They will be FIRED on the spot for sure!"]

def get_exclamation():
  return sample(exclamations, 1)[0]

def time_spent_prettier(seconds):
  m, s = divmod(seconds, 60)
  h, m = divmod(m, 60)
  return f'{h:d} hours {m:2d} minute(s) and {s:02d} seconds'
  

def tweet_status(time_spent=100, prompts=100, app="reddit"):
  if prompts % 10 != 0:
    return

  text = "My user is procrastinating. They are currently browsing {} and has spent {} on it. {}".format(app.capitalize(), time_spent_prettier(time_spent), get_exclamation())  
  api.update_status(text)

if __name__ == "__main__":
  tweet_status(1000, 100, 'reddit')