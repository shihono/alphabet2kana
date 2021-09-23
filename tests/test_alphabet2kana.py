import pytest

from alphabet2kana.alphabet2kana import a2k


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
        ("PS5PS4ps2", "ピーエスファイブピーエスフォーピーエスツー"),
        (
            "sk8やk8sも変換。d4dj,v8・V6",
            "エスケーエイトやケーエイトエスも変換。ディーフォーディージェー,ブイエイト・ブイシックス",
        ),
    ],
)
def test_a2k_numeral(input_text, expected):
    assert a2k(input_text, numeral=True) == expected


@pytest.mark.parametrize(
    "input_text,delimiter,expected",
    [
        ("あa0b1c亜2", "/", "あエー/ゼロ/ビー/ワン/シー亜ツー"),
        ("PS5PS4ps2", "*", "ピー*エス*ファイブ*ピー*エス*フォー*ピー*エス*ツー"),
        ("1234567890", "・", "ワン・ツー・スリー・フォー・ファイブ・シックス・セブン・エイト・ナイン・ゼロ"),
        (
            "sk8やk8sも変換。d4dj,v8・V6",
            "・",
            "エス・ケー・エイトやケー・エイト・エスも変換。ディー・フォー・ディー・ジェー,ブイ・エイト・ブイ・シックス",
        ),
    ],
)
def test_a2k_numeral_delimiter(input_text, delimiter, expected):
    assert a2k(input_text, delimiter=delimiter, numeral=True) == expected
