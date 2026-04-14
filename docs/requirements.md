# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document describes the software requirements for StuntGuard, a mobile-based stunting detection system using machine learning and WHO growth standards.

### 1.2 Scope
StuntGuard is a parent-facing mobile application that enables early stunting risk screening for children under five (0–59 months).

### 1.3 Definitions
- **Stunting**: Chronic malnutrition indicated by low height-for-age
- **Z-score**: Standard deviation score used in growth assessment
- **WHO Standards**: World Health Organization child growth standards

## 2. Overall Description

### 2.1 Product Perspective
StuntGuard provides an accessible tool for parents to monitor child growth and detect stunting risks early.

### 2.2 Product Functions
- User registration and authentication
- Child profile management
- Growth data input and tracking
- ML-based classification
- Alert system with guidance

### 2.3 User Characteristics
- Parents with basic smartphone literacy
- Age range: 18-50 years
- Technical background: Minimal

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
- Clean, intuitive mobile interface
- Color-coded alerts (Green/Yellow/Red)
- Charts for growth visualization

#### 3.1.2 Hardware Interfaces
- Android/iOS smartphones
- Minimum Android API 21, iOS 11.0

#### 3.1.3 Software Interfaces
- Firebase Authentication
- Firestore Database
- Flask REST API for ML inference

### 3.2 Functional Requirements

#### 3.2.1 User Management
- Register with email/password
- Login/logout functionality
- Profile management

#### 3.2.2 Child Profile Management
- Add multiple children
- Store birth date, gender, birth weight
- Edit/delete profiles

#### 3.2.3 Growth Tracking
- Input height, weight, age
- View growth history
- Export data

#### 3.2.4 Classification
- ML prediction using Decision Tree
- Display results with alerts
- Provide guidance based on classification

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance
- Response time < 2 seconds for local operations
- < 5 seconds for ML inference

#### 3.3.2 Security
- Secure authentication
- Data encryption
- Privacy compliance

#### 3.3.3 Usability
- SUS score > 70
- Intuitive navigation

#### 3.3.4 Reliability
- 99% uptime
- Offline functionality

## 4. Appendices

### 4.1 References
- WHO Child Growth Standards (2006)
- Flutter Documentation
- Firebase Documentation