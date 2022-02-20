from flask import Flask
from flask import request
from flask import jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return 'Index Page'

@app.route('/api/american',methods=["GET","POST"])

def hello():
    if request.method == 'POST':
        data = request.get_json(force=True)
        country=model.predict(np.array([data['text']]))
        return jsonify({'text': data["text"],'country':str(country[0])})
    else:
        return "hello"
