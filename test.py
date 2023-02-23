from bootleg_jwt import BootlegJWT, UserData, Timestamp, Token, TokenHeader, TokenBody
from bootleg_jwt.funcs import derive_payload, sign_payload, encode_data, get_time

def test_two(duration = 60):
    token = BootlegJWT(user_data=UserData(),duration=duration)
    items = [token.TOKEN,token.TOKEN_ENCODED,token.TOKEN_JSON,token.TOKEN_GENERATED,token.TOKEN_IS_VALID]
    for i in items: print(i, "\n--------------------\n")


def test(duration = 60):
    created = Timestamp(value=get_time())
    expires = Timestamp(value=created.value + duration)
    header = TokenHeader(
        created=created,
        expires=expires,
        type="test")
    body = TokenBody(
        user=UserData(),
        value="test")
    secret = b"super-duper-test-secret"
    payload = derive_payload(header, body)
    signed_payload = sign_payload(payload=payload, secret=secret)
    hash = signed_payload
    token = Token(
        Header=header,
        Body=body,
        Signature=hash)
    encoded = encode_data(token.json().encode())
    returns = [encoded,payload,signed_payload.json(indent=4),token.json(indent=4)]
    for items in returns:
        print("------------------")
        print(items)
    return


if __name__ == "__main__":
    test()
    test_two()


