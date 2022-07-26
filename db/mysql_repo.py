import mysql.connector
from app.reddit_classes import *
from db.repo import Repo

class MySQL_Repo(Repo):
    def __init__(self) -> None:
        config = {
            'user' : 'root',
            'password': 'root',
            'host':'db',
            #'host' : 'mysql',
            #'host' : 'localhost',
            'port' : '3306',
            #'port' : '32000',
        }
        self.connection:mysql.connector.MySQLConnection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def execute(self, sql:str):
        self.cursor.execute(sql)
        return list(self.cursor)
    
    def initialize(self):
        init_sql = ''
        with open('./data/init.sql') as f:
            init_sql = f.read()
            init_sql = init_sql.replace('\n','')
        
        statements = init_sql.split(';')
        for statement in statements:
            if len(statement) > 0:
                self.cursor.execute(statement+';')

        return list(self.cursor)

    def insert_post(self, r:RedditPost):
        self.execute(
            'INSERT INTO post '
            '(id, title, text_field, subreddit, time_posted) '
            'VALUES '
            '(\"{id}\", \"{title}\", \"{text_field}\", \"{subreddit}\", {time_posted})'
            ';'.format(id=r.id, title=r.title, text_field=r.text, subreddit=r.subreddit, time_posted=r.time)
        )
    def insert_comment(self, r:RedditComment):
        self.execute(
            'INSERT INTO comment '
            '(id, post_id, text_field, subreddit, time_posted) '
            'VALUES '
            '(\"{id}\", \"{post_id}\", \"{text_field}\", \"{subreddit}\", {time_posted})'
            ';'.format(id=r.id, post_id=r.post_id, text_field=r.text, subreddit=r.subreddit, time_posted=r.time)
        )

    def batch_insert_post(self, posts:Iterable[RedditPost]):
        self.execute(
            'USE reddit;'
        )
        
        query_start = (
            'INSERT INTO post '
            '(id, title, text_field, subreddit, time_posted) '
            'VALUES '
        )
        
        vals = ', '.join(
            [
            f"('{r.id}', 'title_placeholder', 'text_placeholder', '{r.subreddit}', {r.time})"
            for r in posts
            ]
        )
        
        self.execute(query_start+vals+';')

    def batch_insert_comment(self, comments:Iterable[RedditComment]):
        self.execute(
            'USE reddit;'
        )
        
        query_start = 'INSERT INTO comment ' \
            + '(id, post_id, text_field, subreddit, time_posted) '\
            + 'VALUES '
        vals = ', '.join(
            [
            f"('{r.id}', '{r.post_id}', 'text_placeholder', '{r.subreddit}', {r.time})"
            for r in comments
            ]
        )

        self.execute(query_start+vals+';')