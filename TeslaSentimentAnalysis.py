import praw 
import json 
 
# Reddit API credentials 
client_id = '-zQ-CysznINz-oAC0VNAYg' 
client_secret = '_hEYwaTgYoXqBMTJcIr-vtKZ430l4w' 
user_agent = 'script:TeslaSentimentApp:1.0 (by /u/Motor-Illustrator888)'

 
# Initialize Reddit API 
reddit = praw.Reddit(client_id=client_id, 
                     client_secret=client_secret, 
                     user_agent=user_agent) 
 
# Define search parameters 
query = 'Tesla'
subreddits = ['cars', 'technology', 'teslamotors', 'stocks', 'investing', 'electricvehicles']
max_posts = 150
posts = []  

# Collect submissions
for subreddit_name in subreddits:
    for submission in reddit.subreddit(subreddit_name).search(query, sort='new', limit=max_posts):
        posts.append({
            'title': submission.title,
            'selftext': submission.selftext,
            'author': str(submission.author),
            'created_utc': submission.created_utc,
            'score': submission.score,
            'url': submission.url,
            'num_comments': submission.num_comments,
            'subreddit': str(submission.subreddit),
            'id': submission.id
        })

 
# Save data to a JSON file 
with open('reddit_posts.json', 'w') as f: 
    json.dump(posts, f, indent=2)
