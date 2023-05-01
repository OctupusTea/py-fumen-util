# -*- coding:utf-8 -*-

import sys

from py_fumen_py import *
from .fumen_combiner import fumen_combiner
from .fumen_locker import fumen_locker
from .fumen_splitter import fumen_splitter
from .glue_fumen import glue_fumen
from .grayout_all import grayout_all_fumen
from .grayout_last import grayout_fumen
from .mirror_fumen import mirror_fumen
from .remove_comment import remove_comment
from .unglue_fumen import unglue_fumen

def usage(dummy_arg=None):
    return [
        'Usage:',
        'python3 -m py_fumen_util command fumen_code [fumen_code...]',
        'Commands (case-insensitive):',
        '    Combine:   Combine multiple Fumens into one',
        '               Alias: Concat, Join',
        '    Split:     Split each page into a Fumen',
        '',
        '    Glue:      Glue each Fumen page into tetromino placements',
        '               Alias: Decompile',
        '    Unglue:    Unglue Fumen placements into one page',
        '               Alias: Compile',
        '',
        '    Gray:      Gray out the last page of each fumen',
        '               Alias: Grey'
        '    Grayall:   Gray out all pages of each fumen',
        '               Alias: Greyall',
        '',
        '    Lock:      Lock the last page of each Fumen and append a new page',
        '    Mirror:    Mirror Fumen pages',
        '               Alias: Flip',
        '    Uncomment: Uncomment Fumen pages',
    ]

if __name__ == '__main__':
    if len(sys.argv) > 2:
        command = sys.argv[1].casefold()
        fumen_codes = ' '.join(sys.argv[2:]).split()

        command_function = {
            'combine': fumen_combiner,
            'concat' : fumen_combiner,
            'join': fumen_combiner,
            'split': fumen_splitter,
            'glue': glue_fumen,
            'decompile': glue_fumen,
            'unglue': unglue_fumen,
            'compile': unglue_fumen,
            'gray': grayout_fumen,
            'grey': grayout_fumen,
            'grayall': grayout_all_fumen,
            'greyall': grayout_all_fumen,
            'lock': fumen_locker,
            'mirror': mirror_fumen,
            'flip': mirror_fumen,
            'uncomment': remove_comment,
        }.get(command, usage)
    else:
        command_function = usage
        fumen_codes = None

    try:
        for line in command_function(fumen_codes):
            print(line)
    except Exception as e:
        print(e)
        usage()
