from .schema import Hash, Token, Payload, Header, Timestamp, Body, Duration
from .messages import ERROR_INVALID_TYPE
from pydantic import ValidationError
from time import time
from base64 import b64encode, b64decode
from hashlib import blake2b
from binascii import Error


def header(duration,type = "Default"):
    time = get_time()
    return Header(duration=Duration(value=duration),type=type,created=Timestamp(value=time),expires=Timestamp(value=time+duration))


def body(user,data):
    return Body(user=user,data=data)


def blake2bhash(
    data: bytes,
    secret_key: bytes = b'',
    person: bytes = b'',
    salt: bytes = b'') -> bytes:
    """hashlib.blake2b.

    Args:
        data (bytes): Data to be hashed.
        secret_key (bytes, optional): A secret key. Can be used to turn hashes into signatures. Defaults to empty.
        person (bytes, optional): A small bytestring used to namespace hashes. Defaults to empty.
        salt (bytes, optional): A small bytestring used to salt hashes. Defaults to empty.

    Returns:
        bytes: utf-8 encoded hex digest
    """
    return blake2b(data,key=secret_key,person=person,salt=salt).hexdigest().encode()


def decode_token(token: bytes):
    try:
        if not isinstance(token, bytes): raise TypeError(ERROR_INVALID_TYPE)
        token = b64decode(token)
        parsed = Token.parse_raw(token)
    except ValidationError or TypeError or Error:
        return False
    else: return parsed


def derive_payload(token: Token):
    payload = Payload(
        header=token.header,
        body=token.body)
    return payload


def encode_token(token: Token):
    return b64encode(token.json().encode())


def encode_payload(payload: Payload):
    return b64encode(payload.header.json().encode() + b'.' + payload.body.json().encode())


def sign_payload(payload: Payload, _secret: bytes, _salt=b'', _person=b''):
    signature = blake2bhash(data=encode_payload(payload),secret_key=_secret,person=_person,salt=_salt)
    signature = Hash(value=signature,keyed=True)
    return signature


def get_time() -> int:
    """Return the current unix epoch.

    Returns:
        int: Current time in seconds since unix epoch (01/01/1970 at 00:00)
    """
    return int(time())