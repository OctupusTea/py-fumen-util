# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder

def remove_comment(fumen_codes):
    output_codes = []
    for code in fumen_codes:
        input_pages = decoder.decode(code)
        for page in input_pages:
            page.comment = ''
            page.flags.quiz = False
        output_codes.append(encoder.encode(input_pages))
    return output_codes

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in remove_comment(' '.join(sys.argv[1:]).split(' ')):
            print(line)
