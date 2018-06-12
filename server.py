#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from flask import Flask, render_template, request

__author__ = 'LY'

'''
    @author: ly
    @file: server.py
    @time: 2018/6/11 11:43
    @desc: 
'''

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>hello world</h1?"


@app.route('/config', methods=["post", "get"])
def config():
    if request.method == 'POST':
        print("开始拍照...")
        from src.cameraMonitor.surveillance import take_photo
        photo_url = take_photo().replace("/home/pi/projects/rspi", '')
        print(photo_url)
        return render_template("control.html", photoUrl=photo_url)
    return render_template("control.html", photoUrl="/static/imgs/preview.jpg")



if __name__ == '__main__':
    app.run(port=8888)