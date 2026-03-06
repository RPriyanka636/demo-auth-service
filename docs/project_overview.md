# Demo Authentication Service - Project Overview

## 📌 Purpose

This repository contains a **demonstration authentication service** built with Python to showcase clean architecture principles and best practices in software development. It serves as an educational resource for understanding how to structure a backend authentication system with proper separation of concerns.

**⚠️ Important:** This is a learning project and should **NOT** be used in production environments without significant security enhancements.

## 🎯 Project Goals

1. **Educational**: Demonstrate layered architecture patterns in Python
2. **Simplicity**: Use only Python standard library (no external dependencies)
3. **Clarity**: Provide clear, well-documented code examples
4. **Practicality**: Show real-world authentication flows in a simplified manner

## 🏗️ Architecture Overview

The project follows a **4-layer architecture** pattern:

```
┌─────────────────────────────────────────┐
│         Controller Layer                │  ← API Interface
│    (controllers/auth_controller.py)     │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│          Service Layer                  │  ← Business Logic
│     (services/auth_service.py)          │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│        Repository Layer                 │  ← Data Access
│  (repositories/user_repository.py)      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│          Utility Layer                  │  ← Helper Functions
│       (utils/jwt_util.py)               │
└─────────────────────────────────────────┘
```

## 📦 Module Descriptions

### 1. Controller Layer (`controllers/auth_controller.py`)

**Purpose:** Acts as the entry point for all authentication requests.

**Responsibilities:**
- Receives and validates incoming requests
- Delegates business logic to the service layer
- Formats responses with appropriate status codes
- Handles request/response transformation

**Key Methods:**
- `login()` - Authenticates users and returns JWT tokens
- `validate_token()` - Verifies token validity
- `reset_password()` - Handles password change requests
- `request_password_reset()` - Generates password reset tokens
- `get_user_profile()` - Retrieves user information
- `logout()` - Handles user logout (token invalidation simulation)

### 2. Service Layer (`services/auth_service.py`)

**Purpose:** Contains the core business logic for authentication operations.

**Responsibilities:**
- Validates user credentials
- Implements authentication rules and policies
- Coordinates between repository and utility layers
- Enforces business constraints (e.g., password length requirements)

**Key Methods:**
- `authenticate_user()` - Verifies email/password and generates tokens
- `validate_token()` - Checks token validity and retrieves user data
- `reset_password()` - Validates and updates user passwords
- `request_password_reset()` - Generates secure reset tokens
- `get_user_info()` - Retrieves user data without sensitive information

**Business Rules Implemented:**
- Passwords must be at least 8 characters
- New passwords must differ from old passwords
- Token expiration validation
- User existence verification

### 3. Repository Layer (`repositories/user_repository.py`)

**Purpose:** Manages data persistence and retrieval (simulated in-memory storage).

**Responsibilities:**
- Simulates database operations
- Provides CRUD operations for user data
- Abstracts data storage implementation

**Key Methods:**
- `find_by_email()` - Retrieves user by email address
- `find_by_user_id()` - Retrieves user by unique ID
- `update_password()` - Updates user password
- `get_all_users()` - Returns all users
- `user_exists()` - Checks if user exists

**Sample Data:**
The repository includes three pre-configured users for testing:
- John Doe (john.doe@example.com)
- Jane Smith (jane.smith@example.com)
- Admin User (admin@example.com)

### 4. Utility Layer (`utils/jwt_util.py`)

**Purpose:** Provides JWT token generation and validation utilities.

**Responsibilities:**
- Generates fake JWT-like tokens
- Encodes/decodes token payloads
- Validates token expiration
- Base64 encoding/decoding

**Key Methods:**
- `generate_token()` - Creates JWT-like tokens with expiration
- `decode_token()` - Extracts payload from tokens
- `is_token_expired()` - Checks if token has expired

**Note:** This is a simplified JWT implementation for demonstration. Production systems should use libraries like PyJWT.

### 5. Main Application (`main.py`)

