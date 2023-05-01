# -*- coding: utf-8 -*-

import sys

from py_fumen_py import *

def cleared_offset(rows_cleared, y):
    for row in rows_cleared:
        if y >= row:
            y += 1
    return y

def unglue_fumen(fumen_codes):
    unglued_fumen = []

    for code in fumen_codes:
        rows_cleared = set()
        input_pages = decode(code)
        field = input_pages[0].field.copy()

        for page in input_pages:
            operation = page.operation
            if operation is None:
                print('warning: skipped a page with no operation')
                continue

            for dx, dy in Operation.shape_at(operation.mino,
                                             operation.rotation):
                x = operation.x + dx
                y = cleared_offset(rows_cleared, operation.y+dy)
                if field.at(x, y) != Mino._:
                    print('error: operation overlaps with current field')
                field.fill(x, y, operation.mino)

            new_rows_cleared = set()
            for dy in range(-2, 3):
                y = cleared_offset(rows_cleared, operation.y+dy)
                if y >= 0 and field.is_lineclear_at(y):
                    new_rows_cleared.add(y)
            rows_cleared |= new_rows_cleared

        unglued_fumen.append(encode([Page(field=field)]))

    return unglued_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in unglue_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
