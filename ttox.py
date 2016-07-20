"""
Searches for some keyword in twitter and saves it to a csv

"""


import sys
import csv
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from local_config import *
# import io


# TODO
#
# fix weird characters appearing in csv
# extract time in csv as well along with tweet
# tweet.created_at
# results.created_at

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(app_token, app_token_secret)
    twitter_api = tweepy.API(auth,retry_delay=5,retry_errors=set([401, 404, 500, 503]),
         wait_on_rate_limit=True )
    myfile = open('teststream.csv', 'w')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    search_results = tweepy.Cursor(twitter_api.search, q="@iamsrk").items(5)
    try:
        for results in search_results:
        # for results in tweepy.Cursor(twitter_api.search, q="@iamsrk").items(5):
            print(results.text)
            item = (results.text).encode('utf-8').strip()
            wr.writerow([item])
        #end of for loop
    #try block end

    except tweepy.error.TweepError:
        time.sleep(60*20)
        #end of except
    #end of except

    except tweepy.TweepError:
        time.sleep(60*20)

    except IOError:
        time.sleep(60*5)

    except StopIteration:
        time.sleep(60*60)
        #do nothing

    finally:
        myfile.close()
