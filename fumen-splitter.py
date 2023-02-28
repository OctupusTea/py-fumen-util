# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder

def fumen_splitter(fumen_codes):
    output = []
    for code in fumen_codes:
        input_pages = decoder.decode(code)
        for page in input_pages:
            if input_pages[0].flags.colorize:
                page.flags.colorize = True
            output.append(encoder.encode([page]))
    return output

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in fumen_splitter(" ".join(sys.argv[1:]).split(" ")):
            print(line)
