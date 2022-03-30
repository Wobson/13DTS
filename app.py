from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error
from datetime import datetime


app = Flask(__name__)
DATABASE = "smile.db"
app.secret_key = "rangabanga"


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def homey():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
