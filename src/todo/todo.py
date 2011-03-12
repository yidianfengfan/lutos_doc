#coding: utf-8
'''
Created on 2011-3-12

@author: Administrator
'''
import sqlite3
from bottle import route, run, debug, template, request, validate, send_file, error

# 当你在 mod_wsgi 上运行 Bottle 时才需要
from bottle import default_app

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status = '1';")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows = result)
    return output

@route('/new', method = 'GET')
def new_item():
    if request.GET.get('save', '').strip():
        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        conn.text_factory = str
        c = conn.cursor()

        c.execute("INSERT INTO todo(task, status) VALUES(?, ?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '〈p〉新任务已被插入到数据库中，其 ID 为 %s〈/p〉' % new_id
    else:
        return template('new_task.tpl')

@route('/edit/:no', method = 'GET')
def edit_item(no):
    if request.GET.get('save', '').strip():
        edit = request.GET.get('task', '').strip()
        status = request.GET.get('status', '').strip()

        if status == '开启':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id = ?", (edit, status, no))
        conn.commit()

        return '〈p〉编号为 %s 的项目已成功更新〈/p〉' % no
    else:
        conn = sqlite3.connect('todo.db')
            
        c = conn.cursor()
        print "sdfsdf==>", no
        
        c.execute( "SELECT task FROM todo WHERE id = ?;", [no])
        cur_data = c.fetchone()

        return template('edit_task', old = cur_data, no = no)

@route('/item:item#[1-9]+#')
def show_item(item):
    conn = sqlite3.connect('todo.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id = ?", [item])
    result = c.fetchall()
    c.close()

    if not result:
        return '该项目编号不存在！'
    else:
        return '任务：%s' % result[0]

@route('/help')
def help():
    send_file('help.html', root = '.')

@route('/json:json#[1-9]+#')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id = ?", [json])
    result = c.fetchall()
    c.close()

    if not result:
        return {'任务': '该项目编号不存在！'}
    else:
        return {'任务': result[0]}

@error(403)
def mistake403(code):
    return '你的 URL 存在错误！'

@error(404)
def mistake404(code):
    return '对不起，该页面不存在！'

debug(True)

con = sqlite3.connect('todo.db') # 警告：该文件被创建在当前目录下
#con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("delete from todo")
print "delete and add one ........"
con.text_factory = str
try:
    con.execute("INSERT INTO todo (task,status) VALUES ('" + u'访问 Python 网站' + "',1)")
except Exception, data:
    print data    
con.commit()

run(reloader = True)