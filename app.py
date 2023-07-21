# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 08:31:43 2023

@author: Soham
"""

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# SQLite database connection
conn = sqlite3.connect('database.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)')


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match!"

        cursor = conn.execute('SELECT * FROM users WHERE email = ?', (email,))
        if cursor.fetchone():
            return "Email already registered!"

        conn.execute('INSERT INTO users (email, username, password) VALUES (?, ?, ?)', (email, username, password))
        conn.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            session['email'] = user[1]
            return redirect(url_for('dashboard'))

        return "Invalid credentials. Please try again."

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', email=session['email'], user_id=session['user_id'])

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
