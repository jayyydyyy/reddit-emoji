from abc import ABC
from dataclasses import dataclass, asdict
from typing import Iterable

@dataclass
class RedditText(ABC):
    id:str
    text:str
    time:int
    subreddit:str

    def to_dict(self) -> dict:
        """Wrapper for dataclass.asdict, for convenient JSON serialization"""
        return asdict(self)        


@dataclass
class RedditComment(RedditText):
    ...

@dataclass
class RedditPost(RedditText):
    title:str
    comments:Iterable[RedditComment]

    def __post_init__(self):
        if self.comments == None:
            self.comments = []