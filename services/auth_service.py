"""
Authentication Service Module

This module contains the business logic for user authentication.
It validates credentials, generates tokens, and handles password resets.
"""

from repositories.user_repository import UserRepository
from utils.jwt_util import JWTUtil
from typing import Optional, Dict, Tuple


class AuthService:
    """
    Service class for authentication operations.
    Contains business logic for login, token generation, and password management.
    """

    def __init__(self):
        """Initialize the authentication service with required dependencies."""
        self.user_repository = UserRepository()
        self.jwt_util = JWTUtil()

    def authenticate_user(self, email: str, password: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Authenticate a user with email and password.

        Args:
            email: User's email address
            password: User's password

        Returns:
            Tuple of (success, token, message)
            - success: Boolean indicating if authentication was successful
            - token: JWT token if successful, None otherwise
            - message: Success or error message
        """
        # Validate input
        if not email or not password:
            return False, None, "Email and password are required"

        # Find user
        user = self.user_repository.find_by_email(email)
        
        if not user:
            return False, None, "Invalid email or password"

        # Verify password (in production, use proper password hashing)
        if user["password"] != password:
            return False, None, "Invalid email or password"

        # Generate token
        token = self.jwt_util.generate_token(
            user_id=user["user_id"],
            email=user["email"]
        )

        return True, token, f"Welcome back, {user['name']}!"

    def validate_token(self, token: str) -> Tuple[bool, Optional[Dict], Optional[str]]:
        """
        Validate a JWT token.

        Args:
            token: JWT token to validate

        Returns:
            Tuple of (valid, user_data, message)
            - valid: Boolean indicating if token is valid
            - user_data: User data if valid, None otherwise
            - message: Success or error message
        """
        try:
            # Check if token is expired
            if self.jwt_util.is_token_expired(token):
                return False, None, "Token has expired"

            # Decode token
            payload = self.jwt_util.decode_token(token)
            
            # Get user_id from payload
            user_id = payload.get("user_id")
            if not user_id:
                return False, None, "Invalid token: missing user_id"
            
            # Get user from repository
            user = self.user_repository.find_by_user_id(user_id)
            
            if not user:
                return False, None, "User not found"

            # Return user data without password
            user_data = {
                "user_id": user["user_id"],
                "email": user["email"],
                "name": user["name"]
            }

            return True, user_data, "Token is valid"

        except (ValueError, KeyError, TypeError) as e:
            return False, None, f"Invalid token: {str(e)}"
        except Exception as e:
            return False, None, f"Token validation error: {str(e)}"

    def reset_password(self, email: str, old_password: str, new_password: str) -> Tuple[bool, Optional[str]]:
        """
        Reset a user's password.

        Args:
            email: User's email address
            old_password: Current password
            new_password: New password to set

        Returns:
            Tuple of (success, message)
            - success: Boolean indicating if password reset was successful
            - message: Success or error message
        """
        # Validate input
        if not email or not old_password or not new_password:
            return False, "All fields are required"

        if len(new_password) < 8:
            return False, "New password must be at least 8 characters long"

        # Find user
        user = self.user_repository.find_by_email(email)
        
        if not user:
            return False, "User not found"

        # Verify old password
        if user["password"] != old_password:
            return False, "Current password is incorrect"

        # Check if new password is different
        if old_password == new_password:
            return False, "New password must be different from current password"

        # Update password
        success = self.user_repository.update_password(email, new_password)
        
        if success:
            return True, "Password reset successfully"
        else:
            return False, "Failed to reset password"

    def request_password_reset(self, email: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Request a password reset (generates a reset token).

        Args:
            email: User's email address

        Returns:
            Tuple of (success, reset_token, message)
            - success: Boolean indicating if request was successful
            - reset_token: Reset token if successful, None otherwise
            - message: Success or error message
        """
        # Validate input
        if not email:
            return False, None, "Email is required"

        # Check if user exists
        if not self.user_repository.user_exists(email):
            # For security, don't reveal if email exists
            return True, None, "If the email exists, a reset link will be sent"

        # Generate a reset token (valid for 1 hour)
        user = self.user_repository.find_by_email(email)
        
        # This should not happen since we checked user_exists, but add safety check
        if not user:
            return False, None, "User not found"
        
        reset_token = self.jwt_util.generate_token(
            user_id=user["user_id"],
            email=user["email"],
            expiry_hours=1
        )

        return True, reset_token, "Password reset token generated successfully"

    