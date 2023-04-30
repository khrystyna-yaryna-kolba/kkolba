from drf_yasg import openapi
from .swagger import unauthorized_401

logout_schema = openapi.Schema(
    title="logout",
    type=openapi.TYPE_OBJECT,
    properties={
        "refresh_token": openapi.Schema(type= openapi.TYPE_STRING, description="refresh token to be blacklisted",
                                        example="jknJj93nc4JN8ssn38JHBfjJ7dnHJ4hUJ4h")
    }
)
response_login = {
    "401": openapi.Response(
        description="invalid email or password",
        examples={
            "application/json": {
                "detail": "No active account found with the given credentials"
            }
        }),
    "200": openapi.Response(
        description="Login was successful",
        examples={
            "application/json":
                {
                    "refresh": "eyJhbI6IkpXVCJ5_nu_A8IZIeZ0x1WJq8X9AISLA4",
                    "access": "eyOjE2NjgzpczASEhgbG6uuhmmkjj8SbFeaumOxyuk"
                }
        }),
}
response_refresh_token = {
    "401": openapi.Response(
        description="invalid token or invalid token type",
        examples={
            "application/json": {
                "detail": "Token is invalid or expired",
                "code": "token_not_valid"
}
        }),
    "201": openapi.Response(
        description="Get new access token",
        examples={
            "application/json":
                {
                    "access": "eyOjE2NjgzpczASEhgbG6uuhmmkjj8SbFeaumOxyuk"
                }
        }),
}
logout_response = {
    "200": openapi.Response(
        description="successfully logged out",
        examples={
            "application/json":
                {
                    "detail": "Successfully logged out"
                }
        }),
    #"401": unauthorized_401,
    "400": openapi.Response(
        description="invalid refresh token in request",
        examples={
            "application/json":
                {
                    "detail": "Token is invalid or expired"
                }
        })
}
register_response = {
    "201": openapi.Response(
        description="successfully registered",
        examples={
            "application/json":
                {
                    "id": 5,
                    "email": "test2@email.com",
                    "first_name": "Mary",
                    "last_name": "Watson",
                    "password": "pbkdf2_sha256$390000$IW8Bnc2qEsYnRJOFC9cCJ6$gF9yJi8cfkTq4WKdB8BN32w8tW9tmBUEf+tw8Bt/9Pk="
                }
        }
    ),
    "400": openapi.Response(
        description="invalid user data",
        examples={
            "application/json":
                {
                    "email": [
                        "user with this email already exists."
                    ],
                    "password": [
                        "Password should contain at least one uppercase letter, one lowercase letter and be at least 8 symbols long"
                    ]
                }
        })
}