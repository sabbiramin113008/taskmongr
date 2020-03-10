# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from flask import Flask, request, jsonify

from taskmongr import controller

app = Flask(__name__)


@app.route('/enqueue', methods=['POST'])
def enqueue():
    return jsonify(controller.db_enqueue(req=request))


@app.route('/tasks', methods=['get'])
def get_tasks():
    return jsonify(controller.get_task(request))


if __name__ == '__main__':

    app.run(
        host='localhost',
        port=4000,
        debug=True
    )
