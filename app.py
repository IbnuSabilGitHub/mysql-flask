from flask import Flask, jsonify,render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

from pymysql import MySQLError, OperationalError
import pymysql

app = Flask(__name__)
app.secret_key = 'rahasia'
bcrypt = Bcrypt(app)

    
def get_db_connection():
    try:
        return pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='transaksi'
        )
    except MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None
    except (MySQLError, OperationalError) as e:
        print(f"Error connecting to database: {e}")
        return None
        
@app.route('/')
def root():
    db = get_db_connection()
    
    if db is None:
        return redirect('/error-db')
    
    db.close()
    
    if 'user_id' in session:
        return redirect('/dashboard')
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db_connection()
    if 'user_id' in session:
        return redirect('/dashboard')
    
    error = None
    show_toast = False
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']

        with db.cursor() as cursor:
            query = 'SELECT id, password FROM user WHERE username=%s'
            cursor.execute(query, (username,))
            user = cursor.fetchone()

            if user:
                user_id = user[0]
                hashed_password = user[1]
                if bcrypt.check_password_hash(hashed_password, password_input):
                    session['user_id'] = user_id
                    return redirect('/dashboard')
            show_toast = True
            error = 'Invalid username or password'
    db.close()
    return render_template('login.html', error=error, show_toast=show_toast, toast_message=error)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html', show_toast=True, toast_message="Login Successful")

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')


@app.route('/error-db')
def error_db():
    return render_template('error-db.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.route('/api/pelanggan', methods=['GET'])
def get_pelanggan():
    db = get_db_connection()
    with db.cursor() as cursor:
        query = 'SELECT * FROM pelanggan'
        cursor.execute(query)
        data = cursor.fetchall()
        result = []
        for item in data:
            result.append({
                'id_pelanggan': item[0],
                'nama_pelanggan': item[1],
                'alamat': item[2]
            })
        return jsonify(result)
    db.close()

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/register')
# def register():
#     # hanya contoh manual, nanti bisa buat form
#     hashed = bcrypt.generate_password_hash('password123').decode('utf-8')
#     user = User(username='admin', password=hashed)
#     db.session.add(user)
#     db.session.commit()
#     return 'User admin ditambahkan'