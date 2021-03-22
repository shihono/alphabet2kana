from itertools import groupby
from .char_table import A2L_TABLE, ALPHABET_ALL


def _convert(text):
    return text.translate(A2L_TABLE)


def a2k(text, delimiter=""):
    """Convert English alphabet to Katakana

    Parameters
    ----------
    text : str
        Half-width English alphabet string.
    delimiter : str
        Katakana delimiter
    Returns
    -------
    str
        convert string

    Examples
    --------
    >>> a2k('ABC')
    'エービーシー'
    >>> a2k('ABCです', delimiter='・')
    'エー・ビー・シーです'
    """
    if not delimiter:
        return _convert(text)
    res = []
    for k, v in groupby(text, lambda x: x in ALPHABET_ALL):
        t = list(v)
        if k:
            res.append(_convert(delimiter.join(t)))
        else:
            res.extend(t)
    return "".join(res)
