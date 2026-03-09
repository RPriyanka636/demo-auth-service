# Demo Authentication Service - Architecture Documentation

## 📋 Table of Contents
- [Overview](#overview)
- [Architecture Pattern](#architecture-pattern)
- [System Components](#system-components)
- [Data Flow](#data-flow)
- [Component Details](#component-details)
- [Security Considerations](#security-considerations)
- [API Endpoints](#api-endpoints)
- [Setup and Usage](#setup-and-usage)
- [Future Enhancements](#future-enhancements)

## Overview

The **Demo Authentication Service** is a Python-based demonstration application that showcases a clean, layered architecture for user authentication. This service implements core authentication features including user login, token validation, password management, and user profile retrieval.

### Purpose
This is a **demonstration/educational project** designed to illustrate:
- Clean architecture principles
- Separation of concerns
- Layered application design
- JWT token-based authentication flow
- Best practices in code organization

### Technology Stack
- **Language**: Python 3.x
- **Authentication**: JWT (JSON Web Tokens) - Simulated
- **Data Storage**: In-memory (simulated database)
- **Architecture**: Layered/Clean Architecture

## Architecture Pattern

This application follows a **3-tier layered architecture** pattern:

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│    (main.py - Demo/Test Runner)         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Controller Layer                │
│    (controllers/auth_controller.py)     │
│    - Request handling                   │
│    - Response formatting                │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Service Layer                   │
│    (services/auth_service.py)           │
│    - Business logic                     │
│    - Validation                         │
│    - Token management                   │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
┌───────▼────────┐  ┌──────▼──────────┐
│  Repository    │  │   Utilities     │
│  Layer         │  │   Layer         │
│ (repositories/ │  │  (utils/        │
│  user_repo.py) │  │   jwt_util.py)  │
│ - Data access  │  │  - JWT ops      │
└────────────────┘  └─────────────────┘
```

### Design Principles

1. **Separation of Concerns**: Each layer has a distinct responsibility
2. **Dependency Injection**: Components receive dependencies through constructors
3. **Single Responsibility**: Each class/module has one primary purpose
4. **Loose Coupling**: Layers communicate through well-defined interfaces
5. **High Cohesion**: Related functionality is grouped together

## System Components

### 1. Main Application (`main.py`)
**Purpose**: Entry point and demonstration runner

**Responsibilities**:
- Orchestrates demo scenarios
- Simulates API requests
- Displays formatted output
- Demonstrates complete authentication flow

**Key Features**:
- 10 comprehensive test scenarios
- User-friendly console output
- Error handling and reporting

### 2. Controller Layer (`controllers/auth_controller.py`)

**Purpose**: HTTP request handling and response formatting

**Class**: `AuthController`

**Methods**:
| Method | Purpose | Returns |
|--------|---------|---------|
| `login(email, password)` | Handle user login | Token + status |
| `validate_token(token)` | Validate JWT token | User data + status |
| `reset_password(email, old_pwd, new_pwd)` | Change password | Success status |
| `request_password_reset(email)` | Generate reset token | Reset token |
| `get_user_profile(email)` | Retrieve user info | User profile |
| `logout(token)` | Handle logout | Success status |

**Response Format**:
```python
{
    "success": bool,
    "message": str,
    "status_code": int,
    "token": str (optional),
    "user": dict (optional)
}
```

### 3. Service Layer (`services/auth_service.py`)

**Purpose**: Business logic and validation

**Class**: `AuthService`

**Core Responsibilities**:
- User authentication logic
- Password validation and management
- Token generation and validation
- Business rule enforcement

**Key Methods**:
| Method | Business Logic |
|--------|----------------|
| `authenticate_user()` | Validates credentials, generates token |
| `validate_token()` | Checks token validity and expiration |
| `reset_password()` | Enforces password rules, updates password |
| `request_password_reset()` | Generates time-limited reset token |
| `get_user_info()` | Retrieves sanitized user data |

**Validation Rules**:
- Email and password required for login
- New passwords must be ≥8 characters
- New password must differ from old password
- Old password must be verified before reset

### 4. Repository Layer (`repositories/user_repository.py`)

**Purpose**: Data access and persistence simulation

**Class**: `UserRepository`

**Data Structure**:
```python
{
    "email": str,
    "password": str,  # Plain text in demo (would be hashed in production)
    "name": str,
    "user_id": str
}
```

**Sample Users**:
- john.doe@example.com (password123)
- jane.smith@example.com (securepass456)
- admin@example.com (admin789)

**Methods**:
| Method | Purpose |
|--------|---------|
| `find_by_email(email)` | Lookup user by email |
| `find_by_user_id(user_id)` | Lookup user by ID |
| `update_password(email, new_pwd)` | Update user password |
| `user_exists(email)` | Check if user exists |
| `get_all_users()` | Retrieve all users |

### 5. Utility Layer (`utils/jwt_util.py`)

**Purpose**: JWT token operations

**Class**: `JWTUtil`

**Token Structure**:
```
header.payload.signature
```

**Header**:
```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

**Payload**:
```json
{
    "user_id": "user_001",
    "email": "user@example.com",
    "iat": 1234567890,  // Issued at timestamp
    "exp": 1234654290   // Expiry timestamp
}
```

**Methods**:
| Method | Purpose |
|--------|---------|
| `generate_token(user_id, email, expiry_hours)` | Create JWT token |
| `decode_token(token)` | Extract payload from token |
| `is_token_expired(token)` | Check token expiration |

**Note**: This is a **simplified JWT implementation** for demonstration. Production systems should use libraries like PyJWT with proper cryptographic signing.

## Data Flow

### Login Flow
```
1. User provides email + password
   ↓
2. Controller receives request
   ↓
3. Service validates credentials
   ↓
4. Repository fetches user data
   ↓
5. Service verifies password
   ↓
6. JWT Util generates token
   ↓
7. Service returns token
   ↓
8. Controller formats response
   ↓
9. User receives token
```

### Token Validation Flow
```
1. User provides token
   ↓
2. Controller receives token
   ↓
3. Service checks expiration
   ↓
4. JWT Util decodes token
   ↓
5. Service extracts user_id
   ↓
6. Repository fetches user
   ↓
7. Service returns user data
   ↓
8. Controller formats response
```

### Password Reset Flow
```
1. User provides email + old_pwd + new_pwd
   ↓
2. Controller receives request
   ↓
3. Service validates input
   ↓
4. Repository fetches user
   ↓
5. Service verifies old password
   ↓
6. Service validates new password
   ↓
7. Repository updates password
   ↓
8. Service confirms success
   ↓
9. Controller formats response
```

## Component Details

### Authentication Service Dependencies

```python
class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()  # Data access
        self.jwt_util = JWTUtil()                # Token operations
```

### Controller Dependencies

```python
class AuthController:
    def __init__(self):
        self.auth_service = AuthService()  # Business logic
```

### Error Handling Strategy

**Service Layer**:
- Returns tuples: `(success: bool, data: Any, message: str)`
- Catches and handles exceptions
- Provides descriptive error messages

**Controller Layer**:
- Translates service responses to HTTP-like responses
- Sets appropriate status codes
- Formats consistent response structure

**Repository Layer**:
- Returns `None` for not found
- Returns `bool` for success/failure operations
- No exception throwing for normal operations

## Security Considerations

### ⚠️ Demo Limitations

This is a **demonstration project** with intentional simplifications:

1. **Plain Text Passwords**: Passwords stored in plain text
   - **Production**: Use bcrypt, argon2, or PBKDF2

2. **Simplified JWT**: No cryptographic signing
   - **Production**: Use PyJWT with proper secret keys

3. **In-Memory Storage**: Data lost on restart
   - **Production**: Use PostgreSQL, MySQL, or MongoDB

4. **No Rate Limiting**: Vulnerable to brute force
   - **Production**: Implement rate limiting

5. **No HTTPS**: Tokens transmitted insecurely
   - **Production**: Always use HTTPS/TLS

6. **No Token Blacklist**: Logout doesn't invalidate tokens
   - **Production**: Implement token blacklist/revocation

7. **No Input Sanitization**: Basic validation only
   - **Production**: Sanitize all inputs, prevent injection

### Production Security Checklist

- [ ] Hash passwords with bcrypt/argon2
- [ ] Use proper JWT library (PyJWT)
- [ ] Implement HTTPS/TLS
- [ ] Add rate limiting
- [ ] Implement token blacklist
- [ ] Add CSRF protection
- [ ] Sanitize all inputs
- [ ] Use environment variables for secrets
- [ ] Implement proper session management
- [ ] Add audit logging
- [ ] Use secure database
- [ ] Implement 2FA/MFA
- [ ] Add account lockout after failed attempts

## API Endpoints

### POST /login
**Purpose**: Authenticate user and receive token

**Request**:
```python
{
    "email": "user@example.com",
    "password": "password123"
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "token": "eyJhbGc...",
    "message": "Welcome back, John Doe!",
    "status_code": 200
}
```

**Response** (Failure - 401):
```python
{
    "success": false,
    "token": null,
    "message": "Invalid email or password",
    "status_code": 401
}
```

### POST /validate-token
**Purpose**: Validate JWT token

**Request**:
```python
{
    "token": "eyJhbGc..."
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "user": {
        "user_id": "user_001",
        "email": "user@example.com",
        "name": "John Doe"
    },
    "message": "Token is valid",
    "status_code": 200
}
```

### POST /reset-password
**Purpose**: Change user password

**Request**:
```python
{
    "email": "user@example.com",
    "old_password": "password123",
    "new_password": "newSecurePass456"
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "message": "Password reset successfully",
    "status_code": 200
}
```

### POST /request-password-reset
**Purpose**: Generate password reset token

**Request**:
```python
{
    "email": "user@example.com"
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "reset_token": "eyJhbGc...",
    "message": "Password reset token generated successfully",
    "status_code": 200
}
```

### GET /user-profile
**Purpose**: Retrieve user profile

**Request**:
```python
{
    "email": "user@example.com"
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "user": {
        "user_id": "user_001",
        "email": "user@example.com",
        "name": "John Doe"
    },
    "message": "User profile retrieved successfully",
    "status_code": 200
}
```

### POST /logout
**Purpose**: Logout user (invalidate token)

**Request**:
```python
{
    "token": "eyJhbGc..."
}
```

**Response** (Success - 200):
```python
{
    "success": true,
    "message": "Logged out successfully",
    "status_code": 200
}
```

## Setup and Usage

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses standard library)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd demo-auth-service

# No additional installation needed - uses Python standard library
```

### Running the Demo

```bash
# Run the main demonstration
python main.py
```

### Expected Output

The demo runs 10 scenarios:
1. ✅ Successful login
2. ❌ Failed login (wrong password)
3. ✅ Token validation
4. ✅ Get user profile
5. ✅ Request password reset
6. ✅ Reset password
7. ✅ Login with new password
8. ❌ Failed password reset (wrong old password)
9. ✅ Logout
10. ❌ User not found

### Project Structure

```
demo-auth-service/
├── main.py                          # Entry point and demo runner
├── controllers/
│   └── auth_controller.py          # Request handling layer
├── services/
│   └── auth_service.py             # Business logic layer
├── repositories/
│   └── user_repository.py          # Data access layer
├── utils/
│   └── jwt_util.py                 # JWT utility functions
└── docs/
    └── architecture.md             # This document
```

## Future Enhancements

### Short-term Improvements
1. **Add Unit Tests**: Implement pytest test suite
2. **Add Type Hints**: Complete type annotations
3. **Add Logging**: Implement structured logging
4. **Add Configuration**: Environment-based config
5. **Add Documentation**: API documentation with Swagger/OpenAPI

### Medium-term Enhancements
1. **Real Database**: Integrate SQLAlchemy + PostgreSQL
2. **Password Hashing**: Implement bcrypt
3. **Real JWT**: Use PyJWT library
4. **REST API**: Add Flask/FastAPI framework
5. **Token Blacklist**: Implement Redis-based blacklist

### Long-term Features
1. **OAuth2 Support**: Add OAuth2/OpenID Connect
2. **2FA/MFA**: Implement two-factor authentication
3. **Role-Based Access**: Add RBAC system
4. **Audit Logging**: Track all authentication events
5. **Rate Limiting**: Prevent brute force attacks
6. **Email Verification**: Verify user emails
7. **Session Management**: Advanced session handling
8. **API Gateway**: Add API gateway integration

## Contributing

This is a demonstration project. For production use:
1. Review all security considerations
2. Implement proper password hashing
3. Use production-grade JWT library
4. Add comprehensive testing
5. Implement proper error handling
6. Add monitoring and logging
7. Follow security best practices

## Changelog

### Version 1.0.1 (2026-03-09)
- **Fixed**: Removed duplicate `reset_password()` method in [`auth_service.py`](../services/auth_service.py:106) that was causing conflicts
- **Fixed**: Cleaned up extra whitespace in [`user_repository.py`](../repositories/user_repository.py)
- **Improved**: Code quality and consistency across service layer

### Version 1.0.0 (2026-03-09)
- Initial architecture documentation
- Complete authentication service implementation
- Comprehensive API documentation

## License

This is a demonstration project for educational purposes.

---

**Generated by**: IBM Bob AI Assistant
**Last Updated**: 2026-03-09
**Version**: 1.0.1