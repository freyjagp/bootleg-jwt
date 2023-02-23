# bootleg-jwt

`bootleg-jwt` aims to mimic JSON Web Tokens.

You can use this module to generate tokens, and validate them.

<!-- # bootleg-jwt

`bootleg-jwt` is a python module that implements the bare minimum of the JWT concept, with zero regard for its actual specification. It utilizes the blake2 hashing algorithm, a secret stored in a .env file, and very simple logic to encode/decode a small set of data into a bytestring that can then be used for stateless client validation.

this is more of a proof of concept, then valid production code. Integrate at your own risk. This is for learning purposes, mainly.

the idea is simple: If we can utilize a keyed hashing algorithm, and a set of data, we may securely authenticate that data so long as they key remains secret.

Abstractly, this means we may take, say, a generic header, a generic token, combine those, hash them, append the hash, and send it. The data contained within the token and header may not be altered in any way, or they will produce a dramatically different hash. Furthermore, the hash cannot be spoofed, unless an attacker knows the key which was used to hash the data in the first place. Therefore, the data is always secure, so long as nobody decides to mess with it. If someone *does* mess with it, then it will simply not validate.

This project does that.

We utilize the `blake2` hashing algorithm, which has the option to hash with or without a key. We establish a secret, stored in a `.env` file (see repository). Then we build our very simple program, and expose its functionality through `__init__.py`. From there, one may import (`from bootleg_jwt import TokenData, BootlegJWT`) the necessary classes to use it.

## Create a token

To create a token, use the imported `TokenData` class. It is a pydantic model. You may create a token in one line: `token = BootlegJWT(data=TokenData(id=1,username="baldur",duration=60*60))`

__NOTE:__ duration is always in seconds.

This produces a bytestring. This bytestring is actually three things:

1. a `base64` encoded json header
2. a `base64` encoded json token
3. a `blake2` hash generated using the header, the token, and our `SECRET`

This verifies the integrity of the data, and prevents tampering. The token contains a duration, which must not have elapsed for the token to remain valid. Any tampering will drastically alter the hash. And a valid hash cannot be generated without the secret. Therefore, this provides a secure stateless authentication token.

## Validate a token

Simply use `BootlegJWT(token=b'not.a.realtoken').TOKEN_IS_VALID`. This will take in a token, check if its valid, and return a bool. If the token is valid, the instance also produces `TOKEN`, which is an easy to parse pydantic model defined in class `HumanReadable`.

## Requirements

`pip install pydantic python-decouple`

## Conclusion

This is just a proof of concept. I offer no warranty. Use at your own volition, and do not integrate this directly into production code. Feel free to fork it, open issues, prs, etc. I might check in and respond. Who knows.

This kinda just helped me learn how JWTs work (and despite my warning, is being used in a private project which I may someday expose to the public). If you have any suggestions for improvement, I'm happy to hear them.

- Freyja -->
