# -*- coding: utf-8 -*-

import sys

from py_fumen_py import *

def mirror_fumen(fumen_codes):
    mirrored_fumen = []
    for code in fumen_codes:
        input_pages = decode(code)
        for i, page in enumerate(input_pages):
            page.field.mirror(mirror_color=True)
            if page.operation:
                page.operation.mirror()
        mirrored_fumen.append(encode(input_pages))
    return mirrored_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in mirror_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
