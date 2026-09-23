from pathlib import Path

# 1. Define the target directory (use current folder for testing)
target_dir = Path(".")

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

# 4. Loop through files and move them
for file_path in target_dir.iterdir():
    if file_path.is_file() and file_path.suffix:
        # TODO: Check which folder category this file_path.suffix belongs to
        pass