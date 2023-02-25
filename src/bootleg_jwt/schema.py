from pydantic import BaseModel
from typing import Any


class Unit(BaseModel):
    type: str = "time"
    name: str = "seconds"
    shorthand: str = "s"


class Timestamp(BaseModel):
    unit: Unit = Unit(name="seconds since epoch",shorthand="s+epoch")
    value: int


class Duration(BaseModel):
    unit: Unit = Unit()
    value: int = 60

class Header(BaseModel):
    type: str = "Default Token Type"
    duration: Duration
    created: Timestamp
    expires: Timestamp


class Body(BaseModel):
    user: Any = "USER"
    data: Any = "BODY"


class Payload(BaseModel):
    header: Header
    body: Body

class Hash(BaseModel):
    value: bytes = b''
    algorithm: str = "blake2b"
    keyed: bool = False
    salt: bytes = b''
    person: bytes = b''


class Token(BaseModel):
    header: Header
    body: Body
    signature: Hash


