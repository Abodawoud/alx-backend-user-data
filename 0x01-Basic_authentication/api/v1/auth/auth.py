#!/usr/bin/env python3
"""
Auth module for API
"""
from typing import TypeVar
from flask import request
from typing import List
from typing import TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization Header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        return None
