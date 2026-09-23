from pathlib import Path

# 1. Define the target directory (use current folder for testing)
# target_dir = Path(".")
target_dir = Path(input("Enter the Target Directory: "))
if not target_dir.exists() and not target_dir.is_file():
    print(f"{target_dir} DOES NOT EXIST")

# 2. Define our categories and their extensions
folders_map = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Data": [".csv", ".xlsx"]
}

# 3. Create folders if they don't exist yet
for folder_name in folders_map.keys():
    folder_path = target_dir / folder_name
    # TODO: Create the directory using pathlib (Hint: look up .mkdir())
    print(f"Ensuring folder exists: {folder_path}")
    if not folder_path.exists():
        Path.mkdir(folder_path)

    if folder_path.exists():
        print(f"Folder exists: {folder_path}")

# 4. Loop through files and move them
for file_path in target_dir.iterdir():
 # Make sure we are looking at a file (not a folder) and it has an extension
    if file_path.is_file() and file_path.suffix:
        file_ext = file_path.suffix.lower()
        
        # Find which category matches this file extension
        target_folder = None
        for category, extensions in folders_map.items():
            if file_ext in extensions:
                target_folder = target_dir / category
                break
        
        # If a matching category folder was found, move the file
        if target_folder:
            destination = target_folder / file_path.name
            file_path.rename(destination)
            print(f"Moved: {file_path.name} -> {target_folder.name}/")

print("\n--- Organization Complete! ---")