from app.text_processing import EmojiHandler

import pytest

def test_emoji_count():
    texts = ['This is a test sentence 😃😃😃', 'Diversity in emoji! 💕💘💜', 'And some more 😃💯💯']
    emoji_dicts = [EmojiHandler.get_emoji_count_dict(text) for text in texts]
    total_counts = EmojiHandler.sum_dicts(emoji_dicts)

    assert len(total_counts) == 5
    assert total_counts['😃'] == 4
    assert total_counts['💜'] == 1
    assert total_counts['💘'] == 1
    assert total_counts['💕'] == 1
    assert total_counts['💯'] == 2
