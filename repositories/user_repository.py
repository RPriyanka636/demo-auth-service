"""
User Repository Module

This module simulates database operations for user management.
In a real application, this would interact with a database.
"""

from typing import Optional, Dict, List


class UserRepository:
    """
    Repository class for managing user data.
    Simulates database operations using an in-memory dictionary.
    """

    def __init__(self):
        """Initialize the repository with sample users."""
        self._users: Dict[str, Dict[str, str]] = {
            "john.doe@example.com": {
                "email": "john.doe@example.com",
                "password": "password123",  # In production, this would be hashed
                "name": "John Doe",
                "user_id": "user_001"
            },
            "jane.smith@example.com": {
                "email": "jane.smith@example.com",
                "password": "securepass456",
                "name": "Jane Smith",
                "user_id": "user_002"
            },
            "admin@example.com": {
                "email": "admin@example.com",
                "password": "admin789",
                "name": "Admin User",
                "user_id": "user_003"
            }
        }

    def find_by_email(self, email: str) -> Optional[Dict[str, str]]:
        """
        Find a user by their email address.

        Args:
            email: The email address to search for

        Returns:
            User dictionary if found, None otherwise
        """
        return self._users.get(email)

    def find_by_user_id(self, user_id: str) -> Optional[Dict[str, str]]:
        """
        Find a user by their user ID.

        Args:
            user_id: The user ID to search for

        Returns:
            User dictionary if found, None otherwise
        """
        for user in self._users.values():
            if user.get("user_id") == user_id:
                return user
        return None

    def update_password(self, email: str, new_password: str) -> bool:
        """
        Update a user's password.

        Args:
            email: The email of the user
            new_password: The new password to set

        Returns:
            True if password was updated, False if user not found
        """
        user = self._users.get(email)
        if user:
            user["password"] = new_password
            return True
        return False

    def get_all_users(self) -> List[Dict[str, str]]:
        """
        Get all users in the repository.

        Returns:
            List of all user dictionaries
        """
        return list(self._users.values())

    def user_exists(self, email: str) -> bool:
        """
        Check if a user exists by email.

        Args:
            email: The email to check

        Returns:
            True if user exists, False otherwise
        """
        return email in self._users

    

# Made with Bob
