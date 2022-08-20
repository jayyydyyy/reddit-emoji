from mysql.connector.errors import DatabaseError
from app.reddit_classes import *
import pytest

# from db.mysql_repo import MySQL_Repo
from db.mysql_alchemy_repo import MySQL_Alchemy_Repo


#mysql_repo = MySQL_Repo()
    
# try:
#     mysql_repo.initialize()
# except DatabaseError:
#     pass

# mysql_repo.execute(
#     'USE reddit;'
# )


# def test_post_insert_access():
#     r = RedditPost(id='a0', time=0, title='Title', text='', subreddit = 'subreddit', comments=None)
    
#     mysql_repo.execute(
#         'INSERT INTO post '
#         '(id, title, text_field, subreddit, time_posted) '
#         'VALUES '
#         '(\"{id}\", \"{title}\", \"{text_field}\", \"{subreddit}\", {time_posted})'
#         ';'.format(id=r.id, title=r.title, text_field=r.text, subreddit=r.subreddit, time_posted=r.time)
#     )
#     res = mysql_repo.execute(
#         'SELECT * FROM post;'
#     )

#     assert len(res) == 1
#     assert 'a0' in res[0]


mysql_alchemy_repo = MySQL_Alchemy_Repo(local=True)
    

def test_post_insert_access():
    r = RedditPost(id='a0', time=0, title='Title', text='', subreddit = 'subreddit', comments=None)
    
    mysql_alchemy_repo.db.execute(
        "DELETE FROM post WHERE id = 'a0';"
    )

    mysql_alchemy_repo.db.execute(
        'INSERT INTO post '
        '(id, title, text_field, subreddit, time_posted) '
        'VALUES '
        '(\"{id}\", \"{title}\", \"{text_field}\", \"{subreddit}\", {time_posted})'
        ';'.format(id=r.id, title=r.title, text_field=r.text, subreddit=r.subreddit, time_posted=r.time)
    )
    res = mysql_alchemy_repo.db.execute(
        'SELECT * FROM post;'
    )

    results = [row for row in res]

    assert ('a0', 'Title', '', 'subreddit', 0) == results[0]