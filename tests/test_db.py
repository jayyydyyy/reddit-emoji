from cgitb import reset
from app.reddit_classes import *
from db.mysql_repo import MySQL_Repo
import pytest

mysql_repo = MySQL_Repo()
mysql_repo.initialize()

def test_post_insert_access():
    r = RedditPost(id='a0', time=0, title='Title', text='', subreddit = 'subreddit', comments=None)
    
    mysql_repo.execute(
        'USE reddit;'
    )
    mysql_repo.execute(
        'INSERT INTO post '
        '(id, title, text_field, subreddit, time_posted) '
        'VALUES '
        '(\"{id}\", \"{title}\", \"{text_field}\", \"{subreddit}\", {time_posted})'
        ';'.format(id=r.id, title=r.title, text_field=r.text, subreddit=r.subreddit, time_posted=r.time)
    )
    res = mysql_repo.execute(
        'SELECT * FROM post;'
    )

    assert len(res) == 1
    assert 'a0' in res[0]