# from flask import Flask
from flask import Flask, render_template, request, jsonify, redirect
from redis import Redis, RedisError
import os
import socket

import json

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)



app = Flask(__name__)

task_list = ['1','2']
task_key = "Kay's task list"

@app.route("/")
def hello():
    try:
        visits = redis.incrby("counter",2)
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route('/tasklist', methods = ['GET'])
def tasklist():
    global task_lists
    task_lists = redis.lrange(task_key, 0, -1)
    length = redis.llen(task_key)
    return render_template('index.html', task_list = task_lists, len = length)

@app.route('/tasks', methods = ['POST'])
def tasks_add():
    global task_key
    tf = redis.rpush(task_key, request.form['task'])

    return redirect('/tasklist')

#    if tf!=0:
#        return "Success insert. There are %d elements in the list." % tf
#    return "Fail to insert"

@app.route('/tasks/delete', methods = ['GET'])
def tasks_delAll():
    global task_key
    redis.ltrim(task_key,1,0)
    tf=redis.llen(task_key)
#    if tf==0:
#        return "Success delete."
#    return "Fail to delete."
    global task_lists
    task_lists = redis.lrange(task_key, 0, -1)
    return redirect('/tasklist')

@app.route('/tasks/deleteOne/<taskid>', methods = ['GET'])
def tasks_delOne(taskid):
    global task_key
    l=len(taskid)
    s=taskid[0:l-1]
    redis.lrem(task_key, 0, s)
    return redirect('/tasklist')

@app.route("/helloworld")
def hello_world():
    return render_template('hello.html', myvar= '1')

@app.route("/getcurrent")
def get_current():
    return os.path.abspath(__file__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
