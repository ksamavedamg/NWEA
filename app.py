
from flask import Flask, request, abort
import json
import sqlite3

app = Flask(__name__)
i = 10

@app.route('/')
def index():
    return "Hello, World!"
