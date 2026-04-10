# txt2js list
txt2js is a Python tool that converts a raw text file into a JavaScript file, exporting the contents to a single array of strings (one element per line)

## Installation
Clone this repo:
```bash
```bash
git clone https://github.com/NitroBTW/txt2js-list
cd txt2js-list
```

## Usage
[uv](https://docs.astral.sh/uv/):
```bash
uv run main.py -i <path_to_input_file> -o <output_file_name>
```

## Arguments
`-i/--input` - Full path to input file
`-o/--output` - Name of output file (excluding extension)
`-v/--variable-name` - Name of the resulting JavaScript variable

## Example
```input.txt
hello
world
```

```output.js (generated)
export const HELLO_WORLD [
    'hello',
    'world'
]
```

## Contributing

Pull requests are welcome, however this was simply a built-in-a-day automation tool as developers tend to do.

## License

[MIT](https://choosealicense.com/licenses/mit/)
