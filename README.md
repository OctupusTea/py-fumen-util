# py-fumen-util
Python implementation of [swng's FumenUtil](https://github.com/swng/FumenUtil), using [hsohliyt105's py-fumen](https://github.com/hsohliyt105/py-fumen)

## Dependency
- `py-fumen`: Python implementation of knewjade's `tetris-fumen` node module

## Usage

```bash
python3 -m py_fumen_util command fumen_code [fumen_code...]
```

### Commands

Commands are case-insensitive.

|Command|Description|Alias|
|:-|:-|:-|
|Combine|Combine multiple Fumens into one|Concat, Join|
|Split|Split each page into a Fumen||
|Glue|Glue each Fumen page into tetromino placements|Decompile|
|Unglue|Unglue Fumen placements into one page|Compile|
|Lock|Lock the last page of each Fumen and append a new page||
|Mirror|Mirror Fumen pages|Flip|
|Uncomment|Uncomment Fumen pages||
