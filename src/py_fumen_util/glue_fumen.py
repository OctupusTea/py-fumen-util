# -*- coding: utf-8 -*-

import sys

from py_fumen_py import *

PIECE_MAPPINGS = {
    Mino.I: [
        [[1, 0], [0, 0], [2, 0], [3, 0]],
        [[0, -2], [0, 0], [0, -1], [0, -3]],
    ],
    Mino.L: [
        [[-1, -1], [0, 0], [-2, -1], [0, -1]],
        [[1, -1], [0, 0], [1, 0], [1, -2]],
        [[1, 0], [0, 0], [2, 0], [0, -1]],
        [[0, -1], [0, 0], [0, -2], [1, -2]],
    ],
    Mino.O: [
        [[0, -1], [0, 0], [1, 0], [1, -1]],
    ],
    Mino.Z: [
        [[1, -1], [0, 0], [1, 0], [2, -1]],
        [[0, -1], [0, 0], [-1, -1], [-1, -2]],
    ],
    Mino.T: [
        [[0, -1], [0, 0], [-1, -1], [1, -1]],
        [[0, -1], [0, 0], [-1, -1], [0, -2]],
        [[1, 0], [0, 0], [2, 0], [1, -1]],
        [[0, -1], [0, 0], [1, -1], [0, -2]],
    ],
    Mino.J: [
        [[1, -1], [0, 0], [0, -1], [2, -1]],
        [[0, -1], [0, 0], [-1, -2], [0, -2]],
        [[1, 0], [0, 0], [2, 0], [2, -1]],
        [[0, -1], [0, 0], [1, 0], [0, -2]],
    ],
    Mino.S: [
        [[0, -1], [0, 0], [1, 0], [-1, -1]],
        [[1, -1], [0, 0], [0, -1], [1, -2]],
    ],
}

def is_inside(field, x, y):
    return 0 <= x < FieldConstants.WIDTH and 0 <= y < field.height()

def place_piece(field, mino_positions):
    for x, y in mino_positions:
        field.fill(x, y, Mino.X)

def remove_line_clears(field):
    lines = []
    n_lineclear = 0
    for line in field:
        if all(mino is Mino.X for mino in line):
            n_lineclear += 1
        else:
            lines.append(line)
    return Field(field=lines, garbage=field[:0]), n_lineclear

def find_remaining_pieces(field):
    remaining = set()
    for line in field:
        for mino in line:
            if mino.is_colored():
                remaining.add(mino)
    return remaining

def check_rotation(x, y, field, pieces_arr, all_pieces_arr):
    piece = field.at(x, y)
    found = False
    leftover_pieces = None

    for state, piece_shape in enumerate(PIECE_MAPPINGS[piece]):
        mino_positions = [[x+dx, y+dy] for dx, dy in piece_shape]

        for px, py in mino_positions:
            if not is_inside(field, px, py) or field.at(px, py) != piece:
                break
        else:
            found_before = found
            found = True
            new_piece_arr = pieces_arr[:]
            new_piece_arr.append(
                Operation(mino=piece, rotation=Rotation(state).shifted(2),
                          x=mino_positions[0][0], y=mino_positions[0][1])
            )

            new_field = field.copy()
            place_piece(new_field, mino_positions)
            new_field, n_lineclear = remove_line_clears(new_field)

            x0, y0 = (0, new_field.height()-1) if n_lineclear else (x, y)

            old_len = len(all_pieces_arr)
            poss_piece_arr, leftover_pieces = scan_field(
                x0, y0, new_field, new_piece_arr, all_pieces_arr
            )

            if leftover_pieces is None:
                leftover_pieces = find_remaining_pieces(new_field)

            if poss_piece_arr is not None and not leftover_pieces:
                all_pieces_arr.append(poss_piece_arr)
            elif old_len == len(all_pieces_arr):
                if piece not in leftover_pieces:
                    return found, leftover_pieces
                else:
                    found = found_before
    return found, leftover_pieces

def scan_field(x0, y0, field, pieces_arr, all_pieces_arr):
    for y in range(y0, -1, -1):
        for x in range(x0 if y == y0 else 0, FieldConstants.WIDTH):
            if field.at(x, y).is_colored():
                rotation_worked, leftover = check_rotation(
                    x, y, field, pieces_arr, all_pieces_arr
                )
                if rotation_worked:
                    return None, leftover
    return pieces_arr, None

def make_empty_field(field):
    field = field.copy()
    for line in field:
        for i, mino in enumerate(line):
            if mino.is_colored():
                line[i] = Mino._
    return field

def glue_fumen(fumen_codes):
    all_pieces_arr = []
    all_fumens = []
    fumen_issues = 0

    for code in fumen_codes:
        input_pages = decode(code)
        this_glue_fumens = []
        for page in input_pages:
            field, n_lineclear = remove_line_clears(page.field.copy())
            empty_field = make_empty_field(field)
            all_pieces_arr.clear()

            scan_field(0, field.height()-1, field, [], all_pieces_arr)

            if not all_pieces_arr:
                print(code, "couldn't be glued")
                fumen_issues += 1

            for pieces_arr in all_pieces_arr:
                pages = [Page(field=empty_field, operation=pieces_arr[0])]
                for operation in pieces_arr[1:]:
                    pages.append(Page(operation=operation))
                this_glue_fumens.append(encode(pages))

            if len(all_pieces_arr) > 1:
                all_fumens.append(
                    'Warning: {} led to {} outputs: {}'.format(
                        code, len(all_pieces_arr), ' '.join(this_glue_fumens)
                    )
                )
        all_fumens += this_glue_fumens

    if fumen_issues > 0:
        print("Warning: {} fumen couldn't be glued".format(fumen_issues))
    return all_fumens

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in glue_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
