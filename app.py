from flask import Flask, render_template, request, jsonify
from imageio import imread
from PIL import Image
import numpy as np
import re
import base64
import sys
import os

sys.path.append(os.path.abspath("./model"))
from model import *

model = init()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    parseImage(request.get_data())

    out = [[1]]
    x = Image.open('output.png')
    x = x.resize((8,8))
    x.save('resized.png')
    
    x = imread('resized.png', pilmode='L')
    x = np.invert(x)
    x = x.reshape(8,8)
    x = np.array(x).flatten()

    prediction = model.predict([x])[0]
 
    return jsonify({'prediction': int(prediction)})


def parseImage(imgData):
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True, port=port)
