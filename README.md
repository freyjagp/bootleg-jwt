# bootleg-jwt <!-- omit in toc -->

`bootleg-jwt` aims to mimic JSON Web Tokens in a simple, `pydantic` way.

This module provides two main functions (soon, three):

- [Generate a token](#generate-a-token)
- [Validate a token](#validate-a-token)

___

## Usage <!-- omit in toc -->

There are two main uses, see below:

### Generate a token

```python
from bootleg_jwt import BootlegJWT, UserData, Token
from os import environ


DURATION = 60*60                    # Token expires after this many seconds


SECRET = "some-secret-key"


environ['SECRET'] = SECRET          # This module depends upon an environment
                                    # variable `SECRET`. You may also set this
                                    # secret in a `.env` file in your project's root,
                                    # or by using `export SECRET="secret"`


user_data = UserData(
    id = 1,
    uuid = b'some-uuid',
    name = 'Username')


generated = BootlegJWT(
    duration=DURATION,
    user_data=user_data,
    body_data=["some","arbitrary",["dataset"]])


token: Token = generated.TOKEN
encoded = generated.TOKEN_ENCODED
json = generated.TOKEN_JSON
validate: bool = generated.TOKEN_IS_VALID # should be true
was_generated: bool = generated.TOKEN_GENERATED # should be true


print(json)
```

<details>
<summary>Output (click to expand):</summary>
<br>

```json
{
    "Header": {
        "created": {
            "unit": [
                "Seconds since epoch",
                "s+epoch"
            ],
            "value": 1677224053
        },
        "expires": {
            "unit": [
                "Seconds since epoch",
                "s+epoch"
            ],
            "value": 1677224083
        },
        "type": "Default"
    },
    "Body": {
        "user": {
            "id": 1,
            "uuid": "some-uuid",
            "name": "Username"
        },
        "value": [
            "some",
            "arbitrary",
            [
                "dataset"
            ]
        ]
    },
    "Signature": {
        "value": "922201ceedf626eada3a4f4f44e36b190d2d5297aec43eb5bd58aafbce36db700a619ca50c584b5f585d87da634dfd473224826230e779b40d1ecb69d7f19ad7",
        "algorithm": "blake2b",
        "keyed": true,
        "salted": false,
        "person": false
    }
}
```

</details>
<br>
This is the json representation of our `Token` model. This is a pydantic model containing three pydantic models defined in `src/bootleg_jwt/schema.py`

- Note: Our `UserData` schema lives in here too, and may be easily adapted to change its parameters as one sees fit. This code does not necessairily provide _functionality_ as much as it is _easily modified_.

You may also call instance variable `TOKEN_ENCODED` to get a base64 encoded bytestring - perfect for storing as a cookie for later use.

```txt
eyJIZWFkZXIiOiB7ImNyZWF0ZWQiOiB7InVuaXQiOiBbIlNlY29uZHMgc2luY2UgZXBvY2giLCAicytlcG9jaCJdLCAidmFsdWUiOiAxNjc3MjI0NzgzfSwgImV4cGlyZXMiOiB7InVuaXQiOiBbIlNlY29uZHMgc2luY2UgZXBvY2giLCAicytlcG9jaCJdLCAidmFsdWUiOiAxNjc3MjI0ODEzfSwgInR5cGUiOiAiRGVmYXVsdCJ9LCAiQm9keSI6IHsidXNlciI6IHsiaWQiOiAxLCAidXVpZCI6ICJzb21lLXV1aWQiLCAibmFtZSI6ICJVc2VybmFtZSJ9LCAidmFsdWUiOiBbInNvbWUiLCAiYXJiaXRyYXJ5IiwgWyJkYXRhc2V0Il1dfSwgIlNpZ25hdHVyZSI6IHsidmFsdWUiOiAiM2I3ZjQ0MTA4ZjU1OWJjYmMyMWQ5NzQ3YTY2NGEyZjFjN2FiYmMxN2YyN2U4NDIyYjgwODIxNTNlYTE4M2MzNGE4NzhmM2Q3NjRlYTExZjE5NDFmN2M3MDUxNTM4MDgyYTdiYTRlYTBjYjFhYmI1OTVhNmU5ZGFiMTc4YmY5MjEiLCAiYWxnb3JpdGhtIjogImJsYWtlMmIiLCAia2V5ZWQiOiB0cnVlLCAic2FsdGVkIjogZmFsc2UsICJwZXJzb24iOiAiRmFsc2UifX0=
```

### Validate a token

See expansion of above:

```python
from bootleg_jwt import BootlegJWT, UserData, Token
from os import environ
from time import sleep


DURATION = 3                   # duration in seconds (one hour)


SECRET = "some-secret-key"


environ['SECRET'] = SECRET          # This module depends upon an environment
                                    # variable `SECRET`. You may also set this
                                    # secret in a `.env` file in your project's root,
                                    # or by using `export SECRET="secret"`


user_data = UserData(
    id = 1,
    uuid = b'some-uuid',
    name = 'Username')


generated = BootlegJWT(
    duration=DURATION,
    user_data=user_data,
    body_data=["some","arbitrary",["dataset"]])


token: Token = generated.TOKEN


# sleep(4)                      # See expiration in action.
                                # If 4 seconds pass on
                                # this 3 second token, it becomes invalid!
validate = BootlegJWT(token=token).TOKEN_IS_VALID


print(validate)
```

__Output:__ `True`

We can test expiration as well by uncommenting `sleep(4)` and watching the output change to `False`

### Decode a token <!-- omit in toc -->

So we can get the token encoded as base64 but that still requires work from the developer to actually decode that shit into a `Token` model before passing it. That's my bad. I overlooked this functionality and have discovered that it is necessary while writing the readme. Version 0.2.0 will address this issue.

## To-do

An ostensible list of things I may or may not add (idk, this is for a personal project, so don't count on it)

- Pass custom user_data schema
