from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from pysnmp.hlapi import *
import os
from datetime import datetime

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from routes import *
from snmp import *

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=80, host="0.0.0.0")
