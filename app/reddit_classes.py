from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

@dataclass
class RedditText(ABC):
    id:str
    text:str
    time:int
    comments:Iterable
    
    def __post_init__(self):
        if self.comments == None:
            self.comments = []

    @abstractmethod
    def serialize(self) -> dict:
        """Converts RedditText object to a dictionary for easy JSON serialization"""
        raise NotImplementedError


@dataclass
class RedditComment(RedditText):

    def serialize(self) -> dict:
        return {'id':self.id, 'text':self.text, 'time':self.time, 'comments':self.comments}

@dataclass
class RedditPost(RedditText):
    title:str

    def serialize(self) -> dict:
        return {'id':self.id, 'text':self.text, 'time':self.time, 'title':self.title, 'comments':self.comments}

