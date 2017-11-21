import praw
import re

from datetime import datetime, timedelta

keywords = {'stila': [(0,10),set(),{'eyeliner'}]}

def search(text,before,after,key):
    word = r"\W*([\w]+)"
    res = re.search(r'{}\W*{}{}'.format(word*before,key,word*after), text)
    if res:
        groups = res.group().split()
        return set(groups[:before]),set(groups[before:])
    else:
        return set(), set()

def parse_body(body):
    for key, item in keywords.items():
        before = item[0][0]
        after = item[0][1]
        before, after = search(body.lower(), before, after, key)
        keywords_af = item[2]
        if keywords_af:
            for word in after:
                if word in keywords_af:
                    return True
        return False

def check_recents():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('makeupexchange')

    recents = []
    for submission in subreddit.new(limit=15):
        time = datetime.fromtimestamp(submission.created_utc)
        delta = datetime.now()-time
        if delta < timedelta(minutes=60):
            recents.append(submission)

    potential = []
    for submission in recents:
        url = submission.url
        body = submission.selftext
        if parse_body(body):
            potential.append(url)
        comments = submission.comments.list()

def notify():
    pass

check_recents()
