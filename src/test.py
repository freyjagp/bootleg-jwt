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
token2 = BootlegJWT(payload=payload2)


print(token.JSON, token.VALID)
print(token2.TOKEN, token2.VALID)


validate1 = BootlegJWT(token.ENCODED)
validate2 = BootlegJWT(token2.ENCODED)
print(validate1.VALID, validate2.VALID)


sleep(3)


validate1 = BootlegJWT(token.ENCODED)
validate2 = BootlegJWT(token2.ENCODED)
print(validate1.VALID, validate2.VALID)




