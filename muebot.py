import praw

from datetime import datetime, timedelta

def parse_body(body):
    allwords = body.split()
    for

def check_recents():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('makeupexchange')

    recents = []
    for submission in subreddit.new(limit=10):
        time = datetime.fromtimestamp(submission.created_utc)
        delta = datetime.now()-time
        if delta < timedelta(minutes=60):
            recents.append(submission)

    for submission in recents:
        url = submission.url
        body = submission.selftext
        parse_body(body)
        comments = submission.comments.list()

check_recents()
