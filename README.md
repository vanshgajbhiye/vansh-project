🔐 Smart Face-Based Authentication System

📌 Description

This project adds an extra layer of security to a system using face recognition. Even if someone knows the system password, they cannot access it without being an authorized user.

When the system starts:

The camera captures the user's face
If the face matches the authorized user → Access is granted
If the face does not match → Screen is locked (black screen)
🚀 Features

🔍 Face Detection & Recognition
🔐 Two-layer Security (Face + Password)
⚡ Real-time Authentication
🚫 Unauthorized Access Prevention
🛠️ Technologies Used

Python
OpenCV
face_recognition library
NumPy
▶️ How to Run

Clone the repository
Install required libraries: pip install opencv-python face_recognition numpy
Run the main file: python main.py
📷 Output

Authorized user → System access allowed
Unauthorized user → Black screen / access denied
💡 Future Improvements

Add multi-user authentication
Improve accuracy with deep learning models
Add alert system (email/notification)
👨‍💻 Author

Vansh Gajbhiye
