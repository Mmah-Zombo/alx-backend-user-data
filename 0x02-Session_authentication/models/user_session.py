#!/usr/bin/env python3
"""model for the user sessions"""
from models.base import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship


class UserSession(Base):
    """the user session class"""
    __tablename__ = 'user_sessions'

    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)

    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
