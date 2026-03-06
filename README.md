# Demo Authentication Service

A simple Python backend project that simulates a user authentication service with a clean, layered architecture.

## 📋 Project Overview

This project demonstrates a basic authentication system built with plain Python (no heavy frameworks). It showcases proper separation of concerns with a clear layered architecture including controllers, services, repositories, and utilities.

## 🏗️ Project Structure

```
demo-auth-service/
├── controllers/
│   └── auth_controller.py      # API endpoint handlers
├── services/
│   └── auth_service.py          # Business logic layer
├── repositories/
│   └── user_repository.py       # Data access layer
├── utils/
│   └── jwt_util.py              # JWT token utilities
├── main.py                      # Application entry point
└── README.md                    # This file
```

## 🎯 Features

### Authentication
- **User Login**: Authenticate users with email and password
- **Token Generation**: Generate JWT-like tokens for authenticated sessions
- **Token Validation**: Verify and decode authentication tokens
- **Password Reset**: Change user passwords with validation
- **Password Reset Request**: Generate reset tokens for password recovery
- **User Profile**: Retrieve user information
- **Logout**: Handle user logout (token invalidation simulation)

### Architecture Layers

1. **Controller Layer** (`controllers/auth_controller.py`)
   - Handles incoming requests
   - Validates input
   - Delegates to service layer
   - Formats responses

2. **Service Layer** (`services/auth_service.py`)
   - Contains business logic
   - Validates credentials
   - Manages authentication flow
   - Coordinates between repository and utilities

3. **Repository Layer** (`repositories/user_repository.py`)
   - Simulates database operations
   - Manages user data storage
   - Provides data access methods

4. **Utility Layer** (`utils/jwt_util.py`)
   - Generates fake JWT tokens
   - Encodes/decodes token payloads
   - Checks token expiration

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone or download the project:
```bash
cd C:/GitRepos/demo-auth-service
```

2. No additional installation needed - the project uses only Python standard library!

### Running the Demo

Execute the main script to see the authentication service in action:

```bash
python main.py
```

This will run through various authentication scenarios including:
- Successful login
- Failed login attempts
- Token validation
- User profile retrieval
- Password reset requests
- Password changes
- Logout operations

## 👥 Sample Users

The repository comes pre-loaded with sample users:

| Email | Password | Name | User ID |
|-------|----------|------|---------|
| john.doe@example.com | password123 | John Doe | user_001 |
| jane.smith@example.com | securepass456 | Jane Smith | user_002 |
| admin@example.com | admin789 | Admin User | user_003 |

## 📝 Usage Examples

### Login Example

```python
from controllers.auth_controller import AuthController

controller = AuthController()

# Attempt login
response = controller.login(
    email="john.doe@example.com",
    password="password123"
)

print(response)
# Output:
# {
#     'success': True,
#     'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...',
#     'message': 'Welcome back, John Doe!',
#     'status_code': 200
# }
```

### Password Reset Example

```python
# Reset password
response = controller.reset_password(
    email="john.doe@example.com",
    old_password="password123",
    new_password="newSecurePass456"
)

print(response)
# Output:
# {
#     'success': True,
#     'message': 'Password reset successfully',
#     'status_code': 200
# }
```

### Token Validation Example

```python
# Validate token
response = controller.validate_token(token)

print(response)
# Output:
# {
#     'success': True,
#     'user': {
#         'user_id': 'user_001',
#         'email': 'john.doe@example.com',
#         'name': 'John Doe'
#     },
#     'message': 'Token is valid',
#     'status_code': 200
# }
```

## 🔒 Security Notes

**⚠️ Important: This is a demonstration project!**

This project is designed for educational purposes and should **NOT** be used in production. Key security considerations:

- Passwords are stored in plain text (use bcrypt/argon2 in production)
- JWT tokens are not cryptographically signed (use PyJWT library in production)
- No rate limiting or brute force protection
- No HTTPS/TLS encryption
- No database persistence
- No session management
- No CSRF protection

## 🛠️ Extending the Project

To make this production-ready, consider:

1. **Add proper password hashing**
   ```bash
   pip install bcrypt
   ```

2. **Use real JWT library**
   ```bash
   pip install PyJWT
   ```

3. **Add database support**
   ```bash
   pip install sqlalchemy
   ```

4. **Add a web framework**
   ```bash
   pip install flask
   # or
   pip install fastapi
   ```

5. **Add input validation**
   ```bash
   pip install pydantic
   ```

## 📚 Learning Objectives

This project demonstrates:

- ✅ Layered architecture (Controller → Service → Repository)
- ✅ Separation of concerns
- ✅ Dependency injection
- ✅ Type hints and documentation
- ✅ Error handling
- ✅ Clean code principles
- ✅ Modular design

## 🤝 Contributing

This is a demo project, but feel free to:
- Fork and experiment
- Add new features
- Improve the architecture
- Add tests
- Enhance documentation

## 📄 License

This project is provided as-is for educational purposes.

## 📧 Contact

For questions or suggestions about this demo project, please open an issue or contact the maintainer.

---

**Happy Learning! 🎓**