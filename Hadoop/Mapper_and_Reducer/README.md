Mapper and Reducer – Tesla Sentiment Analysis 

This folder contains the Mapper and Reducer scripts used in the Hadoop Streaming phase of the Tesla Sentiment Analysis project.

Overview
- mapperTeslaAnalysis.py - Processes Reddit JSON posts:
  - Reads each post line by line.
  - Extracts fields: post_id, author, created_utc, subreddit, score, num_comments, title, selftext.
  - Filters out low-engagement posts (score < 2 and comments < 2).
  - Cleans and normalizes text:
    - Lowercasing
    - Removing URLs, digits, punctuation
    - Removing stopwords
  - Outputs tab-separated values:  
    
    post_id    author    created_utc    subreddit    score    num_comments    cleaned_text
    

- reducerTeslaAnalysis.py:
  - Forwards the mapper’s output line by line without aggregation.
