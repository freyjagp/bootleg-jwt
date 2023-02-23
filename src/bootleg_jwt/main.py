from .schema import Timestamp, UserData, Token, TokenBody, TokenHeader, Hash
from .funcs import derive_payload, sign_payload, get_time, encode_data
from typing import Any
from decouple import config


class BootlegJWT():
    TOKEN: Token = False
    TOKEN_ENCODED: bytes = False
    TOKEN_JSON: Token.json = False
    TOKEN_IS_VALID: bool = False
    TOKEN_GENERATED: bool = False


    def __init__(
        self,
        token: Token = False,
        user_data: UserData = False,
        body_data: Any = False,
        duration: int = 30,
    ):
        secret = config('SECRET').encode()
        if user_data: self.generate(user_data, body_data, duration, secret)
        if token: self.validate(token=token, secret=secret)
        if not token and not user_data: raise Exception("Invalid use of this module.")


    def generate(self, user_data: UserData, body_data: Any, duration: int, secret=b''):
        time = get_time()
        created = Timestamp(value=time)
        expires = Timestamp(value=time+duration)
        header = TokenHeader(
            created=created,
            expires=expires,
            type="Default")
        body = TokenBody(
            user=user_data,
            value=body_data)
        payload = derive_payload(header,body)
        signature: Hash = sign_payload(payload,secret)
        self.TOKEN = Token(
            Header=header,
            Body=body,
            Signature=signature)
        self.TOKEN_ENCODED = encode_data(self.TOKEN.json().encode())
        self.TOKEN_JSON = self.TOKEN.json(indent=4)
        self.TOKEN_GENERATED = True
        self.TOKEN_IS_VALID = self.validate(self.TOKEN,secret)


    def validate(self, token: Token, secret=b''):
        is_valid = False
        expired = True if get_time() > token.Header.expires.value else False
        if expired: return False
        payload = derive_payload(header=token.Header,body=token.Body)
        signature: Hash = sign_payload(payload=payload,secret=secret)
        token_signature = token.Signature.value
        payload_signature = signature.value
        if token_signature.decode() == payload_signature.decode(): is_valid = True
        if is_valid: self.TOKEN_IS_VALID = True


