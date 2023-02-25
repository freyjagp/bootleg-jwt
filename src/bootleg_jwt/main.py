from .schema import Token, Payload
from .funcs import encode_token, decode_token, derive_payload, sign_payload, get_time
from .messages import *


from decouple import config


class BootlegJWT():
    VALID: bool = False
    TOKEN: Token = False
    ENCODED: bytes = False
    DECODED: Token = False
    JSON: Token.json = False


    def __init__(
        self,
        token: bytes = False,
        payload: Payload = False,
    ):
        _secret = config('SECRET').encode()
        if not token and not payload: raise Exception(ERROR_INVALID_USE)
        if payload: self.generate(payload, _secret)
        if token: token = decode_token(token)
        if token: self.validate(token, _secret)


    def generate(self,
        payload: Payload,
        _secret=b''
    ):
        signature = sign_payload(payload, _secret)
        _token: Token = Token(header=payload.header,body=payload.body,signature=signature)
        self.TOKEN = _token
        self.JSON = _token.json(indent=4)
        self.ENCODED = encode_token(_token)
        valid = self.validate(_token,_secret)
        if valid: self.VALID = True

    def validate(self, token: Token, _secret=b''):
        is_valid = False
        expired = True if get_time() > token.header.expires.value else False
        if expired: return False
        payload = derive_payload(token)
        signature = sign_payload(payload, _secret)
        token_signature = token.signature.value
        payload_signature = signature.value
        if token_signature.decode() == payload_signature.decode(): is_valid = True

        if is_valid:
            self.VALID = True
            self.DECODED = token
            self.JSON = token.json(indent=4)
