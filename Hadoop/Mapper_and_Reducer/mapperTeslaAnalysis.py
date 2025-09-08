#!/usr/bin/env python3
import sys
import json
import re

"""
Mapper script for Hadoop Streaming:
- Reads Reddit post JSON lines from stdin
- Filters out low-engagement posts
- Cleans and normalizes text
- Outputs tab-separated values: post_id, author, created_utc, subreddit, score, num_comments, cleaned_text
"""

# Define stopwords
stopwords =stopwords = {
    "i", "me", "my", "myself", "we", "our", "you", "your", "yours", "he", "him", "she", "her", "it", "they", "them",
    "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do",
    "does", "did", "doing", "a", "an", "the", "and", "or", "but", "if", "because", "as", "until", "while", "of", "at",
    "by", "for", "with", "about", "against", "between", "into", "through", "before", "after", "on", "off", "over",
    "under", "again", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
    "very", "can", "will", "just", "don", "should", "now", "ve", "re", "ll", "m", "d", "s", "t", "im", "ive", "youre",
    "theyre", "said", "get", "got", "thing", "things", "someone", "everyone", "even", "also", "still", "maybe"
}

# Function to clean and normalize text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)       # Remove URLs
    text = re.sub(r"\d+", "", text)           # Remove digits
    text = re.sub(r"[^\w\s]", "", text)       # Remove punctuation/emojis
    text = re.sub(r"\s+", " ", text).strip()  # Normalize whitespace
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

# Process each JSON line
for line in sys.stdin:
    try:
        data = json.loads(line)

        post_id = str(data.get("id", "")).strip()
        author = str(data.get("author", "")).strip()
        created_utc = str(data.get("created_utc", "")).strip()
        subreddit = str(data.get("subreddit", "")).strip()
        score = int(data.get("score", 0))
        num_comments = int(data.get("num_comments", 0))
        title = str(data.get("title", ""))
        selftext = str(data.get("selftext", ""))

        # Skip low-engagement or empty posts
        if score < 2 and num_comments < 2:
            continue

        combined_text = f"{title} {selftext}".strip()
        if not combined_text:
            continue

        cleaned = clean_text(combined_text)

        print(f"{post_id}\t{author}\t{created_utc}\t{subreddit}\t{score}\t{num_comments}\t{cleaned}")

    except Exception as e:
        continue  # Or log to stderr if needed: print(f"Error: {e}", file=sys.stderr)
