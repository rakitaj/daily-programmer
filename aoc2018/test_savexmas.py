import pytest
from savexmas import common_letters


@pytest.mark.parametrize("word1, word2, expected", [
    ("abcde", "abcde", "abcde"),
    ("abcd", "abzd", "abd"),
    ("qabc", "rabc", "abc")
])
def test_common_letters(word1, word2, expected):
    result = common_letters(word1, word2)
    assert result == expected
