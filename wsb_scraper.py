import praw
import pandas as pd
import os
import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

reddit = praw.Reddit('bot1', user_agent='jeffzma2000 wsb sentiment analysis script')
wsb = reddit.subreddit('wallstreetbets')

def get_sentiment(df_col):
    vader = SentimentIntensityAnalyzer()
    scores = df_col.apply(vader.polarity_scores).tolist()
    return pd.DataFrame(scores)

def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

def scrape_for(symbol, limit=None, subreddit=wsb):

    result = []

    for submission in wsb.hot(limit=limit):
        date = get_date(submission)
        for word in submission.title.split():
            if word.lower() == symbol.lower():
                result.append((submission.title, date))
                submission.comments.replace_more(limit=0)
                for top_level_comment in submission.comments:
                    result.append((top_level_comment.body, date))
                break
    df = pd.DataFrame(result, columns=['Text', 'Date'])
    scored_df = df.join(get_sentiment(df['Text']), rsuffix='_right')
    return scored_df

# print(scrape_for('tsla', 5))