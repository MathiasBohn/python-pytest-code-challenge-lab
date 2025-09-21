import pytest
from palindrome import longest_palindromic_substring

# Basic cases
@pytest.mark.parametrize(
    "s, expected",
    [
        ("cbbd", "bb"),
        ("racecar", "racecar"),
        ("aa", "aa"),
    ],
)
def test_basic_parametrized(s, expected):
    assert longest_palindromic_substring(s) == expected


def test_babad_allows_either_on_tie():
    result = longest_palindromic_substring("babad")
    assert result in {"bab", "aba"}


def test_two_different_characters_returns_single_char():
    result = longest_palindromic_substring("ac")
    assert result in {"a", "c"}


# Edge cases
def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_long_palindrome_falls_back_to_single_char():
    s = "abcdef"
    result = longest_palindromic_substring(s)
    assert len(result) == 1
    assert result in s


def test_case_sensitivity_A_not_equal_a():
    s = "Aa"
    result = longest_palindromic_substring(s)
    assert len(result) == 1
    assert result in {"A", "a"}


def test_max_length_constraint_example():
    s = "b" * 1000
    assert longest_palindromic_substring(s) == s


# Failure / error cases
def test_raises_typeerror_for_none_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)


def test_raises_typeerror_for_non_string_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)