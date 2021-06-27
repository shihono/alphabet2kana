import pytest
from alphabet2kana import a2k, num2k


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


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("1234567890", "ワンツースリーフォーファイブシックスセブンエイトナインゼロ"),
        ("あa0b1c亜2", "あaゼロbワンc亜ツー"),
        ("404 not found", "フォーゼロフォー not found"),
    ],
)
def test_num2k(input_text, expected):
    assert num2k(input_text) == expected


@pytest.mark.parametrize(
    "input_text,delimiter,expected",
    [
        ("1234567890", "・", "ワン・ツー・スリー・フォー・ファイブ・シックス・セブン・エイト・ナイン・ゼロ"),
        ("あa0b1c亜2", "/", "あaゼロbワンc亜ツー"),
        ("0ロ69_ン_abc_", "_", "ゼロロシックス_ナイン_ン_abc_"),
    ],
)
def test_num2k_delimiter(input_text, delimiter, expected):
    assert num2k(input_text, delimiter=delimiter) == expected


@pytest.mark.parametrize(
    "input_text,delimiter,expected",
    [
        ("PS5PS4ps2", None, "ピーエスファイブピーエスフォーピーエスツー"),
        (
            "sk8やk8sも変換。d4dj,v8・V6",
            "・",
            "エス・ケーエイトやケーエイトエスも変換。ディーフォーディー・ジェー,ブイエイト・ブイシックス",
        ),
    ],
)
def test_a2k_num2k_combination(input_text, delimiter, expected):
    assert a2k(num2k(input_text, delimiter=delimiter), delimiter=delimiter) == expected
    assert num2k(a2k(input_text, delimiter=delimiter), delimiter=delimiter) == expected
