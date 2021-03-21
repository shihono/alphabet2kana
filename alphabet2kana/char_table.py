ALPHABET_U = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
ALPHABET_L = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
ALPHABET_ALL = ALPHABET_U + ALPHABET_L
LFORM = [
    'エー', 'ビー', 'シー', 'ディー', 'イー', 'エフ', 'ジー', 'エイチ', 'アイ', 'ジェー', 'ケー', 'エル', 'エム', 'エヌ',
    'オー', 'ピー', 'キュー', 'アール', 'エス', 'ティー', 'ユー', 'ブイ', 'ダブリュー', 'エックス', 'ワイ', 'ゼット'
]

A2L = dict(zip(ALPHABET_U, LFORM))
A2L.update(dict(zip(ALPHABET_L, LFORM)))
A2L_TABLE = str.maketrans(A2L)
