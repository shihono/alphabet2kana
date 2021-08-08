from itertools import groupby
from .char_table import A2K_TABLE, AN2K_TABLE, ALPHABET_ALL, ALPHABET_NUMERAL_ALL


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
    delimiter_text = ""
    for k, v in groupby(text, lambda x: x in target_words):
        t = list(v)
        if k:
            delimiter_text += delimiter.join(t)
        else:
            delimiter_text += "".join(t)
    return "".join(_convert(delimiter_text, conv_table))


def a2k(text, delimiter=None, numeral=False):
    """Convert English alphabet to Katakana

    Parameters
    ----------
    text : str
        Half-width English alphabet string.
    delimiter : str
        Katakana delimiter
    numeral: bool
        convert Arabic numerals
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
    >>> a2k('k8s', delimiter='・', numeral=True)
    'ケー・エイト・エス'
    """
    if numeral:
        return convert(text, delimiter, AN2K_TABLE, ALPHABET_NUMERAL_ALL)
    return convert(text, delimiter, A2K_TABLE, ALPHABET_ALL)


if __name__ == "__main__":
    print(a2k("ps4", numeral=True))
