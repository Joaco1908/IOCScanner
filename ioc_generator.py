from rich import print
import argparse 

# It will create a JSON file to scan it with ioc_scanner
# Two flags: one for the output filename -o and another one to add more information to a .json file -a 

def main():
    parser = argparse.ArgumentParser(description="Generate and manipulate JSON files")

    parser.add_argument('-o', '--output', type=str, help="Name of the output file", required=True)
    parser.add_argument('-a', '--append', type=str, help="Modify a json file and append information")

    args = parser.parse_args()


if __name__ == "__main__":
    main()
