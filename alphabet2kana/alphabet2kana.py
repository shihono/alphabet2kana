from itertools import groupby
from .char_table import A2K_TABLE, ALPHABET_ALL, N2K_TABLE, NUMERALS


def _convert(text, conv_table):
    return text.translate(conv_table)


def convert(text, delimiter, conv_table, target_words):
    """

    Parameters
    ----------
    text :str
    delimiter : str
    conv_table : dict
        convert table
    target_words : list
        convert words list
    Returns
    -------
    str
        convert string
    """
    if not delimiter:
        return _convert(text, conv_table)
    res = []
    for k, v in groupby(text, lambda x: x in target_words):
        t = list(v)
        if k:
            res.append(_convert(delimiter.join(t), conv_table))
        else:
            res.extend(t)
    return "".join(res)


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
    return convert(text, delimiter, A2K_TABLE, ALPHABET_ALL)


def num2k(text, delimiter=""):
    """Convert numerical digits to Katakana

    Parameters
    ----------
    text : str
        Half-width digits string.
    delimiter : str
        Katakana delimiter

    Returns
    -------
    str
        convert string

    Examples
    --------
    >>> num2k('123')
    'ワンツースリー'
    >>> a2k('123です', delimiter='・')
    'ワン・ツー・スリーです'
    """
    return convert(text, delimiter, N2K_TABLE, NUMERALS)
