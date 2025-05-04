from rich import print
import argparse 
import json
import sys
import os 

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
            print("\n[red][!] Error: Output file must have a .json extension.[/]")
            sys.exit(1)
    else:
        filename = "ioc_file.json"

    # For the --apend flag 
    if args.append:
        open_file = args.append
        open_path = "iocGeneratedFiles/" + open_file 
        if (not os.path.exists(open_path)):
            print(f"\n[red] [!] Error: File '{open_path}' does not exists.[/]")
            sys.exit(1)
        # Open file to append
        with open(open_path, "r") as f:
            ioc_data = json.load(f)
    else:
        # Basic model of the IOC json data 
        ioc_data = {
            "filenames": [],
            "file sizes": [],
            "hashes": []
        }

    # Create all the path to create the file
    path = "iocGeneratedFiles/" + filename

    # Verify if the file doesn't already exists
    if (os.path.exists(path) and not args.append) or (os.path.exists(path) and args.append and args.output):
        print(f"\n[red] [!] Error: File '{path}' already exists.[/]")
        sys.exit(1)

    # --- The user adds the information 
    # Valid choices for the input
    valid_choices = {1, 2, 3, 4}

    print("\nWhat do you want to add?\n1. File name\n2. File size\n3. A file hash\n4. Create file")
    answer_choice = int(input())

    while answer_choice not in valid_choices:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        level = int(input("What do you want to do?: "))
    
    add(answer_choice, ioc_data)

    while not (answer_choice == 4):
        print("\nWhat do you want to add?\n1. File name\n2. File size\n3. A file hash\n4. Create file")
        answer_choice = int(input())
        while answer_choice not in valid_choices:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            answer_choice = int(input("What do you want to do?: "))
        add(answer_choice, ioc_data)

    if args.append and not args.output:
        with open(open_path, "w") as f:
            json.dump(ioc_data, f, indent=4)
            print("[green]\n[+] File modified: " + open_path +".[/]")

    else:
        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            json.dump(ioc_data, f, indent=4)
            print("[green]\n[+] File created: " + path +".[/]")


# to add json information to ioc_data
def add(answer_choice, ioc_data):

    if (answer_choice == 1):
        append_data = input("What is the filename that you want to add?: ")
        ioc_data["filenames"].append(append_data)
    elif (answer_choice == 2):
        append_data = input("What is the file size that you want to add?: ")
        ioc_data["file sizes"].append(append_data)
    elif (answer_choice == 3): 
        append_data = input("What is the file hash that you want to add?: ")
        ioc_data["hashes"].append(append_data)

if __name__ == "__main__":
    main()
