# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import zlib as _zlib


from .abc import Codec
from .compat import buffer_copy, PY2, ensure_memoryview
if PY2:
    from .compat import ensure_buffer


class Zlib(Codec):
    """Codec providing compression using zlib via the Python standard library.

    Parameters
    ----------
    level : int
        Compression level.

    """

    codec_id = 'zlib'

    def __init__(self, level=1):
        self.level = level

    def encode(self, buf):

        # normalise inputs
        if PY2:
            buf = ensure_buffer(buf)
        else:
            buf = ensure_memoryview(buf)

        # do compression
        return _zlib.compress(buf, self.level)

    # noinspection PyMethodMayBeStatic
    def decode(self, buf, out=None):

        # normalise inputs
        if PY2:
            buf = ensure_buffer(buf)
        else:
            buf = ensure_memoryview(buf)

        # do decompression
        dec = _zlib.decompress(buf)

        # handle destination - Python standard library zlib module does not
        # support direct decompression into buffer, so we have to copy into
        # out if given
        return buffer_copy(dec, out)
