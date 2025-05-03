from rich import print
import argparse 
import json
import sys

# It will create a JSON file to scan it with ioc_scanner
# Two flags: one for the output filename -o and another one to add more information to a .json file -a 


def main():
    parser = argparse.ArgumentParser(description="Generate and manipulate JSON files")

    parser.add_argument('-o', '--output', type=str, help="Name of the output file")
    parser.add_argument('-a', '--append', type=str, help="Used to edit an existing json file")

    args = parser.parse_args()

    # If there is not a -o flag, use the filename ioc_file.json 
    if args.output:
        filename = args.output
        # Verify if it ends with .json 
        if (not filename.lower().endswith(".json")):
            print("[red][!] Error: Output file must have a .json extension.[/]")
            sys.exit(1)
    else:
        filename = "ioc_file.json"

    print(filename)

#    with open(filename, "w") as f:


if __name__ == "__main__":
    main()

