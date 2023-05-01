# -*- coding: utf-8 -*-

import sys

from py_fumen_py import *

def grayout_all_fumen(fumen_codes):
    grayed_fumen = []
    for code in fumen_codes:
        input_pages = decode(code)
        for page in input_pages:
            if page.field:
                for line in page.field[:]:
                    for i, mino in enumerate(line):
                        if mino.is_colored():
                            line[i] = Mino.X
        grayed_fumen.append(encode(input_pages))
    return grayed_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in grayout_all_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
