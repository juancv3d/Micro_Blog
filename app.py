from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    # Set up mongo connection
    client = MongoClient(os.environ.get('MONGODB_URI'))
    app.db = client.microblog

    @app.route('/', methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            log = request.form.get('log')
            date = datetime.datetime.today().strftime('%Y-%m-%d')
            date_formated = datetime.datetime.strptime(
                date, '%Y-%m-%d').strftime('%b %d')

            if len(log) > 0:
                app.db.logs.insert_one({
                    'log': log,
                    'date_formated': date_formated,
                    'date': date
                })
                flash("Log added", "success")
            else:
                flash("Log can't be empty", "error")

        return render_template('home.html', logs=app.db.logs.find().sort('_id', -1).limit(10))

    return app
