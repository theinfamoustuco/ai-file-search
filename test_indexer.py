from file_indexer import list_files, save_index
import os
import json

test_folder = input("Enter a folder to test indexing: ").strip()
if not os.path.exists(test_folder):
    print("Folder does not exist. Exiting.")
    exit()

files = list_files(test_folder)
print(f"Found {len(files)} files in '{test_folder}'.")

temp_index_path = "test_file_index.json"
save_index(files, temp_index_path)

if os.path.exists(temp_index_path):
    with open(temp_index_path, "r") as f:
        loaded_files = json.load(f)
    print(f"JSON file saved successfully with {len(loaded_files)} entries.")
else:
    print("Failed to save JSON file.")
