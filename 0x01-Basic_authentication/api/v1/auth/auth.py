#!/usr/bin/env python3
"""module that contains the authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """authentication class"""
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns a path"""
        if path is not None and excluded_paths is not None:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """handles the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets the current user"""
        return None
