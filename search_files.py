import json
from config import INDEX_PATH, MAX_SEARCH_RESULTS

def load_index(json_path=INDEX_PATH):
    with open(json_path, "r") as f:
        files = json.load(f)
    return files

def search_files(files, query):
    query = query.lower()
    results = [f for f in files if query in f.lower()]
    return results

if __name__ == "__main__":
    try:
        files = load_index()
    except FileNotFoundError:
        print(f"No index found at {INDEX_PATH}. Please scan a folder first.")
        exit()

    query = input("Enter what you want to search for: ")
    results = search_files(files, query)
    
    print(f"Found {len(results)} matching files:")
    for r in results[:MAX_SEARCH_RESULTS]:
        print(r)
