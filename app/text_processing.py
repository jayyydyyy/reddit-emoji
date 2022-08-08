from abc import ABC
from collections import defaultdict

from typing import List

import emoji


class TextHandler(ABC):
    @staticmethod
    def sum_dicts(dict_list:List[defaultdict]) -> defaultdict:
        res = defaultdict(int)
        key_set = {k for d in dict_list for k in d}
        for k in key_set:
            res[k] = sum([d[k] for d in dict_list])
        return res

class EmojiHandler(TextHandler):
    @staticmethod
    def get_emoji_count_dict(text):
        res = defaultdict(int)
        emojis = emoji.emoji_list(text)
        for d in emojis:
            res[d['emoji']] += 1
        return res
