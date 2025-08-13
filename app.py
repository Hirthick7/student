import datetime
import io
import base64
import uuid
from flask import Flask, request, render_template, url_for
import pymongo
import qrcode
from PIL import Image

app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://hirthick07:bapcx5j97s@cluster0.4ympx62.mongodb.net/student")
db = client["attendance_db"]
sessions_col = db["sessions"]
attendances_col = db["attendances"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        session_name = request.form['session_name']
        expiry_minutes = int(request.form.get('expiry_minutes', 10))
        session_id = str(uuid.uuid4())
        created_at = datetime.datetime.now()
        expires_at = created_at + datetime.timedelta(minutes=expiry_minutes)

        sessions_col.insert_one({
            "session_id": session_id,
            "name": session_name,
            "created_at": created_at,
            "expires_at": expires_at
        })

        # Generate QR code
        attend_url = url_for('attend', session_id=session_id, _external=True)
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(attend_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        qr_img_src = f'data:image/png;base64,{img_str}'

        return render_template('qr_code.html', 
                            session_name=session_name,
                            expiry_minutes=expiry_minutes,
                            qr_img_src=qr_img_src,
                            attend_url=attend_url,
                            session_id=session_id)

    return render_template('teacher.html')

@app.route('/attend/<session_id>', methods=['GET', 'POST'])
def attend(session_id):
    session = sessions_col.find_one({"session_id": session_id})
    if not session:
        return render_template('error.html', message="Invalid Session")

    now = datetime.datetime.now()
    if now > session['expires_at']:
        return render_template('error.html', message="Session Expired")

    if request.method == 'POST':
        student_id = request.form['student_id']
        if attendances_col.find_one({"session_id": session_id, "student_id": student_id}):
            return render_template('error.html', message="Attendance Already Marked")

        attendances_col.insert_one({
            "session_id": session_id,
            "student_id": student_id,
            "timestamp": now
        })
        return render_template('success.html')

    return render_template('attend.html', session_id=session_id)

@app.route('/view/<session_id>')
def view_attendance(session_id):
    session = sessions_col.find_one({"session_id": session_id})
    if not session:
        return render_template('error.html', message="Invalid Session")

    attendances = list(attendances_col.find({"session_id": session_id}).sort("timestamp", 1))
    return render_template('view_attendance.html', 
                         session_name=session['name'],
                         attendances=attendances)

if __name__ == '__main__':
    app.run(debug=True)