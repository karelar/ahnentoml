if __name__ == "__main__":
    from pathlib import Path
    import os
    base_dir = Path.cwd()
    from .types import read
    for _type in ["ind", "image"]:
        for f in os.listdir(base_dir / (_type + "s")):
            if not f.endswith(".toml"):
                continue
            id = _type + "." + os.path.splitext(f)[0]
            try:
                obj = read(str(base_dir), id)
                if obj.is_empty():
                    print(f"{id} is empty")
                else:
                    print(f"{id} is valid")
            except Exception as e:
                print(f"{id} has error: {str(e)}")

