from pydantic import BaseModel
from typing import Any, List


class Timestamp(BaseModel):
    unit: List[str] = ["Seconds since epoch", "s+epoch"]
    value: int


class UserData(BaseModel):
    id: int = 0
    uuid: bytes = b'00000000'
    name: str = "DEFAULT"


class Hash(BaseModel):
    value: bytes
    algorithm: str = "blake2b"
    keyed: bool = False
    salted: str = False
    person: str = False


class TokenHeader(BaseModel):
    created: Timestamp
    expires: Timestamp
    type: str = "bootlegjwt"


class TokenBody(BaseModel):
    user: UserData
    value: Any


class Token(BaseModel):
    Header: TokenHeader
    Body: TokenBody
    Signature: Hash


