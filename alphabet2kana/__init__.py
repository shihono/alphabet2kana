from sys import version

from . import alphabet2kana

try:
    import importlib_metadata
except:
    import importlib.metadata as importlib_metadata

__all__ = ["a2k"]
__version__ = importlib_metadata.version(__name__)

a2k = alphabet2kana.a2k
