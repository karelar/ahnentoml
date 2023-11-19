from .base import Base
from .image import read_from_toml as read_image
from .ind import read_from_toml as read_ind

from typing import Tuple


def read(base_dir: str,  id: str) -> Base:
    _type, name = id_components(id)
    if _type == 'image':
        return read_image(base_dir, name)
    if _type == 'ind':
        return read_ind(base_dir, name)


def id_components(id:str) -> Tuple[str, str]:
    type_, name = id.split('.', 1)
    return type_, name