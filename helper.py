import jwt


def decode_token(token):
    decoded_token = jwt.decode(jwt=token, algorithms=["RS256"], options={
                               "verify_signature": False
                               })
    return decoded_token
