from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Iterable

@dataclass
class RedditText(ABC):
    id:str
    text:str
    time:int
    subreddit:str
    comments:Iterable # A post has an iterable of comments, and a comment has an iterable of comments which are replies

    def __post_init__(self):
        if self.comments == None:
            self.comments = []

    def to_dict(self) -> dict:
        """Wrapper for dataclass.asdict, for convenient JSON serialization"""
        return asdict(self)        


@dataclass
class RedditComment(RedditText):
    ...

@dataclass
class RedditPost(RedditText):
    title:str
