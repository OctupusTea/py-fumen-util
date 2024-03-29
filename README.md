# py-fumen-util
Python implementation of [swng's FumenUtil](https://github.com/swng/FumenUtil), using [py-fumen-py](https://github.com/OctupusTea/py-fumen-py)

## Dependency
- `py-fumen-py`: Python implementation of knewjade's `tetris-fumen` node module

## Installation

```bash
python3 -m pip install py-fumen-util
```

## Usage

```bash
python3 -m py_fumen_util command [commmand...] file
```

- `command`: Command(s) to execute on the Fumen(s).
- `file`: File with Fumen strings, separated with whitespace and/or linebreak. Use "-" to read from standard input.

### Commands

ommands are case-insensitive.

|Command|Description|Alias|
|:-|:-|:-|
|join|Join multiple Fumens into one|combine concat|
|split|Split each page into a Fumen||
|assemble|Assemble Fumen placements into one page|compile, unglue|
|disassemble|Disassemble each Fumen page into tetrimino placements|decompile, glue|
|gray|Gray out the last page of each Fumen|grey|
|grayall|Gray out all pages of each Fumen|greyall|
|prune|Prune colored minos from the last page of each Fumen||
|pruneall|Prune colored minos from all pages of each Fumen||
|lock|Lock the last page of each Fumen and append a new page||
|mirror|Mirror Fumen pages|flip|
|uncomment|Uncomment Fumen pages||
