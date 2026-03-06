"""
JWT Utility Module

This module provides functions for generating fake JWT tokens.
In a real application, this would use a proper JWT library like PyJWT.
"""

import base64
import json
import time
from typing import Dict, Any


class JWTUtil:
    """
    Utility class for JWT token operations.
    Simulates JWT token generation without actual cryptographic signing.
    """

    def __init__(self, secret_key: str = "demo_secret_key_12345"):
        """
        Initialize the JWT utility.

        Args:
            secret_key: Secret key for token generation (not used in this demo)
        """
        self.secret_key = secret_key

    def generate_token(self, user_id: str, email: str, expiry_hours: int = 24) -> str:
        """
        Generate a fake JWT token for a user.

        Args:
            user_id: The user's unique identifier
            email: The user's email address
            expiry_hours: Token expiry time in hours (default: 24)

        Returns:
            A fake JWT token string
        """
        # Create header
        header = {
            "alg": "HS256",
            "typ": "JWT"
        }

        # Create payload
        current_time = int(time.time())
        expiry_time = current_time + (expiry_hours * 3600)
        
        payload = {
            "user_id": user_id,
            "email": email,
            "iat": current_time,  # Issued at
            "exp": expiry_time    # Expiry time
        }

        # Encode header and payload (simplified, not actual JWT)
        header_encoded = self._base64_encode(json.dumps(header))
        payload_encoded = self._base64_encode(json.dumps(payload))
        
        # Create a fake signature (in real JWT, this would be cryptographically signed)
        signature = self._create_fake_signature(header_encoded, payload_encoded)

        # Combine to create token
        token = f"{header_encoded}.{payload_encoded}.{signature}"
        
        return token

    def _base64_encode(self, data: str) -> str:
        """
        Base64 encode a string.

        Args:
            data: String to encode

        Returns:
            Base64 encoded string
        """
        encoded = base64.urlsafe_b64encode(data.encode()).decode()
        # Remove padding for JWT format
        return encoded.rstrip('=')

    def _create_fake_signature(self, header: str, payload: str) -> str:
        """
        Create a fake signature for demonstration purposes.

        Args:
            header: Encoded header
            payload: Encoded payload

        Returns:
            Fake signature string
        """
        # In a real JWT, this would be HMAC-SHA256(header.payload, secret_key)
        combined = f"{header}{payload}{self.secret_key}"
        fake_signature = base64.urlsafe_b64encode(combined.encode())[:43].decode()
        return fake_signature.rstrip('=')

    def decode_token(self, token: str) -> Dict[str, Any]:
        """
        Decode a JWT token (simplified version).

        Args:
            token: The JWT token to decode

        Returns:
            Dictionary containing the decoded payload

        Raises:
            ValueError: If token format is invalid
        """
        try:
            parts = token.split('.')
            if len(parts) != 3:
                raise ValueError("Invalid token format")

            # Decode payload
            payload_encoded = parts[1]
            # Add padding if needed
            padding = 4 - (len(payload_encoded) % 4)
            if padding != 4:
                payload_encoded += '=' * padding

            payload_json = base64.urlsafe_b64decode(payload_encoded).decode()
            payload = json.loads(payload_json)

            return payload
        except Exception as e:
            raise ValueError(f"Failed to decode token: {str(e)}")

    def is_token_expired(self, token: str) -> bool:
        """
        Check if a token is expired.

        Args:
            token: The JWT token to check

        Returns:
            True if token is expired, False otherwise
        """
        try:
            payload = self.decode_token(token)
            expiry_time = payload.get('exp', 0)
            current_time = int(time.time())
            return current_time > expiry_time
        except ValueError:
            return True

# Made with Bob
