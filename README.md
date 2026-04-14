# 🛡️ StuntGuard

> **Mobile-Based Stunting Detection System Using Machine Learning and WHO Growth Standards**

[![Flutter](https://img.shields.io/badge/Flutter-3.x-02569B?logo=flutter)](https://flutter.dev)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com)
[![License](https://img.shields.io/badge/License-Academic-blue)](./LICENSE)

---

## 📌 Overview

StuntGuard is a parent-facing mobile application that enables early stunting risk screening for children under five (0–59 months). Unlike conventional tools that rely solely on a single Z-score formula, StuntGuard uses a **Decision Tree machine learning model** trained on five features — including birth weight — to detect at-risk cases that a pure formula would miss.

**Case Study Partner:** Bhayangkara Hospital, Indonesia  
**University:** Universiti Teknologi Malaysia (UTM) — Faculty of Computing  
**Course:** SECJ3032 PSM 1 / FYP 1 | Session 2025/2026-2  
**Student:** Jabar Arya Lokananta (A23CS4011)  
**Supervisor:** Dr. Nor Azizah Binti Sa'adon  

---

## 🎯 Objectives

1. Develop a mobile app for parents to register child profiles (incl. birth weight) and input growth data.
2. Implement a Decision Tree ML model to classify nutritional status: **Normal / At-Risk / Stunted**.
3. Design a color-coded alert system (🟢 Green / 🟡 Yellow / 🔴 Red) with actionable guidance.
4. Evaluate system usability (SUS questionnaire, n≥20) and validate ML accuracy vs WHO Z-score benchmarks.

---

## 🏗️ System Architecture

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

---

## 📂 Repository Structure

```
stuntguard/
├── README.md
├── .gitignore
├── docs/                          # Documentation
│   ├── requirements.md            # SRS document
│   ├── architecture.md            # System design
│   ├── api-spec.md                # REST API specification
│   └── test-cases.md              # Test case list (min 30)
├── mobile/                        # Flutter app
│   ├── lib/
│   │   ├── main.dart
│   │   ├── core/
│   │   │   ├── constants/
│   │   │   ├── theme/
│   │   │   └── utils/
│   │   └── features/
│   │       ├── auth/              # Module 1 — User Module
│   │       ├── child_profile/     # Module 1 — Child Profile
│   │       ├── growth_tracking/   # Module 2 — Growth Tracking
│   │       └── classification/    # Module 3 — Classification
│   ├── pubspec.yaml
│   └── test/
└── ml_backend/                    # Python ML service
    ├── notebooks/                 # Jupyter notebooks
    ├── model/                     # Trained .pkl model
    ├── api/                       # Flask REST API
    └── data/                      # Synthetic dataset generation
```

---

## 🧩 Modules

| Module | Status | Description |
|--------|--------|-------------|
| **M1: User Module** | 🔄 In Progress | Register, Login, Manage Child Profile |
| **M2: Growth Tracking** | ⏳ Planned | Input data, charts, history, export |
| **M3: Classification** | ⏳ Planned | ML prediction, color alerts, guidance |
| **M4: ML Backend** | ⏳ Planned | Decision Tree training, Flask API |

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| Mobile Frontend | Flutter 3.x (Dart) |
| State Management | Riverpod |
| Local Database | SQLite (sqflite) |
| Cloud Backend | Firebase (Auth, Firestore, Storage) |
| ML Framework | scikit-learn (Python) |
| ML API | Flask / FastAPI |
| Charts | fl_chart |
| Version Control | Git + GitHub |

---

## 🚀 Getting Started

### Prerequisites
- Flutter SDK 3.x → [Install Flutter](https://docs.flutter.dev/get-started/install)
- Python 3.10+ with pip
- Firebase project (see setup guide below)
- Android Studio or VS Code

### Mobile App Setup
```bash
cd mobile
flutter pub get
flutter run
```

### Firebase Setup
1. Create a Firebase project at [console.firebase.google.com](https://console.firebase.google.com)
2. Enable **Authentication** (Email/Password)
3. Enable **Firestore Database**
4. Download `google-services.json` → place in `mobile/android/app/`
5. Download `GoogleService-Info.plist` → place in `mobile/ios/Runner/`

### ML Backend Setup
```bash
cd ml_backend
pip install -r requirements.txt
python api/app.py
```

---

## 📊 ML Model Details

- **Algorithm:** Decision Tree Classifier (primary) + Random Forest (secondary)
- **Features:** `age_months`, `gender_encoded`, `birth_weight_kg`, `height_cm`, `weight_kg`
- **Labels:** Normal (Z≥-2) | At-Risk (-3≤Z<-2) | Stunted (Z<-3)
- **Dataset:** ~5,000 synthetic records from WHO LMS parameters (2006)
- **Validation:** 80/20 train-test split, 5-fold cross-validation, 50 edge-case test set

---

## 📋 Development Phases

| Phase | Tasks | Status |
|-------|-------|--------|
| **Phase 1: Analysis** | Requirements, literature review, feasibility | ✅ Done |
| **Phase 2: Design** | Architecture, Figma wireframes, DB schema | 🔄 In Progress |
| **Phase 3: Development** | Flutter app, Firebase, ML model, Flask API | ⏳ Planned |
| **Phase 4: Testing** | 30+ test cases, SUS usability, ML validation | ⏳ Planned |

---

## 📚 References

- Ruaida, N. (2018). *Faktor-faktor yang berhubungan dengan kejadian stunting pada balita.* Universitas Muhammadiyah Manado.
- SSGI. (2024). *Hasil Survei Status Gizi Indonesia 2024.* Kemenkes RI.
- WHO. (2006). *WHO child growth standards.* https://www.who.int/tools/child-growth-standards
- WHO. (2020). *Levels and trends in child malnutrition.* https://www.who.int/publications/i/item/9789240003576

---

*Faculty of Computing, Universiti Teknologi Malaysia | PSM1 2025/2026-2*