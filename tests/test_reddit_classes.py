from app.reddit_classes import *
import pytest

def test_post_construction():
    r = RedditPost(id='a0', time=0, title='Title', text='', subreddit = 'subreddit', comments=None)
    assert r.id == 'a0'
    assert r.time == 0
    assert r.title == 'Title'
    assert r.text == ''
    assert r.subreddit == 'subreddit'
    assert r.comments == []

def test_post_to_dict():
    r = RedditPost(id='a0', time=0, title='Title', text='', subreddit = 'subreddit', comments=None)
    rd = r.to_dict()

    assert rd.get('id') == 'a0'
    assert rd.get('time') == 0
    assert rd.get('title') == 'Title'
    assert rd.get('text') == '' 
    assert rd.get('subreddit') == 'subreddit'
    assert rd.get('comments') == []

def test_comment_construction():
    r = RedditComment(id='a0', time=0, text='', subreddit = 'subreddit', comments=None)
    assert r.id == 'a0'
    assert r.time == 0
    assert r.text == ''
    assert r.subreddit == 'subreddit'
    assert r.comments == []

def test_comment_to_dict():
    r = RedditComment(id='a0', time=0, text='', subreddit = 'subreddit', comments=None)
    rd = r.to_dict()

    assert rd.get('id') == 'a0'
    assert rd.get('time') == 0
    assert rd.get('text') == ''
    assert rd.get('subreddit') == 'subreddit'
    assert rd.get('comments') == []