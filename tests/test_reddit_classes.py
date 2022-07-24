from app.reddit_classes import *
import pytest

def test_post_construction():
    r = RedditPost(id='a0', time=0, title='Title', text='', comments=None)
    assert r.id == 'a0'
    assert r.time == 0
    assert r.title == 'Title'
    assert r.text == ''
    assert r.comments == []

def test_post_serialize():
    r = RedditPost(id='a0', time=0, title='Title', text='', comments=None)
    rd = r.serialize()

    assert rd.get('id') == 'a0'
    assert rd.get('time') == 0
    assert rd.get('title') == 'Title'
    assert rd.get('text') == '' 
    assert rd.get('comments') == []

def test_comment_construction():
    r = RedditComment(id='a0', time=0, text='', comments=None)
    assert r.id == 'a0'
    assert r.time == 0
    assert r.text == ''
    assert r.comments == []

def test_comment_serialize():
    r = RedditComment(id='a0', time=0, text='', comments=None)
    rd = r.serialize()

    assert rd.get('id') == 'a0'
    assert rd.get('time') == 0
    assert rd.get('text') == ''
    assert rd.get('comments') == []