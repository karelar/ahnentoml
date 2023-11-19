import abc
from abc import ABC
import os
from typing import List


class Base(ABC):
    _type: str
    _data: dict
    _name: str

    def __init__(self, type: str, name: str, data: dict):
        self._data = data
        self._type = type
        self._name = name

    @property
    def path(self) -> str:
        """
        :return: a relative path from the base directory to where this data can be found.
        """
        # note that we pluralize the type
        return os.sep.join([self._type + "s", self.filename])

    @property
    def filename(self) -> str:
        return self._name + ".toml"

    @property
    def id(self) -> str:
        return self._type + "." + self._name

    def references(self, collection: 'ahnen.collection.Collection') -> List['Base']:
        """
        :return: all references, regardless of type. Current implementation assumes any field named "id"
        denotes a reference to another object in the system, in the future this is likely to be abstract
        """
        r = []
        self._find_references_in_dict(r, self._data, collection)
        return r

    def _find_references_in_dict(self, r: List['Base'], data: dict, collection: 'ahnen.collection.Collection') -> None:
        if 'id' in data:
            ref = collection.get_by_id(data['id'], self.path)
            if ref is not None:
                r.append(ref)
            else:
                print(f"Missing reference in {self.path}: {data['id']}")

        if 'individual' in data and type(data['individual']) is str:
            ref = collection.get_by_id(data['individual'], self.path)
            if ref is not None:
                r.append(ref)
            else:
                print(f"Missing reference in {self.path}: {data['individual']}")



        for k in data:
            if type(data[k]) is dict:
                self._find_references_in_dict(r, data[k], collection)
            if type(data[k]) is list:
                for item in data[k]:
                    if type(item) is dict:
                        self._find_references_in_dict(r, item, collection)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    @abc.abstractproperty
    @property
    def summary(self):
        pass

    def __str__(self):
        return f"{self.id}: {self.summary}"
