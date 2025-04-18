from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from config import SECRET_KEY
import jwt
import datetime
from db.database import init_db, connect_db
from langchain_groq import ChatGroq
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
from prompts import SYSTEM

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize the database
init_db()


# Routes
@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/faqs')
def faqs():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded_token['username']
         # Fetch the user data to check admin 
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT isadmin FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        isadmin = user[0] == 1 if user else False
        return render_template('/faqs.html', username=username, isadmin = isadmin)
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('password')

        if not (username and password):
            return render_template('/login.html', error='Username and password are required!')

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT user_id, username, isadmin FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            token = jwt.encode({
                'user_id': user[0],
                'username': user[1],
                'isadmin': user[2],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }, app.config['SECRET_KEY'], algorithm='HS256')

            session['token'] = token
            return redirect(url_for('dashboard'))

        return render_template('/login.html', error='Invalid username or password!')

    return render_template('/login.html')



@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if not (username and email and password):
        return render_template('/login.html', error='All fields are required!')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ? OR username = ?', (email, username))
    existing_user = cursor.fetchone()

    if existing_user:
        return render_template('/login.html', error='Email or Username already exists!')

    cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                   (username, email, password))
    conn.commit()
    conn.close()

    return render_template('/login.html', success='User registered successfully!')


@app.route('/dashboard')
def dashboard():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    try:
        # Decode the token
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded_token.get('username')

        # Fetch the user data to check admin status
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT isadmin FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        # Check if the user is an admin
        isadmin = user[0] == 1 if user else False
        return render_template('/dashboard.html', username=username, isadmin=isadmin)

    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))


