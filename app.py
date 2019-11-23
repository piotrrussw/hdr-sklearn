from flask import Flask, render_template, request
import numpy as np
import re
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # parseImage(request.get_data())
    out = [[1]]
    response = np.array_str(np.argmax(out, axis=1))

    return response


def parseImage():
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)
