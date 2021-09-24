import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

logs = []


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        log = request.form.get('log')
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        date_formated = datetime.datetime.strptime(
            date, '%Y-%m-%d').strftime('%b %d')
        if len(log) > 0:
            logs.append((date, log, date_formated))
    return render_template('home.html', logs=logs)
