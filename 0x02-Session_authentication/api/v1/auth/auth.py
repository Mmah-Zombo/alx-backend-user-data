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
        if (path is None):
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        stri = f"{path}/"
        if path in excluded_paths or stri in excluded_paths:
            return False
        for each in excluded_paths:
            if each.endswith('*'):
                each2 = each[:-1]
                if path.startswith(each2):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """handles the authorization header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """gets the current user"""
        return None
