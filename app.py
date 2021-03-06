#!/usr/bin/python3

import os
from flask import Flask
from flask import request
from flask import jsonify
import pickle
import numpy as np
from joblib import load

# Set environnment variables
# MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE=  os.environ["MODEL_FILE"]
MODEL_PATH =  MODEL_FILE

app = Flask(__name__)
model = load(MODEL_PATH)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/api/american',methods=["POST"])

def hello():
    data = request.get_json(force=True)
    country=model.predict(np.array([data['text']]))
    return jsonify({'is_american':str(country[0]),'version':'0.98','model_date':'2022-02-23 20:48:23'})
