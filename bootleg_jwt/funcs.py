from .schema import Hash, TokenHeader, TokenBody
from .messages import ERROR_TYPE_INVALID
from typing import List
from time import time
from base64 import b64encode
from hashlib import blake2b


def get_time() -> int:
    """Return the current unix epoch.

    Returns:
        int: Current time in seconds since unix epoch (01/01/1970 at 00:00)
    """
    return int(time())


def concat_bytestrings(items: list, delimiter: bytes = b'.') -> bytes:
    """Concatenate a list of base64 bytestrings, delimited by a period.

    Args:
        items (list): a list of base64 bytestrings.
        delimiter (bytes, optional): Option to set delimiter. Defaults to b'.'.

    Raises:
        TypeError: If items are not bytestring.

    Returns:
        bytes: base64 encoded bytestrings concatenated by a period.
    """
    concat = b''
    for i in items:
        if not isinstance(i,bytes): raise TypeError(ERROR_TYPE_INVALID)
        concat = i if concat == b'' else concat + delimiter + i
    return concat


def encode_concat(items: List[bytes]) -> bytes:
    """Encode a series of items using encode_data(), then concactenate with periods and return as a single bytestring.

    Args:
        items (List[bytes]): A list of bytestrings to be encoded.

    Returns:
        bytes: The supplied data, encoded in base64 and concatenated by periods.
    """
    encoded = []
    for i in items: encoded.append(encode_data(i))
    return concat_bytestrings(encoded)


def encode_data(data: bytes) -> bytes:
    """Encodes supplied data in bytes as base64.

    Args:
        data (bytes): data to be encoded.

    Raises:
        TypeError: if data is not bytes.

    Returns:
        bytes: returns base64 encoded bytestring.
    """
    if not isinstance(data, bytes): raise TypeError(ERROR_TYPE_INVALID)
    return b64encode(data)


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
        bytes: _description_
    """
    return blake2b(data,key=secret_key,person=person,salt=salt).hexdigest().encode()


def sign_payload(payload: bytes, secret: bytes, person=b'', salt=b'') -> Hash:
    """Signs a payload with a secret using blake2b. Optional values person and salt may be used for namespacing and randomization.

    Args:
        payload (bytes): payload is defined by derive_payload() as two base64 bytestrings concatenated with a period.
        secret (bytes): A secret password only the machine knows. Prevents spoofing of tokens.
        person (bytes, optional): A small bytestring used to namespace hashes. Defaults to empty.
        salt (bytes, optional): A small bytestring used to salt hashes. Defaults to empty.

    Returns:
        Hash: pytantic schema found in schema.py.
    """
    signed = blake2bhash(payload,secret_key=secret,person=person,salt=salt)
    person = person if person else False
    salt = salt if salt else False
    return Hash(value=signed,keyed=True,person=person,salt=salt)


def derive_payload(header: TokenHeader, body: TokenBody) -> bytes:
    """Derive the payload from a token's header and body.

    Args:
        header (TokenHeader): TokenHeader pytantic schema found in schema.py.
        body (TokenBody): TokenBody pytantic schema found in schema.py.

    Returns:
        bytes: two base64 bytestrings concatenated with a period.
    """
    return encode_concat([header.json().encode(),body.json().encode()])

