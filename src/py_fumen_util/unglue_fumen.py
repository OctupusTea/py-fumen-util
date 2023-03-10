# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder
from py_fumen.constants import FieldConstants
from py_fumen.field import create_inner_field
from py_fumen.inner_field import InnerField
from py_fumen.page import Page

PIECES = {
    'T': [
        [[0, 0], [0, -1], [0, 1], [1, 0]],
        [[0, 0], [0, 1], [1, 0], [-1, 0]],
        [[0, 0], [0, -1], [0, 1], [-1, 0]],
        [[0, 0], [0, -1], [1, 0], [-1, 0]],
    ],
    'I': [
        [[0, 0], [0, -1], [0, 1], [0, 2]],
        [[0, 0], [1, 0], [-1, 0], [-2, 0]],
        [[0, 0], [0, -1], [0, -2], [0, 1]],
        [[0, 0], [1, 0], [2, 0], [-1, 0]],
    ],
    'L': [
        [[0, 0], [0, -1], [0, 1], [1, 1]],
        [[0, 0], [1, 0], [-1, 0], [-1, 1]],
        [[0, 0], [0, -1], [0, 1], [-1, -1]],
        [[0, 0], [1, -1], [1, 0], [-1, 0]],
    ],
    'J': [
        [[0, 0], [0, -1], [0, 1], [1, -1]],
        [[0, 0], [1, 0], [-1, 0], [1, 1]],
        [[0, 0], [0, -1], [0, 1], [-1, 1]],
        [[0, 0], [-1, -1], [1, 0], [-1, 0]],
    ],
    'S': [
        [[0, 0], [0, -1], [1, 0], [1, 1]],
        [[0, 0], [1, 0], [0, 1], [-1, 1]],
        [[0, 0], [0, 1], [-1, 0], [-1, -1]],
        [[0, 0], [-1, 0], [0, -1], [1, -1]],
    ],
    'Z': [
        [[0, 0], [0, 1], [1, 0], [1, -1]],
        [[0, 0], [-1, 0], [0, 1], [1, 1]],
        [[0, 0], [0, -1], [-1, 0], [-1, 1]],
        [[0, 0], [1, 0], [0, -1], [-1, -1]],
    ],
    'O': [
        [[0, 0], [1, 0], [0, 1], [1, 1]],
        [[0, 0], [0, 1], [-1, 0], [-1, 1]],
        [[0, 0], [-1, 0], [0, -1], [-1, -1]],
        [[0, 0], [0, -1], [1, -1], [1, 0]],
    ],
}

ROTATION_MAPPING = {
    'spawn': 0,
    'right': 1,
    'reverse': 2,
    'left': 3,
}

def cleared_offset(rows_cleared, y):
    for row in rows_cleared:
        if y >= row:
            y += 1
    return y

def unglue_fumen(fumen_codes):
    unglued_fumen = []

    for code in fumen_codes:
        rows_cleared = set()
        input_pages = decoder.decode(code)
        field = input_pages[0].get_field()

        for page in input_pages:
            operation = page.operation
            if operation is None:
                print('warning: skipped a page without an operation')
                continue

            for dy, dx in PIECES[operation.piece_type]\
                    [ROTATION_MAPPING[operation.rotation]]:
                x = operation.x + dx
                y = cleared_offset(rows_cleared, operation.y+dy)
                if field.at(x, y) != '_':
                    print('error: operation overlaps with current field')
                field.set(x, y, operation.piece_type)

            new_rows_cleared = set()
            for dy in range(-2, 3):
                y = cleared_offset(rows_cleared, operation.y+dy)
                if y >= 0 and all(field.at(x, y) != '_'\
                                  for x in range(0, FieldConstants.WIDTH)):
                    new_rows_cleared.add(y)
            rows_cleared |= new_rows_cleared

        unglued_fumen.append(encoder.encode([Page(field=create_inner_field(field))]))

    return unglued_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in unglue_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
