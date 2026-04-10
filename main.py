import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

# Initialise the parser 
parser = argparse.ArgumentParser(
    description="A python script to take a text input and generate a js file with an Array seperated by newlines",
)

parser.add_argument(
    "-i",
    "--input",
    type=Path,
    default=SCRIPT_DIR / "input.txt",
    help="Path to input file",
)

parser.add_argument(
    "-o",
    "--output",
    type=str,
    default="output",
    help="Name of output file"
)

parser.add_argument(
    "-v",
    "--variable-name",
    type=str,
    default="TXT2JS",
    help="Name of the resulting JavaScript variable"
)

# Parse arguments
args = parser.parse_args()

INPUT_FILE = args.input
OUTPUT_FILE = f"{args.output}.js"
VARIABLE_NAME = args.variable_name

def main():
    content = [f"export const {VARIABLE_NAME} = ["]
    try:
        # Create a list of lines to be written as a variable
        with open(INPUT_FILE, "r") as f:
            input_lines = f.readlines()
            for line in input_lines:
                content.append(f"\t'{line.rstrip()}',")
            f.close()
        content.append("]")
    
        # Write list to output file       
        with open(OUTPUT_FILE, "w+") as g:
            g.write("\n".join(content))
            g.close()
    except Exception as e:
        print(f"Failed to write to file: {e}")
    
    print(f"Successfully wrote {len(content)} lines to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
