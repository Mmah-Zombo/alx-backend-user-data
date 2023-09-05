#!/usr/bin/env python3
"""module that contains the basic authentication class
"""
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
