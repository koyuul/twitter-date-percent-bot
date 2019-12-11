#!/usr/bin/python3.7
import tweepy
import datetime

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

starttime = datetime.datetime(2016, 8, 17, 0, 0, 0, 0) #aug 17 2017 replace date with whatever you want (year, month, date, specific time in day)
endtime = datetime.datetime(2021, 6, 4, 0, 0, 0, 0) #june 4 21 (year, month, date, specific time in day)
remains = endtime - datetime.datetime.now() #days from now on
total = endtime - starttime #total days
truepercent=1-(remains/total)
roundedpercent=round(truepercent, 2)
printpercent=roundedpercent*100
comparepercent=roundedpercent
int (printpercent)
_delta = truepercent-roundedpercent


if((_delta<.00057) and (_delta>0)): #date matches
    api.update_status("There is " + str(int(printpercent)) + "% left!") #tweets "(percent)% left". Change to add context to tweet
    truepercent=1-(remains/total)
    roundedpercent=round(truepercent, 2)

else:
    print("No change.")
    print(truepercent)
    print(roundedpercent)
