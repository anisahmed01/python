from pathlib import Path
import os


BASE_DIR = Path.cwd()


def list_files():
    """Return a list of all files under BASE_DIR (recursive) and print them numbered."""
    files = [p for p in BASE_DIR.rglob("*") if p.is_file()]
    if not files:
        print("No files found.")
        return []

    print("\nAvailable files:\n")
    for idx, f in enumerate(files, start=1):
        print(f"{idx}. {f}")
    print()
    return files


def create_file():
    try:
        name = input("Enter new file name (with path if needed): ").strip()
        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)

        if p.exists():
            print("This file already exists.")
            return

        if not p.parent.exists():
            print("Folder path does not exist.")
            return

        data = input("What do you want to write in this file: ")
        with open(p, "w", encoding="utf-8") as fs:
            fs.write(data)

        print("FILE CREATED SUCCESSFULLY")

    except Exception as err:
        print(f"An error occurred: {err}")


def read_file():
    try:
        files = list_files()
        if not files:
            return

        choice = input("Enter the number of the file you want to read: ").strip()
        if not choice.isdigit():
            print("Invalid input.")
            return

        idx = int(choice)
        if not (1 <= idx <= len(files)):
            print("Invalid file number.")
            return

        p = files[idx - 1]

        with open(p, "r", encoding="utf-8") as fs:
            data = fs.read()

        print("\n----- FILE CONTENT START -----\n")
        print(data)
        print("\n----- FILE CONTENT END -----\n")
        print("FILE READ SUCCESSFULLY")

    except Exception as err:
        print(f"An error has occurred: {err}")


def update_file():
    try:
        files = list_files()
        if not files:
            return

        choice = input("Enter the number of the file you want to update: ").strip()
        if not choice.isdigit():
            print("Invalid input.")
            return

        idx = int(choice)
        if not (1 <= idx <= len(files)):
            print("Invalid file number.")
            return

        p = files[idx - 1]

        print("\nWhat do you want to do?")
        print("1. Rename the file")
        print("2. Overwrite the file content")
        print("3. Append to the file")
        action = input("Enter your choice (1/2/3): ").strip()

        if action == "1":
            new_name = input("Enter the new file name: ").strip()
            if not new_name:
                print("New file name cannot be empty.")
                return
            p2 = p.with_name(new_name)
            p.rename(p2)
            print("FILE NAME UPDATED SUCCESSFULLY!")

        elif action == "2":
            data = input("Enter new content (this will overwrite existing data): ")
            with open(p, "w", encoding="utf-8") as fs:
                fs.write(data)
            print("FILE CONTENT OVERWRITTEN SUCCESSFULLY!")

        elif action == "3":
            data = input("Enter content to append: ")
            with open(p, "a", encoding="utf-8") as fs:
                fs.write("\n" + data)
            print("FILE UPDATED (APPENDED) SUCCESSFULLY!")

        else:
            print("Invalid option selected.")

    except Exception as err:
        print(f"An error occurred: {err}")


def delete_file():
    try:
        files = list_files()
        if not files:
            return

        choice = input("Enter the number of the file you want to delete: ").strip()
        if not choice.isdigit():
            print("Invalid input.")
            return

        idx = int(choice)
        if not (1 <= idx <= len(files)):
            print("Invalid file number.")
            return

        p = files[idx - 1]

        confirm = input(f"Are you sure you want to delete '{p}'? (y/N): ").strip().lower()
        if confirm == "y":
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("Deletion cancelled.")

    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    while True:
        print("\n--- FILE MANAGER ---")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("Q. Quit")

        choice = input("Please enter your choice: ").strip().lower()

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_file()
        elif choice == "q":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
