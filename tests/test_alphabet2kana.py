import pytest
from alphabet2kana import a2k


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("abcABC", "エービーシーエービーシー"),
        ("あいうえお", "あいうえお"),
        ("AZ!!", "エーゼット!!"),
    ],
)
def test_a2k(input_text, expected):
    assert a2k(input_text) == expected


@pytest.mark.parametrize(
    "input_text,delimiter,expected",
    [
        ("abc", "・", "エー・ビー・シー"),
        ("XYZ", "/", "エックス/ワイ/ゼット"),
        ("あabc亜", "・", "あエー・ビー・シー亜"),
        ("aアbc", "・", "エーアビー・シー"),
    ],
)
def test_a2k_delimiter(input_text, delimiter, expected):
    assert a2k(input_text, delimiter=delimiter) == expected
