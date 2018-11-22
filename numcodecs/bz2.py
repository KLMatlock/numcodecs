# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import bz2 as _bz2
import array


import numpy as np


from numcodecs.abc import Codec
from numcodecs.compat import buffer_copy, ensure_memoryview


class BZ2(Codec):
    """Codec providing compression using bzip2 via the Python standard library.

    Parameters
    ----------
    level : int
        Compression level.

    """

    codec_id = 'bz2'

    def __init__(self, level=1):
        self.level = level

    def encode(self, buf):

        # normalise inputs
        buf = ensure_memoryview(buf)

        # do compression
        return _bz2.compress(buf, self.level)

    # noinspection PyMethodMayBeStatic
    def decode(self, buf, out=None):

        # normalise inputs
        buf = ensure_memoryview(buf)

        # do decompression
        dec = _bz2.decompress(buf)

        # handle destination - Python standard library bz2 module does not
        # support direct decompression into buffer, so we have to copy into
        # out if given
        return buffer_copy(dec, out)
