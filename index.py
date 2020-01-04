import praw
import os
import sys
import time
import json
#For more information check https://github.com/MobKill3r2006/Reddit-Auto-Post
data = json.load(open("config.json"))

password = data["config"]["password"]
client_id = data["config"]["client_id"]
client_secret = data["config"]["client_secret"]
username = data["config"]["username"]
user_agent = data["config"]["user_agent"]
subreddit = data["config"]["subreddit"]
timesec = data["config"]["time"]
title = data["config"]["title"]


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent=user_agent,
                     username=username)

sub = reddit.subreddit(subreddit)
selftext = "Reddit Body"
sub.submit(title, selftext=selftext, url=None, flair_id=None, flair_text=None, resubmit=True, send_replies=True, nsfw=False, spoiler=False, collection_id=None)
print("Successfully posted the submission on r/" + sub.display_name)
time.sleep(int(timesec, base=0))
os.execv(sys.executable, ['py index.py'] + [])
