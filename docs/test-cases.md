# Test Cases

## 1. User Authentication

### TC-001: User Registration
**Description:** Verify user can register with valid email and password
**Preconditions:** App installed, no existing account
**Steps:**
1. Open app
2. Tap "Register"
3. Enter valid email and password
4. Tap "Register"
**Expected Result:** Account created, redirected to login

### TC-002: User Login
**Description:** Verify user can login with correct credentials
**Preconditions:** Valid account exists
**Steps:**
1. Open app
2. Enter email and password
3. Tap "Login"
**Expected Result:** Logged in, redirected to dashboard

### TC-003: Invalid Login
**Description:** Verify error on wrong credentials
**Preconditions:** Valid account exists
**Steps:**
1. Enter wrong password
2. Tap "Login"
**Expected Result:** Error message displayed

## 2. Child Profile Management

### TC-004: Add Child Profile
**Description:** Verify adding new child profile
**Steps:**
1. Login
2. Go to "Children" tab
3. Tap "Add Child"
4. Fill all fields
5. Save
**Expected Result:** Child added to list

### TC-005: Edit Child Profile
**Description:** Verify editing existing child profile
**Steps:**
1. Select child from list
2. Tap "Edit"
3. Modify fields
4. Save
**Expected Result:** Changes saved

### TC-006: Delete Child Profile
**Description:** Verify deleting child profile
**Steps:**
1. Select child
2. Tap "Delete"
3. Confirm
**Expected Result:** Child removed from list

## 3. Growth Tracking

### TC-007: Add Growth Data
**Description:** Verify adding growth measurement
**Steps:**
1. Select child
2. Go to "Growth" tab
3. Tap "Add Measurement"
4. Enter height and weight
5. Save
**Expected Result:** Data saved, chart updated

### TC-008: View Growth Chart
**Description:** Verify growth chart displays correctly
**Steps:**
1. Select child with growth data
2. View chart
**Expected Result:** Chart shows data points and trends

### TC-009: Export Growth Data
**Description:** Verify data export functionality
**Steps:**
1. Select child
2. Tap "Export"
3. Choose format
**Expected Result:** File downloaded

## 4. Classification

### TC-010: Normal Classification
**Description:** Verify normal growth classification
**Steps:**
1. Add normal growth data
2. Trigger classification
**Expected Result:** Green alert, normal message

### TC-011: At-Risk Classification
**Description:** Verify at-risk classification
**Steps:**
1. Add borderline data
2. Trigger classification
**Expected Result:** Yellow alert, warning message

### TC-012: Stunted Classification
**Description:** Verify stunted classification
**Steps:**
1. Add low growth data
2. Trigger classification
**Expected Result:** Red alert, urgent message

## 5. Offline Functionality

### TC-013: Offline Data Entry
**Description:** Verify app works offline
**Steps:**
1. Disable internet
2. Add growth data
**Expected Result:** Data stored locally

### TC-014: Sync on Reconnect
**Description:** Verify data syncs when online
**Steps:**
1. Reconnect internet
2. Open app
**Expected Result:** Local data synced to cloud

## 6. Performance

### TC-015: Response Time
**Description:** Verify response time < 2 seconds
**Steps:**
1. Perform various operations
2. Measure time
**Expected Result:** All operations < 2 seconds

### TC-016: Memory Usage
**Description:** Verify reasonable memory usage
**Steps:**
1. Use app for extended period
2. Monitor memory
**Expected Result:** Memory usage stable

## 7. Security

### TC-017: Data Encryption
**Description:** Verify data is encrypted
**Steps:**
1. Inspect stored data
**Expected Result:** Data encrypted

### TC-018: Session Timeout
**Description:** Verify automatic logout
**Steps:**
1. Login and wait
**Expected Result:** Auto logout after timeout

## 8. Usability

### TC-019: SUS Questionnaire
**Description:** Administer System Usability Scale
**Steps:**
1. Have 20+ users complete SUS
**Expected Result:** Average score > 70

### TC-020: Accessibility
**Description:** Verify accessibility compliance
**Steps:**
1. Test with screen reader
2. Test color contrast
**Expected Result:** Meets accessibility standards

## 9. ML Model Validation

### TC-021: Model Accuracy
**Description:** Verify ML model accuracy > 90%
**Steps:**
1. Test with validation dataset
**Expected Result:** Accuracy > 90%

### TC-022: Edge Cases
**Description:** Verify handling of edge cases
**Steps:**
1. Test with extreme values
**Expected Result:** Graceful handling

### TC-023: WHO Standards Compliance
**Description:** Verify compliance with WHO standards
**Steps:**
1. Compare with WHO Z-score calculations
**Expected Result:** Consistent results

## 10. Integration

### TC-024: Firebase Integration
**Description:** Verify Firebase connectivity
**Steps:**
1. Perform auth and data operations
**Expected Result:** All operations successful

### TC-025: API Integration
**Description:** Verify ML API connectivity
**Steps:**
1. Send prediction requests
**Expected Result:** Responses received

### TC-026: Database Sync
**Description:** Verify SQLite-Firestore sync
**Steps:**
1. Add data offline, sync online
**Expected Result:** Data consistent

## 11. Error Handling

### TC-027: Network Error
**Description:** Verify graceful network error handling
**Steps:**
1. Disconnect network during operation
**Expected Result:** User-friendly error message

### TC-028: Invalid Input
**Description:** Verify input validation
**Steps:**
1. Enter invalid data
**Expected Result:** Validation errors shown

### TC-029: API Error
**Description:** Verify API error handling
**Steps:**
1. Trigger API error
**Expected Result:** Error handled gracefully

## 12. Compatibility

### TC-030: Android Compatibility
**Description:** Verify Android device compatibility
**Steps:**
1. Test on various Android versions
**Expected Result:** Works on Android 5.0+

### TC-031: iOS Compatibility
**Description:** Verify iOS device compatibility
**Steps:**
1. Test on various iOS versions
**Expected Result:** Works on iOS 11.0+

### TC-032: Screen Size Compatibility
**Description:** Verify different screen sizes
**Steps:**
1. Test on phones and tablets
**Expected Result:** UI adapts correctly