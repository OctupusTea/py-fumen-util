# -*- coding: utf-8 -*-

import sys

from py_fumen_py import *

def grayout_fumen(fumen_codes):
    grayed_fumen = []
    for code in fumen_codes:
        input_pages = decode(code)
        if input_pages[-1].field:
            for line in input_pages[-1].field[:]:
                for i, mino in enumerate(line):
                    if mino.is_colored():
                        line[i] = Mino.X
        grayed_fumen.append(encode(input_pages))
    return grayed_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in grayout_fumen(' '.join(sys.argv[1:]).split()):
            print(line)

