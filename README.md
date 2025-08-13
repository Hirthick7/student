Classroom Attendance System with QR Codes
This is a Flask-based web application for managing classroom attendance using QR codes. Teachers can create sessions, generate QR codes for attendance, and students can scan these QR codes to mark their attendance. The system prevents duplicate and late entries and stores data in a MongoDB Atlas database.
Features

Teacher Dashboard: Create sessions with a name and expiry time, generating a QR code for attendance.
Student Attendance: Students scan the QR code and submit their ID to mark attendance.
Duplicate Prevention: Ensures each student can only mark attendance once per session.
Session Expiry: Attendance can only be marked within the session's active time window.
Attendance View: Teachers can view the list of students who marked attendance for a session.
Responsive Design: Simple, clean UI with inline CSS for accessibility on all devices.

Project Structure
attendance_system/
├── app.py                     # Flask application code
├── templates/                 # HTML templates
│   ├── index.html             # Home page
│   ├── teacher.html           # Teacher dashboard for creating sessions
│   ├── qr_code.html           # Displays QR code and session details
│   ├── attend.html            # Student attendance form
│   ├── success.html           # Success message after marking attendance
│   ├── error.html             # Error message display
│   └── view_attendance.html   # View attendance list
├── requirements.txt           # Python dependencies
├── README.md                  # This file

Prerequisites

Python: Version 3.8 or higher
MongoDB Atlas: Cloud database account (configured with the provided URI)
Internet Access: Required for connecting to MongoDB Atlas

Installation

Clone or Set Up the Project:

Create a directory named attendance_system.
Copy the provided app.py and templates/ folder with all HTML files into this directory.


Set Up MongoDB Atlas:

Ensure you have a MongoDB Atlas account and cluster.
Update the MongoDB URI in app.py with your credentials:client = pymongo.MongoClient("mongodb+srv://hirthick07:bapcx5j97s@cluster0.4ympx62.mongodb.net/student?retryWrites=true&w=majority")
db = client["student"]


Verify that your IP is whitelisted in MongoDB Atlas Network Access settings.
Ensure the user hirthick07 has readWrite permissions for the student database.


Install Dependencies:

Create a requirements.txt file with the following:flask==2.3.3
pymongo==4.6.3
qrcode==7.4.2
pillow==10.4.0
dnspython==2.6.1


Install dependencies:pip install -r requirements.txt




Run the Application:

Navigate to the attendance_system directory:cd attendance_system


Run the Flask app:python app.py


Access the app at http://127.0.0.1:5000/ in a web browser.



Usage

Teacher:

Navigate to the Teacher Dashboard (/teacher).
Enter a session name and expiry time (in minutes) to create a session.
A QR code and direct link are generated. Share the QR code with students.
View attendance for a session via the "View Attendance" link.


Student:

Scan the QR code or visit the provided attendance link.
Enter your Student ID to mark attendance.
Receive confirmation if successful, or an error if the session is expired or attendance is already marked.


View Attendance:

Teachers can access the attendance list for a session to see student IDs and timestamps.



Troubleshooting

MongoDB Connection Error:
Verify the MongoDB Atlas URI, username, and password in app.py.
Ensure your IP is whitelisted in MongoDB Atlas.
Check that dnspython is installed for SRV resolution.


Module Not Found:
Confirm all dependencies are installed (pip list).
Reinstall dependencies if needed: pip install -r requirements.txt.


Port Conflict:
If port 5000 is in use, modify app.py to use another port, e.g., app.run(debug=True, port=5001).


QR Code Not Displaying:
Ensure qrcode and pillow are installed correctly.


For other issues, check the Flask console output or contact the developer with the error message.

Dependencies

Flask: Web framework for the application
PyMongo: MongoDB driver for Python
QRCode: Generates QR codes
Pillow: Image processing for QR code rendering
dnspython: Resolves MongoDB Atlas SRV records

Notes

The app uses inline CSS in HTML templates for simplicity and portability.
The MongoDB database (student) is automatically created when data is inserted.
Ensure secure handling of MongoDB credentials in production environments.

For questions or issues, please contact the developer or raise an issue in the repository.