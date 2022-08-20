from app.reddit_classes import *
from sqlalchemy import create_engine
from sqlalchemy.sql import text as sql_text
from sqlalchemy.sql.expression import TextClause

from db.repo import Repo

class MySQL_Alchemy_Repo(Repo):
    def __init__(self, local=False) -> None:
        db_user, db_pass, db_host, db_port, db = (
            "root", "root", "db", "3306", "reddit"
        )

        if local: db_host, db_port = ("localhost", "32000")

        db_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db}"

        self.insert_post_start = (
            'INSERT INTO post '
            '(id, title, text_field, subreddit, time_posted) '
            'VALUES '
        )

        self.insert_comment_start = (
            'INSERT INTO comment '
            '(id, post_id, text_field, subreddit, time_posted) '
            'VALUES '
        )

        self.db = create_engine(db_string)

    def insert_post(self, r:RedditPost):
        val = f"('{r.id}', 'title_placeholder', 'text_placeholder', '{r.subreddit}', {r.time})"
        self.db.execute(self.insert_post_start+val+";")

    def insert_comment(self, r:RedditComment):
        val = f"('{r.id}', '{r.post_id}', 'text_placeholder', '{r.subreddit}', {r.time})"
        self.db.execute(self.insert_post_start+val+";")

    def batch_insert_post(self, posts:Iterable[RedditPost]):
        param_dict = {}
        fstrings = []
        for r in posts:
            param_dict[r.id+"_title"] = r.title
            param_dict[r.id+"_text"] = r.text
            fstrings.append(f"('{r.id}', :{r.id}_title, :{r.id}_text, '{r.subreddit}', {r.time})")

        vals = ', '.join(fstrings)
        query:TextClause = sql_text(self.insert_post_start+vals+';').bindparams(**param_dict)
        
        self.db.execute(query)

    def batch_insert_comment(self, comments:Iterable[RedditComment]):
        vals = ', '.join(
            [
            f"('{r.id}', '{r.post_id}', 'text_placeholder', '{r.subreddit}', {r.time})"
            for r in comments
            ]
        )

        self.db.execute(self.insert_comment_start+vals+';')
