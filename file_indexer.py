import os
import json
from config import INDEX_PATH

def list_files(folder_path, allowed_extensions=None):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        # Skip hidden folders
        dirs[:] = [d for d in dirs if not d.startswith(".") and not d.startswith("__")]
        for file in files:
            if file.startswith(".") or file.endswith(".pyc"):
                continue  # skip hidden or compiled files
            if allowed_extensions and not any(file.lower().endswith(ext) for ext in allowed_extensions):
                continue
            file_list.append(os.path.join(root, file))
    return file_list

def save_index(file_list, output_path=INDEX_PATH):
    with open(output_path, "w") as f:
        json.dump(file_list, f)
    print(f"Saved index to {output_path}")

if __name__ == "__main__":
    folder = input("Enter the folder path to scan: ").strip()
    files = list_files(folder, allowed_extensions=[".txt"])  # example: only index .txt
    print(f"Found {len(files)} files.")
    save_index(files)
