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
    myfile = open('karanjoharcsv.csv', 'w')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    # startdate="2016-06-14"
    # enddate="2016-06-21"

    # search_results = tweepy.Cursor(twitter_api.search, q="@karanjohar").items(999999999999)
    try:
        # for results in search_results:
        while 1:
            for results in tweepy.Cursor(twitter_api.search, q="@karanjohar").items(99999999999999999999):
                print(results.text)
                print (results.created_at)
                item = (results.text).encode('utf-8').strip()
                wr.writerow([item,results.created_at])
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
