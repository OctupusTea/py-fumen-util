# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder
from py_fumen.page import Page, Flags

def fumen_locker(fumen_codes):
    locked_fumen = []
    for code in fumen_codes:
        input_pages = decoder.decode(code)
        input_pages.append(Page(flags=Flags(lock=True)))
        locked_fumen.append(encoder.encode(input_pages))
    return locked_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in fumen_locker(" ".join(sys.argv[1:]).split(" ")):
            print(line)
