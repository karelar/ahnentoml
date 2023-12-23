import tomli
import os

from .base import Base


def read_from_toml(base_dir, name):
    path = os.path.join(base_dir, "inds", name + ".toml")
    with open(path, "rb") as f:
        data = tomli.load(f)
    return read_from_dict(data, name)


def read_from_dict(data: dict, name: str):
    return Individual(data, name)


class Individual(Base):
    def __init__(self, data: dict, name: str):
        super().__init__("ind", name, data)

    @property
    def summary(self):
        return str(self._data['name'])

