import tomli
import os

from .base import Base


def read_from_toml(base_dir, name):
    path = os.path.join(base_dir, "images", name + ".toml")
    with open(path, "rb") as f:
        data = tomli.load(f)
    return read_from_dict(data, name)


def read_from_dict(data: dict, name: str):
    return Image(data, name)


class Image(Base):
    def __init__(self, data: dict, name: str):
        super().__init__("image", name, data)

    @property
    def summary(self):
        return self._data['caption']


