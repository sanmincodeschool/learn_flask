#-*- coding: utf8 -*-

from flask import Flask,jsonify
import logging



app = Flask(__name__)


@app.route('/index/',methods=['GET','POST'])
def index():
    logging.warn('请求到了')
    data = {
        "data": '数据',
        "code": 0,
        "msg": "ok"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
