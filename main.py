from search.file_indexer import list_files, save_index
from search.search_files import search_files
from search import semantic_search
import os
import tkinter as tk
from tkinter import filedialog

def pick_folder():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select folder to scan")
    return folder

def main():
    print("=== AI File Assistant MVP ===")
    
    choice = input("Do you want to scan a folder for files? (y/n): ").lower()
    
    if choice == "y":
        folder = pick_folder()
        if not folder:
            print("No folder selected. Exiting.")
            return
        print(f"Selected folder: {folder}")

        files = list_files(folder, allowed_extensions=[".txt"])
        print(f"Found {len(files)} files.")
        save_index(files)  # optional, keeps a copy on disk
    
    else:
        try:
            import json
            with open("data/file_index.json", "r") as f:
                files = json.load(f)
            print(f"Loaded index with {len(files)} files.")
        except FileNotFoundError:
            print("No existing index found. Please scan a folder first.")
            return
    
    if not files:
        print("No files to search. Exiting.")
        return
    
    search_type = input("Choose search type: literal (l) or AI semantic (a): ").lower()
    
    query = input("Enter what you want to search for: ").strip()
    
    if search_type == "l":
        results = search_files(files, query)
        print(f"\nFound {len(results)} matching files (top 10 shown):")
        for r in results[:10]:
            print(r)
    elif search_type == "a":
        results, scores = semantic_search.semantic_search(query, files)
        print(f"\nFound {len(results)} matching files (top 10 shown):")
        for r, s in zip(results[:10], scores[:10]):
            print(f"{r} (score: {s:.3f})")
    else:
        print("Invalid option. Defaulting to literal search.")
        results = search_files(files, query)
        print(f"\nFound {len(results)} matching files (top 10 shown):")
        for r in results[:10]:
            print(r)

if __name__ == "__main__":
    main()
