
import json

import praw

def main():
	with open("private/creds.json") as f:
		cj = json.load(f)

	creds = cj["credentials"]
	reddit = praw.Reddit(
		client_id = creds["id"],
		client_secret = creds["secret"],
		user_agent = creds["appname"],
		username = creds["username"],
		password = creds["password"]
	)

	subreddit = reddit.subreddit('Cricket')
	top_posts = subreddit.top(limit=10)
	for index, post in enumerate(top_posts):
		print(f"{index}. {post.title} [{post.shortlink}]")

if __name__ == '__main__':
	main()