**Purpose:** Demonstrates the authentication service in action.

**Features:**
- Runs 10 different authentication scenarios
- Shows successful and failed operations
- Provides formatted output for easy understanding
- Serves as integration test and usage example

## 🔄 Authentication Flow

### Login Flow
```
1. User provides email + password
   ↓
2. Controller receives request
   ↓
3. Service validates credentials via Repository
   ↓
4. Service generates JWT token via Utility
   ↓
5. Controller returns token to user
```

### Token Validation Flow
```
1. User provides JWT token
   ↓
2. Controller receives token
   ↓
3. Service decodes token via Utility
   ↓
4. Service checks expiration
   ↓
5. Service retrieves user data from Repository
   ↓
6. Controller returns user information
```

### Password Reset Flow
```
1. User provides email + old password + new password
   ↓
2. Controller receives request
   ↓
3. Service validates old password via Repository
   ↓
4. Service checks new password requirements
   ↓
5. Service updates password in Repository
   ↓
6. Controller confirms success
```

## 🔐 Security Considerations

### Current Implementation (Demo Only)
- ❌ Plain text password storage
- ❌ Unsigned JWT tokens
- ❌ No rate limiting
- ❌ No HTTPS/TLS
- ❌ No session management
- ❌ No CSRF protection
- ❌ In-memory data (lost on restart)

### Production Requirements
- ✅ Use bcrypt/argon2 for password hashing
- ✅ Use PyJWT for proper token signing
- ✅ Implement rate limiting (e.g., Flask-Limiter)
- ✅ Use HTTPS/TLS encryption
- ✅ Add persistent database (PostgreSQL, MongoDB)
- ✅ Implement session management
- ✅ Add CSRF tokens
- ✅ Add input validation (Pydantic)
- ✅ Implement logging and monitoring
- ✅ Add multi-factor authentication

## 🚀 Usage

### Running the Demo
```bash
python main.py
```

### Using as a Library
```python
from controllers.auth_controller import AuthController

controller = AuthController()

# Login
response = controller.login("john.doe@example.com", "password123")
token = response["token"]

# Validate token
validation = controller.validate_token(token)

# Get user profile
profile = controller.get_user_profile("john.doe@example.com")
```

## 📚 Learning Outcomes

By studying this project, you will understand:

1. **Layered Architecture**: How to separate concerns across different layers
2. **Dependency Injection**: How layers depend on abstractions, not implementations
3. **Single Responsibility**: Each module has one clear purpose
4. **Type Hints**: Using Python type annotations for better code clarity
5. **Error Handling**: Proper exception handling and error messages
6. **Documentation**: Writing clear docstrings and comments
7. **Authentication Basics**: Core concepts of user authentication
8. **Token-Based Auth**: How JWT tokens work (simplified)

## 🔧 Extension Ideas

To enhance your learning, consider adding:

1. **Database Integration**: Replace in-memory storage with SQLite/PostgreSQL
2. **Web Framework**: Add Flask/FastAPI for REST API endpoints
3. **Password Hashing**: Implement bcrypt for secure password storage
4. **Real JWT**: Use PyJWT library for proper token signing
5. **Unit Tests**: Add pytest tests for all layers
6. **API Documentation**: Generate OpenAPI/Swagger docs
7. **Docker Support**: Containerize the application
8. **CI/CD Pipeline**: Add GitHub Actions for automated testing
9. **Logging**: Implement structured logging
10. **Monitoring**: Add health checks and metrics

## 📖 Related Concepts

- **REST API Design**: How to structure HTTP endpoints
- **OAuth 2.0**: Industry-standard authorization framework
- **OpenID Connect**: Authentication layer on top of OAuth 2.0
- **Session Management**: Alternative to token-based auth
- **RBAC**: Role-Based Access Control for authorization
- **API Security**: OWASP API Security Top 10

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork and experiment
- Add new features
- Improve documentation
- Share your learnings

## 📄 License

This project is provided as-is for educational purposes.

---

**Created for learning and demonstration purposes** 🎓