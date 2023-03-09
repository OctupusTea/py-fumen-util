# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder

def fumen_combiner(fumen_codes):
    combined_fumen = []
    for code in fumen_codes:
        combined_fumen += decoder.decode(code)
    return encoder.encode(combined_fumen)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(fumen_combiner(" ".join(sys.argv[1:]).split(" ")))
