#!/usr/bin/env python3
"""
Baisc_Auth module for API
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
        BasicAuth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """"
            extract base64 authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """"
            decode base64 authorization header
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(
                base64_authorization_header)  # base64 to bytes
            decoded_string = decoded_bytes.decode('utf-8')  # bytes to str
            return decoded_string
        except Exception as e:
            return None
