# -*- coding: utf-8 -*-

import sys

from py_fumen import encoder, decoder
from py_fumen.constants import FieldConstants
from py_fumen.defines import Piece
from py_fumen.field import Field
from py_fumen.page import Page

MIRROR_MINO = {
    '_': '_',
    'I': 'I',
    'L': 'J',
    'O': 'O',
    'Z': 'S',
    'T': 'T',
    'J': 'L',
    'S': 'Z',
    'X': 'X',
}

MIRROR_PIECE = {
    Piece.EMPTY: Piece.EMPTY,
    Piece.I: Piece.I,
    Piece.L: Piece.J,
    Piece.O: Piece.O,
    Piece.Z: Piece.S,
    Piece.T: Piece.T,
    Piece.J: Piece.L,
    Piece.S: Piece.Z,
    Piece.GRAY: Piece.GRAY,
}

MIRROR_ROTATION = {
    'spawn': 'spawn',
    'right': 'left',
    'reverse': 'reverse',
    'left': 'right',
}

def _mirror_field(field):
    field.mirror()
    field._InnerField__field._PlayField__pieces = [
        MIRROR_PIECE[p] for p in field._InnerField__field._PlayField__pieces
    ]

def _mirror_operation(operation):
    if operation is not None:
        operation.piece_type = MIRROR_MINO[operation.piece_type]
        if operation.piece_type in 'OI':
            if operation.rotation == 'reverse':
                operation.x = FieldConstants.WIDTH - operation.x
            elif operation.rotation == 'left' and operation.piece_type == 'O':
                operation.x = FieldConstants.WIDTH - operation.x
            elif operation.rotation == 'spawn' or operation.piece_type == 'O':
                operation.x = FieldConstants.WIDTH - operation.x - 2
            else:
                operation.x = FieldConstants.WIDTH - operation.x - 1
        else:
            operation.rotation = MIRROR_ROTATION[operation.rotation]
            operation.x = FieldConstants.WIDTH - operation.x - 1

def mirror_fumen(fumen_codes):
    mirrored_fumen = []
    for code in fumen_codes:
        input_pages = decoder.decode(code)
        for i, page in enumerate(input_pages):
            _mirror_field(page._Page__field)
            _mirror_operation(page.operation)
        mirrored_fumen.append(encoder.encode(input_pages))
    return mirrored_fumen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for line in mirror_fumen(' '.join(sys.argv[1:]).split()):
            print(line)
