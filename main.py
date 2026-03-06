"""
Main Application Module

This module simulates API requests by calling controller methods.
Demonstrates the complete authentication flow.
"""

import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.auth_controller import AuthController


def print_separator():
    """Print a visual separator for better output readability."""
    print("\n" + "=" * 80 + "\n")


def print_response(title: str, response: dict):
    """
    Print a formatted response.

    Args:
        title: Title for the response
        response: Response dictionary to print
    """
    print(f"📋 {title}")
    print("-" * 80)
    for key, value in response.items():
        print(f"  {key}: {value}")
    print_separator()


def main():
    """
    Main function to demonstrate the authentication service.
    Simulates various API requests.
    """
    print_separator()
    print("🚀 DEMO AUTHENTICATION SERVICE")
    print("   Simulating API Requests")
    print_separator()

    # Initialize controller
    controller = AuthController()

    # ========================================================================
    # Scenario 1: Successful Login
    # ========================================================================
    print("📌 SCENARIO 1: Successful Login")
    print_separator()
    
    login_response = controller.login(
        email="john.doe@example.com",
        password="password123"
    )
    print_response("Login Response", login_response)

    # Store token for later use
    auth_token = login_response.get("token")

    # ========================================================================
    # Scenario 2: Failed Login (Wrong Password)
    # ========================================================================
    print("📌 SCENARIO 2: Failed Login (Wrong Password)")
    print_separator()
    
    failed_login = controller.login(
        email="john.doe@example.com",
        password="wrongpassword"
    )
    print_response("Failed Login Response", failed_login)

    # ========================================================================
    # Scenario 3: Validate Token
    # ========================================================================
    print("📌 SCENARIO 3: Validate Token")
    print_separator()
    
    if auth_token:
        validation_response = controller.validate_token(auth_token)
        print_response("Token Validation Response", validation_response)

    # ========================================================================
    # Scenario 4: Get User Profile
    # ========================================================================
    print("📌 SCENARIO 4: Get User Profile")
    print_separator()
    
    profile_response = controller.get_user_profile("jane.smith@example.com")
    print_response("User Profile Response", profile_response)

    # ========================================================================
    # Scenario 5: Request Password Reset
    # ========================================================================
    print("📌 SCENARIO 5: Request Password Reset")
    print_separator()
    
    reset_request = controller.request_password_reset("admin@example.com")
    print_response("Password Reset Request Response", reset_request)

    # Store reset token
    reset_token = reset_request.get("reset_token")
    if reset_token:
        print(f"🔑 Reset Token Generated: {reset_token[:50]}...")
        print_separator()

    # ========================================================================
    # Scenario 6: Reset Password
    # ========================================================================
    print("📌 SCENARIO 6: Reset Password")
    print_separator()
    
    password_reset = controller.reset_password(
        email="john.doe@example.com",
        old_password="password123",
        new_password="newSecurePass456"
    )
    print_response("Password Reset Response", password_reset)

    # ========================================================================
    # Scenario 7: Login with New Password
    # ========================================================================
    print("📌 SCENARIO 7: Login with New Password")
    print_separator()
    
    new_login = controller.login(
        email="john.doe@example.com",
        password="newSecurePass456"
    )
    print_response("Login with New Password Response", new_login)

    # ========================================================================
    # Scenario 8: Failed Password Reset (Wrong Old Password)
    # ========================================================================
    print("📌 SCENARIO 8: Failed Password Reset (Wrong Old Password)")
    print_separator()
    
    failed_reset = controller.reset_password(
        email="jane.smith@example.com",
        old_password="wrongpassword",
        new_password="newPassword123"
    )
    print_response("Failed Password Reset Response", failed_reset)

    # ========================================================================
    # Scenario 9: Logout
    # ========================================================================
    print("📌 SCENARIO 9: Logout")
    print_separator()
    
    if auth_token:
        logout_response = controller.logout(auth_token)
        print_response("Logout Response", logout_response)

    # ========================================================================
    # Scenario 10: User Not Found
    # ========================================================================
    print("📌 SCENARIO 10: User Not Found")
    print_separator()
    
    not_found = controller.get_user_profile("nonexistent@example.com")
    print_response("User Not Found Response", not_found)

    # ========================================================================
    # Summary
    # ========================================================================
    print("✅ DEMO COMPLETED")
    print("   All authentication scenarios have been tested successfully!")
    print_separator()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

# Made with Bob
