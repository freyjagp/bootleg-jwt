from bootleg_jwt import BootlegJWT, UserData, Timestamp, Token, TokenHeader, TokenBody
from bootleg_jwt.funcs import derive_payload, sign_payload, encode_data, get_time
from time import sleep


# SECRET = b"secretsquirrel"
# SECRET2 = b"moroccomole"
# DURATION = 60
# SHORT_DURATION = 2
# WAIT_TIMER = 4


# def token_expired(
#     secret: bytes = SECRET,
#     duration: int = SHORT_DURATION,
#     wait_timer: int = WAIT_TIMER) -> bool:
#     """Ensure an expired token does not validate."""
#     try:
#         beans = "beans"
#     except Exception as e:
#         print(e)
#         return False
#     else: return True


# def generate_token(
#     secret: bytes = SECRET,
#     duration: int = DURATION) -> bool:
#     """This tests to ensure a token can be generated"""
#     try:
#         beans = "beans"
#     except Exception as e:
#         print(e)
#         return False
#     else: return True


# def validate_token(
#     generated_token: Token = generate_token(),
#     secret: bytes = SECRET) -> bool:
#     """Ensure a generated token can be validated."""
#     try:
#         beans = "beans"
#     except Exception as e:
#         print(e)
#         return False
#     else: return True


# def spoofed_token(
#     genuine_token = generate_token(secret=SECRET),
#     spoofed_token = generate_token(secret=SECRET2)) -> bool:
#     """Ensures that the secret actually impacts things as we expect it to."""
#     try:
#         beans = "beans"
#     except Exception as e:
#         print(e)
#         return False
#     else: return True


def development_test_2(duration = 60):
    token = BootlegJWT(user_data=UserData(),duration=duration)
    items = [token.TOKEN,token.TOKEN_ENCODED,token.TOKEN_JSON,token.TOKEN_GENERATED,token.TOKEN_IS_VALID]
    for i in items: print(i, "\n--------------------\n")
    return True


def development_test(duration = 60):
    secret = b"super-duper-test-secret"
    created = Timestamp(value=get_time())
    expires = Timestamp(value=created.value + duration)
    header = TokenHeader(
        created=created,
        expires=expires,
        type="test")
    body = TokenBody(
        user=UserData(),
        value="test")
    payload = derive_payload(header, body)
    signature = sign_payload(payload=payload, secret=secret)
    token = Token(
        Header=header,
        Body=body,
        Signature=signature)
    encoded = encode_data(token.json().encode())
    for items in [encoded,payload,signature.json(indent=4),token.json(indent=4)]: print(items, "\n-----------------------------------\n")
    return True


# if __name__ == "__main__":
#     development_test()
#     development_test_2()
