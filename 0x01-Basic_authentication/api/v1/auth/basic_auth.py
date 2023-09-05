#!/usr/bin/env python3
"""module that contains the basic authentication class
"""
import base64
from .auth import Auth


class BasicAuth(Auth):
    """basic authentication class"""
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization
        header for a Basic Authentication:"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic'):
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header:"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            d_bytes = base64.b64decode(base64_authorization_header)
            d_string = d_bytes.decode('utf-8')
            return d_string
        except Exception:
            return None
