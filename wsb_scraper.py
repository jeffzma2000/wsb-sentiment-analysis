import praw
import pandas as pd
import os

reddit = praw.Reddit('bot1', user_agent='jeffzma2000 wsb sentiment analysis script')
wsb = reddit.subreddit('wallstreetbets')

def scrape_for(symbol, limit, subreddit=wsb):

    result = {}

    for submission in wsb.hot(limit=limit):
        for word in submission.title.split():
            if word.lower() == symbol.lower():
                result['title'] = submission.title
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    print(comment.body)
                break

    return result

print(scrape_for('tsla', 30))