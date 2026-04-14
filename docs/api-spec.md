# REST API Specification

## Base URL
```
https://api.stuntguard.com/v1
```

## Authentication
All API requests require JWT token in Authorization header:
```
Authorization: Bearer <jwt_token>
```

## Endpoints

### POST /auth/login
Authenticate user and return JWT token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "jwt_token_here",
  "user": {
    "id": "user_id",
    "email": "user@example.com"
  }
}
```

### POST /predict
Predict stunting classification.

**Request:**
```json
{
  "age_months": 24,
  "gender": "male",
  "birth_weight_kg": 3.2,
  "height_cm": 85.5,
  "weight_kg": 11.8
}
```

**Response:**
```json
{
  "classification": "normal",
  "confidence": 0.95,
  "alert_level": "green",
  "guidance": "Child growth is within normal range. Continue monitoring."
}
```

### GET /children
Get user's children profiles.

**Response:**
```json
[
  {
    "id": "child_id",
    "name": "John Doe",
    "birth_date": "2020-01-15",
    "gender": "male",
    "birth_weight_kg": 3.2
  }
]
```

### POST /children
Create new child profile.

**Request:**
```json
{
  "name": "Jane Doe",
  "birth_date": "2021-03-20",
  "gender": "female",
  "birth_weight_kg": 2.8
}
```

### PUT /children/{id}
Update child profile.

### DELETE /children/{id}
Delete child profile.

### GET /growth/{child_id}
Get growth history for child.

**Response:**
```json
[
  {
    "date": "2023-01-15",
    "age_months": 36,
    "height_cm": 95.2,
    "weight_kg": 14.5,
    "classification": "normal"
  }
]
```

### POST /growth
Add new growth measurement.

**Request:**
```json
{
  "child_id": "child_id",
  "height_cm": 95.2,
  "weight_kg": 14.5
}
```

## Error Responses

**400 Bad Request:**
```json
{
  "error": "Invalid input data",
  "details": "age_months must be between 0 and 60"
}
```

**401 Unauthorized:**
```json
{
  "error": "Invalid or expired token"
}
```

**404 Not Found:**
```json
{
  "error": "Resource not found"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal server error"
}
```

## Rate Limiting
- 100 requests per minute per user
- 1000 requests per hour per user