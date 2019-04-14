#-*- coding: utf8 -*-
from flask import Blueprint,jsonify,session,render_template

page1 = Blueprint('page1',__name__,url_prefix='/page1')


@page1.context_processor
def common():
    return{
        'isLogin' : True
    }

@page1.route('/a/')
def test():

    # print('请求蓝图page1---')
    session['account']='test'
    account = session['account']
    print(account)
    data = {
        "data" : "session"
    }
    return jsonify(data)

@page1.route('/main/')
def main():
    data = {
        "name" : u'数据',
        "isLogin" : True
    }
    return render_template('main.html',**data)
