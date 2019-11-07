"""
1
"""
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
"""
2
"""
# import flask
# import json
#
# server = flask.Flask(__name__)  # 实例化server，把当前这个python文件当作一个服务，__name__代表当前这个python文件
#
#
# @server.route('/index', methods=['get'])  # 'index'是接口路径，methods不写，则默认get请求
# # 装饰器，下面的函数变为一个接口
# def index():
#     res = {'msg': '这是我开发的第一个接口', 'msg_code': '0000'}
#     return json.dumps(res, ensure_ascii=False)
#
#
# # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
#
# server.run(port=8888, debug=True, host='0.0.0.0')  # 启动服务
# # debug=True,改了代码后，不用重启，它会自动重启
# # 'host='0.0.0.0'别人可以通过IP访问
"""
3
"""
import flask
import json
import pymysql


def my_db(sql):
    connect = pymysql.connect(
        host='localhost', user='root', passwd='',
        port=3306, db='test', charset='utf8')
    cur = connect.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()
    else:
        connect.commit()
        res = 'ok'
    cur.close()
    connect.close()
    return res


server = flask.Flask(__name__)


@server.route('/reg', methods=['post'])
def reg():
    username = flask.request.values.get('username')
    pwd = flask.request.values.get('pwd')
    if username and pwd:
        sql = 'select * from my_user where username = "%s";' % username
        if my_db(sql):
            res = {'msg': '用户已存在', 'msg_code': 2001}
        else:
            insert_sql = 'insert into my_user(username,passwd,is_admin) values ("%s","%s",0);' % (username, pwd)
            my_db(insert_sql)
            res = {'msg': '注册成功', 'msg_code': 0000}
    else:
        res = {'msg': '必填字段未填，请查看接口文档！', 'msg_code': 1001}
    return json.dumps(res, ensure_ascii=False)


server.run(port=8888, debug=True, host='0.0.0.0')  # 启动服务
# debug=True,改了代码后，不用重启，它会自动重启
# 'host='0.0.0.0'别人可以通过IP访问
