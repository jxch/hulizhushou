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


@app.route('/search_option_by_img_base64', methods=["GET"])
def search_option_by_img_base64():
    img_base64 = request.args['img_base64']
    return search_service.search_option_by_img_base64(img_base64)


@app.route('hidden_search_option_by_img_base64', methods=["GET"])
def hidden_search_option_by_img_base64():
    img_base64 = request.args['img_base64']
    return search_service.hidden_search_option_by_img_base64(img_base64)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
