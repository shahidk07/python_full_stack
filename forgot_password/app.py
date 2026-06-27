from flask import Flask, request, redirect, render_template, session
from random import randint
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

otp = randint(100000, 999999)


@app.route("/send_otp", methods=["POST"])
def send_otp():
    email = request.form["email"]
    otp = str(randint(100000, 999999))

    session["email"] = email
    session["otp"] = otp

    # create email
    msg = EmailMessage()
    msg["Subject"] = "Password Reset OTP Testing"
    msg["From"] = "viperoflegendkiller@gmail.com"
    msg["To"] = email

    msg.set_content(f"your otp is {otp}")

    # send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: