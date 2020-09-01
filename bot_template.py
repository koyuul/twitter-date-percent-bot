#!/usr/bin/python3.7
import tweepy
import datetime

#insert your own keys below
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

starttime = datetime.datetime(2017, 8, 17, 0, 0, 0, 0) #aug 17 2017
endtime = datetime.datetime(2021, 6, 16, 0, 0, 0, 0) #june 5 21
remains = endtime - datetime.datetime.now() #days from now on
total = endtime - starttime #total days
truepercent=1-(remains/total)
roundedpercent=round(truepercent, 2)
printpercent=roundedpercent*100
comparepercent=roundedpercent
int (printpercent)
_delta = truepercent-roundedpercent


if((_delta<.00057) and (_delta>0)): #date matches
    api.update_status("The Class of 2021 is "+ str(int(printpercent)) + "% finished with high school!")
    truepercent=1-(remains/total)
    roundedpercent=round(truepercent, 2)

else:
    print("No change.")
    print(truepercent)
    print(roundedpercent)
