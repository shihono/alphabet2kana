# alphabet2kana

## Usage

```python
from alphabet2kana import a2k
a2k('ABC')
# 'エービーシー'

a2k('Alphabetと日本語')
# 'エーエルピーエイチエービーイーティーと日本語'
a2k('Alphabetと日本語', delimiter="・")
# 'エー・エル・ピー・エイチ・エー・ビー・イー・ティーと日本語'
``` 