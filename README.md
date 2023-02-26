# bootleg-jwt <!-- omit in toc -->

`bootleg-jwt` aims to mimic JSON Web Tokens in a simple, `pydantic` way.

This module provides two main functions:

- [Generate a token](#generate-a-token)
- [Validate a token](#validate-a-token)

These are designed to be very simple to use. See below:

## Generate a token

```python
from bootleg_jwt import BootlegJWT, Payload, header, body
from pydantic import BaseModel
from os import environ              # An environment variable is required.


SECRET = "some-secret-key"


DURATION = 60 * 60                  # Token expires after this many seconds


TYPE = "Testing Token"              # An arbitrary name


environ['SECRET'] = SECRET          # This module depends upon an environment
                                    # variable `SECRET`. You may also set this
                                    # secret in a `.env` file in your project's root,
                                    # or by using `export SECRET="secret"`



## These two pydantic models are simple examples. They may have arbitrary names and data. They must only map to Token.body.user and Token.body.data
class UserData(BaseModel):
    id: int
    username: str


class BodyData(BaseModel):
    info: str
    value: bool


payload_user = UserData(id=69,username="nice")
payload_body = BodyData(info="Some Information", value=True)


payload = Payload(
    header=header(duration=DURATION,type=TYPE),
    body=body(user=payload_user,data=payload_body)
)


generate = BootlegJWT(payload=payload)
token = generate.TOKEN
encoded = generate.ENCODED
json = generate.JSON
validate = generate.VALID
divider = "\n------------------------------\n"



print(token,divider,encoded,divider,json,divider,validate)
```

<details>
<summary>Output (click to expand):</summary>
<br>

```json
header=Header(type='Testing Token', duration=Duration(unit=Unit(type='time', name='seconds', shorthand='s'), value=3600), created=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677382369), expires=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677385969)) body=Body(user=UserData(id=69, username='nice'), data=BodyData(info='Some Information', value=True)) signature=Hash(value=b'e0b99c4eca2811bd9d164185219a283a4fddc2129ec0d2b3e5ba7b22596e4c7b8ac6d7b7c81812b50ace0a5b6d0be3ce5f977f753069d951bf15d13f179014df', algorithm='blake2b', keyed=True, salt=b'', person=b'')
------------------------------
 b'eyJoZWFkZXIiOiB7InR5cGUiOiAiVGVzdGluZyBUb2tlbiIsICJkdXJhdGlvbiI6IHsidW5pdCI6IHsidHlwZSI6ICJ0aW1lIiwgIm5hbWUiOiAic2Vjb25kcyIsICJzaG9ydGhhbmQiOiAicyJ9LCAidmFsdWUiOiAzNjAwfSwgImNyZWF0ZWQiOiB7InVuaXQiOiB7InR5cGUiOiAidGltZSIsICJuYW1lIjogInNlY29uZHMgc2luY2UgZXBvY2giLCAic2hvcnRoYW5kIjogInMrZXBvY2gifSwgInZhbHVlIjogMTY3NzM4MjM2OX0sICJleHBpcmVzIjogeyJ1bml0IjogeyJ0eXBlIjogInRpbWUiLCAibmFtZSI6ICJzZWNvbmRzIHNpbmNlIGVwb2NoIiwgInNob3J0aGFuZCI6ICJzK2Vwb2NoIn0sICJ2YWx1ZSI6IDE2NzczODU5Njl9fSwgImJvZHkiOiB7InVzZXIiOiB7ImlkIjogNjksICJ1c2VybmFtZSI6ICJuaWNlIn0sICJkYXRhIjogeyJpbmZvIjogIlNvbWUgSW5mb3JtYXRpb24iLCAidmFsdWUiOiB0cnVlfX0sICJzaWduYXR1cmUiOiB7InZhbHVlIjogImUwYjk5YzRlY2EyODExYmQ5ZDE2NDE4NTIxOWEyODNhNGZkZGMyMTI5ZWMwZDJiM2U1YmE3YjIyNTk2ZTRjN2I4YWM2ZDdiN2M4MTgxMmI1MGFjZTBhNWI2ZDBiZTNjZTVmOTc3Zjc1MzA2OWQ5NTFiZjE1ZDEzZjE3OTAxNGRmIiwgImFsZ29yaXRobSI6ICJibGFrZTJiIiwgImtleWVkIjogdHJ1ZSwgInNhbHQiOiAiIiwgInBlcnNvbiI6ICIifX0='
------------------------------
 {
    "header": {
        "type": "Testing Token",
        "duration": {
            "unit": {
                "type": "time",
                "name": "seconds",
                "shorthand": "s"
            },
            "value": 3600
        },
        "created": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677382369
        },
        "expires": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677385969
        }
    },
    "body": {
        "user": {
            "id": 69,
            "username": "nice"
        },
        "data": {
            "info": "Some Information",
            "value": true
        }
    },
    "signature": {
        "value": "e0b99c4eca2811bd9d164185219a283a4fddc2129ec0d2b3e5ba7b22596e4c7b8ac6d7b7c81812b50ace0a5b6d0be3ce5f977f753069d951bf15d13f179014df",
        "algorithm": "blake2b",
        "keyed": true,
        "salt": "",
        "person": ""
    }
}
------------------------------
 True
```

</details>
<br>

## Validate a token

```python
from bootleg_jwt import BootlegJWT, Payload, header, body
from pydantic import BaseModel
from os import environ              # An environment variable is required.


SECRET = "some-secret-key"


DURATION = 60 * 60                  # Token expires after this many seconds


TYPE = "Testing Token"              # An arbitrary name


environ['SECRET'] = SECRET          # This module depends upon an environment
                                    # variable `SECRET`. You may also set this
                                    # secret in a `.env` file in your project's root,
                                    # or by using `export SECRET="secret"`



## These two pydantic models are simple examples. They may have arbitrary names and data. They must only map to Token.body.user and Token.body.data
class UserData(BaseModel):
    id: int
    username: str


class BodyData(BaseModel):
    info: str
    value: bool


payload_user = UserData(id=69,username="nice")
payload_body = BodyData(info="Some Information", value=True)


payload = Payload(
    header=header(duration=DURATION,type=TYPE),
    body=body(user=payload_user,data=payload_body)
)


divider = "\n------------------------------\n"


def generate(payload):
    generate = BootlegJWT(payload=payload)
    decoded = generate.DECODED
    encoded = generate.ENCODED
    json = generate.JSON
    validate = generate.VALID
    print(decoded,divider,encoded,divider,json,divider,validate)
    return encoded


def validate_token(token):
    validate_token = BootlegJWT(token=token)
    v_decoded = validate_token.DECODED
    v_json = validate_token.JSON
    v_valid = validate_token.VALID
    print(v_decoded,divider,v_json,divider,v_valid)


validate_token(generate(payload))
```

<details>
<summary>Output (click to expand):</summary>
<br>

```json
header=Header(type='Testing Token', duration=Duration(unit=Unit(type='time', name='seconds', shorthand='s'), value=3600), created=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677383225), expires=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677386825)) body=Body(user=UserData(id=69, username='nice'), data=BodyData(info='Some Information', value=True)) signature=Hash(value=b'9a6a3fc5c866442ee886c1d20f44fe49da29be4e56fd6f40a1c3e23f672d801c0d787f9f239265477da1339fffc41754f16a0899f5955aa0ed7602693919071d', algorithm='blake2b', keyed=True, salt=b'', person=b'')
------------------------------
 b'eyJoZWFkZXIiOiB7InR5cGUiOiAiVGVzdGluZyBUb2tlbiIsICJkdXJhdGlvbiI6IHsidW5pdCI6IHsidHlwZSI6ICJ0aW1lIiwgIm5hbWUiOiAic2Vjb25kcyIsICJzaG9ydGhhbmQiOiAicyJ9LCAidmFsdWUiOiAzNjAwfSwgImNyZWF0ZWQiOiB7InVuaXQiOiB7InR5cGUiOiAidGltZSIsICJuYW1lIjogInNlY29uZHMgc2luY2UgZXBvY2giLCAic2hvcnRoYW5kIjogInMrZXBvY2gifSwgInZhbHVlIjogMTY3NzM4MzIyNX0sICJleHBpcmVzIjogeyJ1bml0IjogeyJ0eXBlIjogInRpbWUiLCAibmFtZSI6ICJzZWNvbmRzIHNpbmNlIGVwb2NoIiwgInNob3J0aGFuZCI6ICJzK2Vwb2NoIn0sICJ2YWx1ZSI6IDE2NzczODY4MjV9fSwgImJvZHkiOiB7InVzZXIiOiB7ImlkIjogNjksICJ1c2VybmFtZSI6ICJuaWNlIn0sICJkYXRhIjogeyJpbmZvIjogIlNvbWUgSW5mb3JtYXRpb24iLCAidmFsdWUiOiB0cnVlfX0sICJzaWduYXR1cmUiOiB7InZhbHVlIjogIjlhNmEzZmM1Yzg2NjQ0MmVlODg2YzFkMjBmNDRmZTQ5ZGEyOWJlNGU1NmZkNmY0MGExYzNlMjNmNjcyZDgwMWMwZDc4N2Y5ZjIzOTI2NTQ3N2RhMTMzOWZmZmM0MTc1NGYxNmEwODk5ZjU5NTVhYTBlZDc2MDI2OTM5MTkwNzFkIiwgImFsZ29yaXRobSI6ICJibGFrZTJiIiwgImtleWVkIjogdHJ1ZSwgInNhbHQiOiAiIiwgInBlcnNvbiI6ICIifX0='
------------------------------
 {
    "header": {
        "type": "Testing Token",
        "duration": {
            "unit": {
                "type": "time",
                "name": "seconds",
                "shorthand": "s"
            },
            "value": 3600
        },
        "created": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677383225
        },
        "expires": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677386825
        }
    },
    "body": {
        "user": {
            "id": 69,
            "username": "nice"
        },
        "data": {
            "info": "Some Information",
            "value": true
        }
    },
    "signature": {
        "value": "9a6a3fc5c866442ee886c1d20f44fe49da29be4e56fd6f40a1c3e23f672d801c0d787f9f239265477da1339fffc41754f16a0899f5955aa0ed7602693919071d",
        "algorithm": "blake2b",
        "keyed": true,
        "salt": "",
        "person": ""
    }
}
------------------------------
 True
header=Header(type='Testing Token', duration=Duration(unit=Unit(type='time', name='seconds', shorthand='s'), value=3600), created=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677383225), expires=Timestamp(unit=Unit(type='time', name='seconds since epoch', shorthand='s+epoch'), value=1677386825)) body=Body(user={'id': 69, 'username': 'nice'}, data={'info': 'Some Information', 'value': True}) signature=Hash(value=b'9a6a3fc5c866442ee886c1d20f44fe49da29be4e56fd6f40a1c3e23f672d801c0d787f9f239265477da1339fffc41754f16a0899f5955aa0ed7602693919071d', algorithm='blake2b', keyed=True, salt=b'', person=b'')
------------------------------
 {
    "header": {
        "type": "Testing Token",
        "duration": {
            "unit": {
                "type": "time",
                "name": "seconds",
                "shorthand": "s"
            },
            "value": 3600
        },
        "created": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677383225
        },
        "expires": {
            "unit": {
                "type": "time",
                "name": "seconds since epoch",
                "shorthand": "s+epoch"
            },
            "value": 1677386825
        }
    },
    "body": {
        "user": {
            "id": 69,
            "username": "nice"
        },
        "data": {
            "info": "Some Information",
            "value": true
        }
    },
    "signature": {
        "value": "9a6a3fc5c866442ee886c1d20f44fe49da29be4e56fd6f40a1c3e23f672d801c0d787f9f239265477da1339fffc41754f16a0899f5955aa0ed7602693919071d",
        "algorithm": "blake2b",
        "keyed": true,
        "salt": "",
        "person": ""
    }
}
------------------------------
 True


```
