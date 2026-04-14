# System Architecture

## 1. Overview

StuntGuard follows a layered architecture with clear separation of concerns between the mobile frontend, cloud services, and ML backend.

## 2. Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│              Presentation Layer                  │
│  ┌──────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │ User Module  │ │Growth Track │ │Classific. │ │
│  │Register/Login│ │Input & Chart│ │ & Alerts  │ │
│  └──────────────┘ └─────────────┘ └───────────┘ │
├─────────────────────────────────────────────────┤
│              Data & Services Layer               │
│  ┌────────────┐ ┌──────────────┐ ┌───────────┐  │
│  │ SQLite DB  │ │   Firebase   │ │ Flask API │  │
│  │  (Offline) │ │Auth+Firestore│ │(ML Infer.)│  │
│  └────────────┘ └──────────────┘ └───────────┘  │
│                                  ┌───────────┐   │
│                                  │Decision   │   │
│                                  │Tree .pkl  │   │
│                                  └───────────┘   │
└─────────────────────────────────────────────────┘
```

## 3. Components

### 3.1 Mobile Application (Flutter)
- **Framework**: Flutter 3.x
- **State Management**: Riverpod
- **Local Storage**: SQLite (sqflite)
- **UI Components**: Material Design

### 3.2 Cloud Services (Firebase)
- **Authentication**: Email/Password
- **Database**: Firestore
- **Storage**: Firebase Storage (optional)

### 3.3 ML Backend (Python)
- **Framework**: Flask/FastAPI
- **ML Library**: scikit-learn
- **Model**: Decision Tree Classifier
- **Data**: WHO growth standards

## 4. Data Flow

1. User inputs growth data in mobile app
2. Data sent to Flask API for ML inference
3. Model predicts classification
4. Result returned with color-coded alert
5. Data stored locally and synced to Firebase

## 5. Security Considerations

- JWT tokens for API authentication
- Data encryption in transit and at rest
- Secure key management for Firebase
- Input validation and sanitization

## 6. Deployment

- Mobile: App Store / Play Store
- Backend: Azure/AWS/GCP VM or containerized
- Database: Firebase Firestore