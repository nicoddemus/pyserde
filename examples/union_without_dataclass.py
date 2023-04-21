from dataclasses import dataclass
from typing import Union

from serde import serde
from serde.json import from_json, to_json


@serde
@dataclass
class Bar:
    b: int


@serde
@dataclass
class Baz:
    b: int


f = Baz(10)
s = to_json(f, c=Union[Bar, Baz])
print(f)
print("serialized", s)
ff = from_json(Union[Bar, Baz], s)
print("deserialized", ff)
