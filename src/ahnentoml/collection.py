import os
from pathlib import Path

from .types import read, id_components
from .types.base import Base

from typing import Dict, Union


class Collection:
    def __init__(self, base_dir: str, by_type: Dict[str, Dict[str, Base]], by_path: Dict[str, Base]):
        self.by_type = by_type
        self.base_dir = base_dir
        self.by_path = by_path

    def get_by_id(self, id: str, rel_dir: Union[str, None]) -> Union[Base, None]:
        if rel_dir:
            id_as_path = str((Path(rel_dir).parent / Path(id)).resolve())
            if id_as_path in self.by_path:
                return self.by_path[id_as_path]
        type_, _ = id_components(id)
        if type_ in self.by_type and id in self.by_type[type_]:
            return self.by_type[type_][id]
        return None


def read_collection(base_dir: str) -> Collection:
    by_type = dict()
    by_path = dict()
    errors = list()
    for _type in ["ind", "image"]:
        by_type[_type] = dict()
        type_dir = os.sep.join([base_dir, _type + "s"])
        for f in os.listdir(type_dir):
            if not f.endswith(".toml"):
                continue
            id = _type + "." + os.path.splitext(f)[0]
            try:
                obj = read(str(base_dir), id)
                by_type[_type][id] = obj
                by_path[str((Path(type_dir) / f).resolve())] = obj
            except Exception as e:
                errors.append(f"{id} has error: {str(e)}")

    # if errors:
    #     raise Exception(errors)
    return Collection(base_dir, by_type, by_path)


"""
Reads the project in the current directory and some simple checking that their structure/references are valid.
Any invalid toml files are ignored at this time.
"""
if __name__ == "__main__":
    c = read_collection('')
    for path in c.by_path:
        c.by_path[path].references(c)
