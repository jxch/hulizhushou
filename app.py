from flask import Flask, render_template
import logging
import service.search_service as search_service
from flask import request
import pandas as pd

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello_world():
    df = pd.DataFrame([])
    return render_template('index.html', res=df)


@app.route('/search_text', methods=["GET"])
def search_text():
    text = request.args['text']
    df = search_service.search_text(text)
    return render_template('index.html', res=df)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
