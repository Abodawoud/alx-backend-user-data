#!/usr/bin/env python3
"""
Auth module for API
"""
from typing import TypeVar
from flask import request
from typing import List
from typing import TypeVar


class Auth:
    """
        Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth"""
        if path is None:
            return True

        if excluded_paths is (None or []):
            return True

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.rstrip('/')):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        return None