@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    # Check if the user is logged in by verifying the session token
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    try:
        # Decode the token to extract the username
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded_token.get('username')
        userid = decoded_token.get('user_id')  # Extract the username and id
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # student_id = request.form.get('student_id')
        student_id = userid
        print(student_id)
        advisor_id = request.form.get('advisor_id')
        appointment_date = request.form.get('appointment_date')
        time_slot = request.form.get('time_slot')

        if not (student_id and advisor_id and appointment_date and time_slot):
            return render_template('/book_appointment.html', error='All fields are required!', username=username)

        conn = connect_db()
        cursor = conn.cursor()

        # Check if the selected time slot is available
        cursor.execute(
            'SELECT * FROM time_slots WHERE advisor_id = ? AND available_date = ? AND time_slot = ? AND is_booked = 0',
            (advisor_id, appointment_date, time_slot)
        )
        slot = cursor.fetchone()
        cursor = conn.cursor()
        cursor.execute('SELECT advisor_id, name FROM advisors')
        advisors = cursor.fetchall()
        cursor = conn.cursor()
        cursor.execute('SELECT isadmin FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        isadmin = user[0] == 1 if user else False
        if not slot:
            conn.close()
            return render_template('/book_appointment.html', error='Selected time slot is not available!', isadmin=isadmin,username=username, advisors=advisors)

        # Book the time slot
        cursor.execute('UPDATE time_slots SET is_booked = 1 WHERE id = ?', (slot[0],))
        cursor.execute(
            'INSERT INTO appointments (student_id, advisor_id, appointment_date, time_slot) VALUES (?, ?, ?, ?)',
            (student_id, advisor_id, appointment_date, time_slot)
        )
        conn.commit()
        
        conn.close()

        return render_template('/book_appointment.html', success='Appointment booked successfully!', isadmin=isadmin,username=username, advisors=advisors)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT advisor_id, name FROM advisors')
    advisors = cursor.fetchall()
    # Fetch the user data to check admin 
    cursor = conn.cursor()
    cursor.execute('SELECT isadmin FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    isadmin = user[0] == 1 if user else False
    cursor.execute('SELECT slot_id, available_date, time_slot FROM time_slots WHERE is_booked = 0')
    slots = cursor.fetchall()
    conn.close()
    return render_template('/book_appointment.html', advisors=advisors, slots=slots, username=username, isadmin = isadmin)


@app.route('/api/advisors', methods=['GET'])
def get_advisors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT advisor_id, name FROM advisors')
    advisors = cursor.fetchall()
    conn.close()

    return jsonify([{"id": advisor[0], "name": advisor[1]} for advisor in advisors])


@app.route('/api/available_slots', methods=['GET'])
def get_available_slots():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT slot_id, available_date, time_slot, advisor_id FROM time_slots WHERE is_booked = 0')
    slots = cursor.fetchall()
    conn.close()

    return jsonify([{
        "id": slot[0],
        "available_date": slot[1],
        "time_slot": slot[2],
        "advisor_id": slot[3]
    } for slot in slots])


@app.route('/api/book_appointment', methods=['POST'])
def book_appointment_api():
    data = request.json
    student_id = data.get('student_id')
    advisor_id = data.get('advisor_id')
    appointment_date = data.get('appointment_date')
    time_slot = data.get('time_slot')

    if not (student_id and advisor_id and appointment_date and time_slot):
        return jsonify({"error": "All fields are required"}), 400

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Check if the selected time slot is available
        cursor.execute('SELECT * FROM time_slots WHERE advisor_id = ? AND available_date = ? AND time_slot = ? AND is_booked = 0',
                       (advisor_id, appointment_date, time_slot))
        slot = cursor.fetchone()

        if not slot:
            conn.close()
            return jsonify({"error": "Selected time slot is not available"}), 400

        # Book the time slot
        cursor.execute('UPDATE time_slots SET is_booked = 1 WHERE id = ?', (slot[0],))
        cursor.execute('INSERT INTO appointments (student_id, advisor_id, appointment_date, time_slot) VALUES (?, ?, ?, ?)',
                       (student_id, advisor_id, appointment_date, time_slot))
        conn.commit()
        return jsonify({"message": "Appointment booked successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


@app.route('/api/slots', methods=['GET'])
def get_slots():
    advisor_id = request.args.get('advisor_id')
    date = request.args.get('date')

    if not advisor_id or not date:
        return jsonify({'error': 'Missing advisor_id or date'}), 400

    # Fetch slots from the database based on advisor_id and date
    query = """
        SELECT time_slot
        FROM time_slots
        WHERE advisor_id = ?  AND available_date = ? AND is_booked = 0
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (advisor_id, date))
    slots = cursor.fetchall()
    conn.close()
    # Convert fetched slots to a list of dictionaries
    slot_list = [{'time_slot': slot[0]} for slot in slots]

    return jsonify(slot_list)

# Admin Pannel

@app.route('/admin')
def admin_dashboard():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()

        return render_template('/admin.html', username=decoded_token['username'], isadmin=isadmin)
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))

# Users Management

@app.route('/users')
def users():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('partials/users.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))

@app.route('/api/users_data')
def get_users_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, email, isadmin FROM users')
    users = cursor.fetchall()
    conn.close()

    # Format the data into a list of dictionaries
    users_data = [
        {"id": user[0], "username": user[1], "email": user[2], "isadmin": user[3] == 1}
        for user in users
    ]

    return jsonify(users_data)

@app.route('/api/toggle_admin', methods=['POST'])
def toggle_admin():
    user_id = request.form.get('user_id')
    message = "Admin status updated successfully"
    if not user_id:
        message = "User ID is required", 400

    conn = connect_db()
    cursor = conn.cursor()

    # Fetch current admin status
    cursor.execute('SELECT isadmin FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        message = "User not found", 404

    is_admin = user[0]

    # Toggle admin status
    new_status = 0 if is_admin == 1 else 1
    cursor.execute('UPDATE users SET isadmin = ? WHERE id = ?', (new_status, user_id))
    conn.commit()
    conn.close()

    # Redirect to admin dashboard with the current section
    return redirect(url_for('users', message = message))


@app.route('/api/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form.get('user_id')
    message = "User deleted successfully"
    if not user_id:
        message = "User ID is required", 400

    conn = connect_db()
    cursor = conn.cursor()

    # Delete user by ID
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    # Redirect to admin dashboard with the current section
    return redirect(url_for('users', message = message))

# Appointments Management

@app.route('/appointments')
def appointments():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('/partials/appointments.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))


@app.route('/api/appointments_data')
def get_appointments_data():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Updated query with LEFT JOIN
    cursor.execute('''
        SELECT 
            a.id, 
            u.username AS student, 
            adv.name AS advisor, 
            a.appointment_date, 
            a.time_slot
        FROM 
            appointments a
        LEFT JOIN 
            users u ON a.student_id = u.id
        LEFT JOIN 
            advisors adv ON a.advisor_id = adv.id
    ''')
    
    appointments = cursor.fetchall()
    conn.close()
    
    # Constructing JSON response
    appointments_data = [
        {
            "id": appt[0],
            "student": appt[1] if appt[1] else "Unknown",  # Handling NULL values
            "advisor": appt[2] if appt[2] else "Unknown",  # Handling NULL values
            "date": appt[3],
            "time_slot": appt[4]
        }
        for appt in appointments
    ]

    return jsonify(appointments_data)


@app.route('/api/delete_appointment', methods=['POST'])
def delete_appointment():
    success_message = "Appointment deleted successfully"
    appointment_id = request.form.get('appointment_id')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()
    return render_template('/partials/appointments.html', success=success_message)


@app.route('/addappointmentslots')
def addappointmentslots():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()
        
        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM advisors')
        advisors = cursor.fetchall()
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('/partials/addappointmentslot.html', advisors = advisors)
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))


@app.route('/api/add_slots', methods=['POST'])
def add_slots():
    advisor_id = request.form.get('advisor_id')
    available_date = request.form.get('available_date')
    time_slot = request.form.get('time_slot')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO time_slots (advisor_id, available_date, time_slot, is_booked)
            VALUES (?, ?, ?,?)
        ''', (advisor_id, available_date, time_slot, 0))

        conn.commit()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM advisors')
        advisors = cursor.fetchall()
        success_message = 'Slot added successfully'
        return render_template('/partials/addappointmentslot.html', success=success_message, advisors = advisors)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('/partials/addappointmentslot.html', error=error_message)

    finally:
        conn.close()

# Doctor Management

@app.route('/adddoctor')
def adddoctor():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('/partials/adddoctor.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))
  
@app.route('/api/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form.get('name')
    specialization = request.form.get('specialization')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO advisors (name, specialization)
            VALUES (?, ?)
        ''', (name, specialization))

        conn.commit()
        success_message = 'Doctor added successfully'
        return render_template('/partials/adddoctor.html', success=success_message)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('/partials/adddoctor.html', error=error_message)

    finally:
        conn.close()

# Course Management

@app.route('/courses', methods=['GET'])
def courses():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('/partials/viewallcourses.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))
    
@app.route('/api/courses_data', methods=['GET'])
def courses_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, course_name, description FROM courses')
    courses = cursor.fetchall()
    conn.close()

    # Prepare the courses data to send as JSON
    courses_list = []
    for course in courses:
        courses_list.append({
            'id': course[0],
            'course_name': course[1],
            'description': course[2]
        })
    
    return jsonify(courses_list)


@app.route('/addcourse')
def addcourse():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch user data to check if the user is an admin
        cursor.execute('SELECT isadmin FROM users WHERE id = ?', (decoded_token['user_id'],))
        isadmin = cursor.fetchone()[0]
        conn.close()
        if not isadmin:
            return redirect(url_for('dashboard'))
        return render_template('/partials/addcourse.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))

@app.route('/updatecourse/<int:course_id>', methods=['GET'])
def updatecourse(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT course_name, description FROM courses WHERE id = ?', (course_id,))
    course = cursor.fetchone()
    conn.close()

    if course:
        course_name, description = course
        return render_template('/partials/updatecourse.html', 
                                      course_id=course_id, 
                                      course_name=course_name, 
                                      description=description)
    else:
        error_message = "Course not found"
        return render_template('/partials/updatecourse.html', error=error_message)


@app.route('/api/update_course/<int:course_id>', methods=['POST'])
def update_course(course_id):
    course_name = request.form.get('course_name')
    description = request.form.get('description')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            UPDATE courses
            SET course_name = ?, description = ?
            WHERE id = ?
        ''', (course_name, description, course_id))

        conn.commit()
        success_message = 'Course updated successfully'
        return render_template('/partials/viewallcourses.html', success=success_message, 
                                      course_id=course_id, course_name=course_name, description=description)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('/partials/viewallcoursses.html', error=error_message, 
                                      course_id=course_id, course_name=course_name, description=description)

    finally:
        conn.close()


@app.route('/api/add_course', methods=['POST'])
def add_course():
    course_name = request.form.get('course_name')
    description = request.form.get('description')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO courses (course_name, description)
            VALUES (?, ?)
        ''', (course_name, description))

        conn.commit()
        success_message = 'Course added successfully'
        return render_template('/partial/addcourse.html', success=success_message)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('/partial/addcourse.html', error=error_message)

    finally:
        conn.close()


# Chat Management (Save & View)

# Load the fine-tuned model and tokenizer
# MODEL_DIR = "./qatar_advisory_bot"  # Path to your downloaded model directory
# tokenizer = GPT2Tokenizer.from_pretrained(MODEL_DIR)
# model = GPT2LMHeadModel.from_pretrained(MODEL_DIR)


@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.json
    chat_id = data.get("chat_id")
    question = data.get("question", "").strip()
    print(question)
    if not question:
        return jsonify({"error": "Question is required"}), 400

    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = decoded_token.get('username')
        userid = decoded_token.get('user_id')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))

    # Generate response

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key="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"
    )
    messages = [
    (
        "system",
        SYSTEM,
    ),
    ("human", question),
]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)   
    # Save the chat session if it doesn't already exist
    conn = connect_db()
    cursor = conn.cursor()

    if chat_id == 0:
        # Create a new chat session
        cursor.execute("INSERT INTO chat_sessions (user_id) VALUES (?)", (userid,))
        chat_id = cursor.lastrowid

    # Save the chat message
    cursor.execute(
        "INSERT INTO chats (user_id, session_id, user_message, bot_response) VALUES (?, ?, ?, ?)",
        (userid, chat_id, question, ai_msg.content)
    )
    conn.commit()
    conn.close()

    return jsonify({"chat_id": chat_id, "question": question, "answer": ai_msg.content})



@app.route('/api/chat_sessions', methods=['GET'])
def get_chat_sessions():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        userid = decoded_token.get('user_id')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT session_id, name, created_at FROM chat_sessions WHERE user_id = ? ORDER BY created_at DESC", (userid,))
    sessions = cursor.fetchall()
    conn.close()
    return jsonify([
        {"id": row[0], "name": row[1] or "New Chat", "created_at": row[2]}
        for row in sessions
    ])

@app.route('/api/chat/<int:chat_id>', methods=['GET'])
def get_chat(chat_id):
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        userid = decoded_token.get('user_id')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_message, bot_response, timestamp FROM chats WHERE chat_session_id = ? AND user_id = ? ORDER BY timestamp ASC",
        (chat_id, userid)
    )
    chats = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            "user_message": row[0],
            "bot_response": row[1],
            "timestamp": row[2]
        }
        for row in chats
    ])


@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0')
