#!/usr/bin/env python3
"""module that contains the session authentication class
"""
from .auth import Auth


class SessionAuth(Auth):
    """the session authentication class"""
    def __init__(self) -> None:
        super().__init__()
