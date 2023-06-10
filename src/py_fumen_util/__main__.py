# -*- coding:utf-8 -*-

import argparse
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

_command_function_map = {
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
}

def usage():
    return [
        'commands (case-insensitive):',
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
    argparser = argparse.ArgumentParser(
        description='Tetris Fumen utilies in Python.',
        prog='python3 -m py_fumen_util'
    )
    argparser.add_argument(
        'command',
        type=str,
        nargs='+',
        help='Command(s) to execute on the Fumen(s).'
    )
    argparser.add_argument(
        'file',
        type=str,
        help='File with Fumen strings, separated with whitespace and/or linebreak. Use "-" to read from standard input.'
    )

    args = argparser.parse_args(sys.argv[1:])
    commands = args.command
    fumen_file = sys.stdin if args.file == '-' else open(args.file, 'r')
    fumen_codes = fumen_file.read().split()
    fumen_file.close()

    for command in commands:
        command_function = _command_function_map.get(command.casefold(), None)
        try:
            fumen_codes = command_function(fumen_codes)
        except Exception as e:
            if command_function:
                print(e)
            else:
                print(f'"{command}" is not a valid command.')
            print()
            argparser.print_help()
            print()
            for line in usage():
                print(line)
            exit()

    for line in fumen_codes:
        print(line)
