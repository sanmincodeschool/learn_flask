#-*- coding: utf8 -*-
from flask import Blueprint,jsonify,session

page1 = Blueprint('page1',__name__,url_prefix='/page1')

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