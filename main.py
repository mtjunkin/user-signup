from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def def_display_signup():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def validate_input():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        username_error = "Username must be entered"

    if password == '':
        password_error = "Password must be entered"
    
    if verify_password == '':
        verify_password_error = "Password must be entered"

    for char in (username):
        if char == ' ':
            username_error = "Username cannot contain spaces"
        else:
            if len(username)<3 or len(username)>20:
                username_error = "Username must be between 3 and 20 characters"

    for char in password:
        if char == ' ':
            password_error = "Password cannot contain spaces"
        else:
            if len(password)<3 or len(password)>20:
                password_error = "Password must be between 3 and 20 characters"

    if password != verify_password:
        verify_password_error = "Passwords do not match"

    if email != '':
        if "@" and "." not in email:
            email_error = "That is not a valid email"

    if not username_error and not password_error and not verify_password_error and not email_error:
        username=request.form['username']
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, 
        verify_password_error=verify_password_error, email_error=email_error, username=username, email=email)

app.run()