"""
Authentication Controller Module

This module exposes functions for handling authentication requests.
It acts as the interface between the API layer and the service layer.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.auth_service import AuthService
from typing import Dict, Any


class AuthController:
    """
    Controller class for authentication endpoints.
    Handles incoming requests and delegates to the service layer.
    """

    def __init__(self):
        """Initialize the controller with the authentication service."""
        self.auth_service = AuthService()

    def login(self, email: str, password: str) -> Dict[str, Any]:
        """
        Handle user login request.

        Args:
            email: User's email address
            password: User's password

        Returns:
            Dictionary containing:
            - success: Boolean indicating if login was successful
            - token: JWT token if successful
            - message: Success or error message
            - status_code: HTTP status code
        """
        print(f"[Controller] Processing login request for: {email}")
        
        success, token, message = self.auth_service.authenticate_user(email, password)
        
        if success:
            return {
                "success": True,
                "token": token,
                "message": message,
                "status_code": 200
            }
        else:
            return {
                "success": False,
                "token": None,
                "message": message,
                "status_code": 401
            }

    def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Validate a JWT token.

        Args:
            token: JWT token to validate

        Returns:
            Dictionary containing:
            - success: Boolean indicating if token is valid
            - user: User data if valid
            - message: Success or error message
            - status_code: HTTP status code
        """
        print("[Controller] Validating token")
        
        valid, user_data, message = self.auth_service.validate_token(token)
        
        if valid:
            return {
                "success": True,
                "user": user_data,
                "message": message,
                "status_code": 200
            }
        else:
            return {
                "success": False,
                "user": None,
                "message": message,
                "status_code": 401
            }

    def reset_password(self, email: str, old_password: str, new_password: str) -> Dict[str, Any]:
        """
        Handle password reset request.

        Args:
            email: User's email address
            old_password: Current password
            new_password: New password to set

        Returns:
            Dictionary containing:
            - success: Boolean indicating if reset was successful
            - message: Success or error message
            - status_code: HTTP status code
        """
        print(f"[Controller] Processing password reset for: {email}")
        
        success, message = self.auth_service.reset_password(email, old_password, new_password)
        
        if success:
            return {
                "success": True,
                "message": message,
                "status_code": 200
            }
        else:
            return {
                "success": False,
                "message": message,
                "status_code": 400
            }

    def request_password_reset(self, email: str) -> Dict[str, Any]:
        """
        Handle password reset request (generates reset token).

        Args:
            email: User's email address

        Returns:
            Dictionary containing:
            - success: Boolean indicating if request was successful
            - reset_token: Reset token if successful
            - message: Success or error message
            - status_code: HTTP status code
        """
        print(f"[Controller] Processing password reset request for: {email}")
        
        success, reset_token, message = self.auth_service.request_password_reset(email)
        
        return {
            "success": success,
            "reset_token": reset_token,
            "message": message,
            "status_code": 200 if success else 400
        }

    def get_user_profile(self, email: str) -> Dict[str, Any]:
        """
        Get user profile information.

        Args:
            email: User's email address

        Returns:
            Dictionary containing:
            - success: Boolean indicating if user was found
            - user: User data if found
            - message: Success or error message
            - status_code: HTTP status code
        """
        print(f"[Controller] Fetching profile for: {email}")
        
        user_info = self.auth_service.get_user_info(email)
        
        if user_info:
            return {
                "success": True,
                "user": user_info,
                "message": "User profile retrieved successfully",
                "status_code": 200
            }
        else:
            return {
                "success": False,
                "user": None,
                "message": "User not found",
                "status_code": 404
            }

    def logout(self, token: str) -> Dict[str, Any]:
        """
        Handle user logout (in a real app, this would invalidate the token).

        Args:
            token: JWT token to invalidate

        Returns:
            Dictionary containing:
            - success: Boolean (always True for this demo)
            - message: Success message
            - status_code: HTTP status code
        """
        print("[Controller] Processing logout request")
        
        # In a real application, you would:
        # 1. Add token to a blacklist
        # 2. Remove from active sessions
        # 3. Clear any cached data
        
        return {
            "success": True,
            "message": "Logged out successfully",
            "status_code": 200
        }

# Made with Bob
