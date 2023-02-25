from bootleg_jwt import BootlegJWT, Payload, body, header

from time import sleep

payload1 = Payload(
    header = header(duration=5),
    body = body(user="some user",data="some data")
)
payload2 = Payload(
    header = header(duration=2),
    body = body(user="some user 1",data="some data 1")
)

token = BootlegJWT(payload=payload1)

print(token.JSON, token.VALID)

token2 = BootlegJWT(payload=payload2)
print(token2.TOKEN, token2.VALID)
sleep(3)

validate = BootlegJWT(token2.ENCODED)



print(token2.JSON, validate.VALID, validate.DECODED)