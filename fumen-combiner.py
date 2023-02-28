# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder

def fumen_combiner(fumen_codes):
    combined = []
    for code in fumen_codes:
        combined += decoder.decode(code)
    return encoder.encode(combined)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(fumen_combiner(" ".join(sys.argv[1:]).split(" ")))
