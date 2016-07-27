import praw
import datetime

agent = 'subreddit_analyser/1.0 by /u/utopianidot'
r = praw.Reddit(user_agent=agent)
t = r.get_subreddit('asoiaf')
print (t.created_utc)
time = datetime.datetime.utcfromtimestamp(t.created_utc)
print(time)
better = datetime.datetime.strftime(time, "%b %d %Y %H:%M:%S")
print(better)
# submissions = r.get_subreddit('asoiaf').get_top_from_all(limit=10)
# for x in submissions:
#     print (str(x),str(x.author),str(x.score),str(x.gilded))
