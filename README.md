# 2347129_2347122_CV_hackathon

# Attendance Management System

An automated attendance management system using **Face Detection and Recognition**. This system simplifies the process of marking attendance by using live video feeds and advanced image processing techniques.

---

## Features

- **Face Detection & Recognition**: Captures live video, detects faces, and matches them with pre-encoded images.
- **Attendance Logging**: Records attendance with date and time.
- **GUI Interface**: User-friendly interface for managing attendance.
- **Text-to-Speech Feedback**: Audio confirmation for attendance recognition.
- **Data Retrieval**: View and manage attendance records.

---

## Tech Stack

- **Python**: Main programming language.

### Libraries Used
- **OpenCV (cv2)**: Real-time face detection.
- **SimpleFacerec**: Simplifies face encoding and recognition.
- **pyttsx3**: Text-to-speech feedback.
- **SpeechRecognition**: (Optional) For adding voice commands.
- **Tkinter**: GUI design.
- **Pillow (PIL)**: Image processing.
- **Datetime**: Logging timestamps.
- **OS and Shutil**: File and directory operations.

---

## Installation and Setup

### 1. Clone the Repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
### 2. Install Dependencies:
Make sure you have Python installed (>= 3.7). Install the required libraries:
```
pip install opencv-python simplefacerec pyttsx3 SpeechRecognition pillow
```
###3. Run the Application:
```
   python main.py
```
###4. Add User Images:
```
Place images of users in the designated folder (/images/known/) for face encoding.
```


Using the Application

Start Attendance: Click the "START" button to begin attendance.

Add New User: Add images for new users via the GUI.

Get Attendance: Retrieve attendance records.

Screenshots

![image](https://github.com/user-attachments/assets/2cc3b188-44aa-49b6-8dea-b112af71df07)




![image](https://github.com/user-attachments/assets/ab452f46-a1d7-405e-95df-ec2fa56fd416)


![image](https://github.com/user-attachments/assets/13088a84-b700-47e5-8a3b-9e2c87035bba)




