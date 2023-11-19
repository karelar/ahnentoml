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
            read(str(base_dir), id)
            print(f"{id} is valid")
        except Exception as e:
            print(f"{id} has error: {str(e)}")

