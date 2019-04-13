#-*- coding: utf8 -*-
from flask import Blueprint,jsonify,g

page2 = Blueprint('page2',__name__,url_prefix='/page2')

@page2.route('/a/')
def test():

    print('请求蓝图page2---')
 
    data = {
        "data" : g.sss
    }
    return jsonify(data)