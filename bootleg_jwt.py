import base64
from time import time
from hashlib import blake2b
from pydantic import BaseModel
from json import dumps, loads
from decouple import config

class Token(BaseModel):
    id: int
    name: str
    init: int
    exp: int


class Header(BaseModel):
    alg: str = "blake2b"
    typ: str = "FWT"


class Data(BaseModel):
    header: bytes
    token: bytes
    hash: bytes
    received: int


class HumanReadable(BaseModel):
    header: Header
    token: Token
    hash: bytes
    received: int


class TokenData(BaseModel):
    id: Token.id
    username: Token.name
    duration: int


def get_time():
    return int(time())


def get_data(encoded_token: bytes):
    z = encoded_token.split(b'.')
    a = z[0]
    b = z[1]
    c = z[2]
    t = get_time()
    return Data(header=a,token=b,hash=c,received=t)


def human_readable(data: Data) -> HumanReadable:
    header = data.header
    token = data.token
    hash = data.hash
    received = data.received
    header = loads(loads(base64.b64decode(header)))
    token = loads(loads(base64.b64decode(token)))
    header = Header(
        alg=header['alg'],
        typ=header['typ']
    )
    token = Token(
        id=token['id'],
        name=token['name'],
        init=token['init'],
        exp=token['exp']
    )
    return HumanReadable(header=header,token=token,hash=hash,received=received)


class BootlegJWT():


    TOKEN_IS_VALID = False


    def encode_token(self, token: Token, secret) -> bytes:
        a = base64.b64encode(dumps(self.HEADER.json(),ensure_ascii=True,indent=4).encode())
        b = base64.b64encode(dumps(token.json(),ensure_ascii=True,indent=4).encode())
        c = a + b'.' + b
        d = blake2b(c,key=secret).hexdigest().encode()
        return c + b'.' + d


    def validate_token(self, token: bytes, secret) -> HumanReadable | False:
        data: Data = get_data(token)
        if c != data.hash: return False
        b = data.header + b'.' + data.token
        c = blake2b(b,key=secret).hexdigest().encode()
        d = loads(loads(base64.b64decode(data.token)))
        if d['exp'] < d['init']: return False
        return True if data.received < d['exp'] else False


    def build_token(id: int, username: str, duration: int) -> Token:
        t = int(get_time())
        return Token(
            id=id,
            name=username,
            init=t,
            exp=int(t + duration)
        )


    def build_header(self) -> Header:
        return Header()


    def __init__(self, token_data: TokenData = False, token: Token = False):
        secret = config('SECRET')
        self.HEADER = self.build_header()
        if token_data: built = self.build_token(id=token_data.id,username=token_data.username,duration=token_data.duration)
        self.ENCODED_TOKEN = self.encode_token(built, secret)
        if token: self.TOKEN_IS_VALID = self.validate_token(token, secret)
        if self.TOKEN_IS_VALID: self.TOKEN = human_readable(get_data(token))