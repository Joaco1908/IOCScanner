from rich import print
import argparse 
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate and manipulate JSON files")

    parser.add_argument('-t', '--textfile', type=str, help="Name of the textfile with the IPs.")

    args = parser.parse_args()

    if (args.textfile):
        # If there is a text file
        if (not os.path.exists(args.textfile)):
            print(f"\n[red][!] Error: File '{args.textfile}' does not exist.[/]")
            sys.exit(1)
        if (not args.textfile.lower().endswith(".txt")):
                print("\n[red][!] Error: The textfile must have a .txt extension.[/]")
                sys.exit(1)
    else:
        # If there is no text file (gather IPs from console)
        print(f"\n[green][+] Give me the IP that you want to check: ", end="")
        text_console = input()
    


if __name__ == "__main__":
    main()
