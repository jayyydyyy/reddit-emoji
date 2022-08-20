from psaw import PushshiftAPI
from praw import Reddit
from dotenv import dotenv_values
from mysql.connector.errors import DatabaseError

from db.mysql_alchemy_repo import MySQL_Alchemy_Repo

from app.pushshift_handler import PushshiftHandler
from app.text_processing import EmojiHandler

import datetime as dt

praw_vals = dotenv_values('.env')

class Services:
    def __init__(self, local=False) -> None:
        reddit = Reddit(client_id=praw_vals['CLIENT_ID'], client_secret=praw_vals['CLIENT_SECRET'], user_agent=praw_vals['USER_AGENT'])
        
        pushshift = PushshiftAPI(reddit)

        self.repo = MySQL_Alchemy_Repo(local)
        
        self.pushshift = PushshiftHandler(pushshift)

    def get_emoji_frequency_for_range(self, after, before, subreddit, limit=1000):
        posts = self.pushshift.get_posts(after, before, subreddit, limit)
        self.repo.batch_insert_post(posts)

        texts = []
        for p in posts:
            texts.append(p.title)
            if len(p.text) > 0: texts.append(p.text)

            if len(p.comments) == 0 : continue

            self.repo.batch_insert_comment(p.comments)
            for c in p.comments:
                texts.append(c.text)

        
        emoji_dicts = [EmojiHandler.get_emoji_count_dict(text) for text in texts]
        return EmojiHandler.sum_dicts(emoji_dicts)


    def date_str_to_unix(self, date:str)->int:
        y,m,d = date.split('-')
        return self.time_to_unix(year=int(y), month=int(m), day=int(d))

    @staticmethod
    def time_to_unix(year:int, month:int = 1, day:int = 1, hour:int = 0, minute:int = 0, second:int = 0, microsecond:int=0) -> int:
        return int(dt.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, microsecond=microsecond).timestamp())
