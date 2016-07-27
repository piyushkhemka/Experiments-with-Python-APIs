import praw
import datetime
import csv
import time

myfile = open('reddittester.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

agent = 'subreddit_analyser/1.0 by /u/utopianidot'
r = praw.Reddit(user_agent=agent)
subreddit = r.get_subreddit('asoiaf')

DONE = False

lowerTime = 1437868800
upperTime = 1469571424
#lowerTime= upperTime - (60*60*24*365)


counter = 0
while not DONE:
    try:
        print ("trying")
        query = 'timestamp:%d..%d' % (lowerTime, upperTime)
        print (query)
        submissions = list(r.search(query, subreddit='asoiaf',
         sort='new', limit=1000, syntax='cloudsearch'))

        # for x in submissions:
        #     print (x)
        print (len(submissions))

        if (len(submissions) == 0):
            print ("zero")
            break

        for submission in submissions:
            print ("looping")
            # print ((submission) + readable_date(submission.created_utc))
            # submissions.append(submission)
            # wr.writerow([submission])
            if submission.created_utc > upperTime:
                continue

            if submission.created_utc <= lowerTime:
                DONE = True
                break

            if submission.created_utc <= upperTime:
                # print (submission + readable_date(submission.created_utc))
                print (submission)
                # submissions.append(submission)
                wr.writerow([submission])

        submissions.sort(key=lambda x: x.created_utc)
        upperTime = submissions[0].created_utc - 0.1

    except Exception as e:
        print (e)
        print ('Going to sleep for 30 seconds...\n')
        time.sleep(30)
        submissions.sort(key=lambda x: x.created_utc)
        upperTime = submissions[0].created_utc - 0.001
        continue

    finally:
        myfile.close()


def readable_date(timestamp):
    time = datetime.datetime.utcfromtimestamp(timestamp)
    readable_time = datetime.datetime.strftime(time, "%b %d %Y %H:%M:%S")
    return readable_time

# submissions = r.get_subreddit('asoiaf').get_new(limit=10)
# for x in submissions:
#     print (str(x),str(x.author),str(x.score),str(x.gilded),str(x.created_utc))


# class download_data():
#
#     def __init__(self, subreddit_name, csv_name):
#         self.subreddit_name = subreddit_name
#         self.csv_name = csv_name
#
#     def
