# alphabet2kana

Convert English alphabet to Katakana

アルファベットの日本語表記は [Unidic](https://unidic.ninjal.ac.jp/) 
と [英語アルファベット - Wikipedia](https://ja.wikipedia.org/wiki/%E8%8B%B1%E8%AA%9E%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88) を参考にしています。

特に、`Z` は `ゼット` 表記です。

## Installation

```bash
pip install alphabet2kana
```

## Usage

```python
from alphabet2kana import a2k

a2k("ABC")
# "エービーシー"

a2k("Alphabetと日本語")
# "エーエルピーエイチエービーイーティーと日本語"

a2k("Alphabetと日本語", delimiter="・")
# "エー・エル・ピー・エイチ・エー・ビー・イー・ティーと日本語"

a2k('k8s', delimiter='・', numeral=True)
# "ケー・エイト・エス"
``` 

半角にのみ対応しています。
全角アルファベットは [mojimoji](https://github.com/studio-ousia/mojimoji) や [jaconv](https://github.com/ikegami-yukino/jaconv) 
などで半角に変換してください。

Only supported with half-width characters.