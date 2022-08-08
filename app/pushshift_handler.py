from pmaw import PushshiftAPI
from praw import Reddit
from app.reddit_classes import *

class PushshiftHandler:
    def __init__(self, api:PushshiftAPI, reddit:Reddit=None) -> None:
        self.api = api

    def get_posts(self, after:int, before:int, subreddit:str, limit:int=1000):
        raw_posts = self.api.search_submissions(after=after, before=before, subreddit=subreddit, limit=limit)
        post_list = []
        for post in raw_posts:
            try: selftext = post['selftext']
            except KeyError: selftext = ''
            post_list.append(RedditPost(id='t3_'+post['id'], text=selftext.replace('"', ''), time=int(post['created_utc']), subreddit=subreddit, comments=[], title=post['title'].replace('"', '')))
        for post in post_list:
            post_id = post.id
            raw_comments = self.api.search_comments(link_id=post_id)
            comments = [RedditComment(id='t1_'+comment['id'],post_id=post_id, text=comment['body'].replace('"', ''), time=int(comment['created_utc']), subreddit=subreddit) for comment in raw_comments]
            post.comments = comments

        return post_list
