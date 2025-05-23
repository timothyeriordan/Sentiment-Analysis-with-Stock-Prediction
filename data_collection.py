import requests
import pandas as pd
import time
from datetime import datetime
import praw

#Reddit Credentials for StockTextScrapper 
reddit_app = praw.Reddit(
    client_id = 'id',
    client_secret = 'secret',
    user_agent = 'agent',
    username = 'username',
    password = 'password'
)
    
def collect_posts(subreddit=None, limit=100):
    subreddit_posts = []
    subreddit = reddit_app.subreddit(subreddit)
    
    for post in subreddit.new(limit=limit):
        subreddit_posts.append({
            'title': post.title,
            'selftext': post.selftext,
            'created_utc': datetime.utcfromtimestamp(post.created_utc),
            'score': post.score,
            'num_comments': post.num_comments,
            'id': post.id
        })
        
    return pd.DataFrame(subreddit_posts)

df_wsb = collect_posts(subreddit='wallstreetbets', limit=5)
print(df_wsb)
