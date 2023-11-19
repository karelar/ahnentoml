"""
Reads a single toml file based on its ID from the current directory, and logs if it is empty, valid, or invalid.
"""
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("Error, no ids listed")
        exit(1)
    from pathlib import Path
    base_dir = Path.cwd()
    from .types import read
    for id in sys.argv[1:]:
        try:
            obj = read(str(base_dir), id)
            if obj.is_empty():
                print(f"{id} is empty")
            else:
                print(f"{id} is valid")
        except Exception as e:
            print(f"{id} has error: {str(e)}")

