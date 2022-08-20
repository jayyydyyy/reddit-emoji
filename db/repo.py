from app.reddit_classes import *
from abc import ABC, abstractmethod

class Repo(ABC):
    @abstractmethod
    def insert_post(self, post:RedditPost):
        raise NotImplementedError

    @abstractmethod
    def insert_comment(self, comment:RedditComment):
        raise NotImplementedError

    @abstractmethod
    def batch_insert_post(self, posts:Iterable[RedditPost]):
        raise NotImplementedError

    @abstractmethod
    def batch_insert_comment(self, comments:Iterable[RedditComment]):
        raise NotImplementedError