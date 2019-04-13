#-*- coding: utf8 -*-

from flask import Flask,jsonify,request,g,session
import logging
from page1 import page1
from page2 import page2

blueviews = [page1,page2]


app = Flask(__name__)

app.config.from_pyfile('config.py')

@app.route('/index/',methods=['GET','POST'])
def index():
    # logging.warn('请求到了')

    account = request.args.get('account',None)

    print(account)

    data = {
        "data": account,
        "code": 0,
        "msg": "ok"
    }
    return jsonify(data)

def bootstrap(app=None):

    for view in blueviews:
        app.register_blueprint(view)



    @app.before_request
    def before():

        g.sss="这是一个全局变量"

        print('请求到来了')

    @app.after_request
    def after(response):
        print('请求结束')
        return response
bootstrap(app=app)


if __name__ == '__main__':
    app.run(host=app.config['WEB_HOST'],port=app.config['WEB_PORT'])

