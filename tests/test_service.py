from collections import defaultdict
import pytest
import datetime as dt

from app.service import Services

def test_emoji_count_service():
    start = int(dt.datetime(2022,1,1).timestamp())
    end = int(dt.datetime(2022,2,1).timestamp())
    s = Services(local=True)

    res = s.get_emoji_frequency_for_range(after=start, before=end, subreddit='tokipona', limit=100)

    assert isinstance(res, defaultdict)
    assert len(res.keys()) > 0