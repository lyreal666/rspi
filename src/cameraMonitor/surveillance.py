#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import multiprocessing
from time import sleep
from datetime import datetime
from picamera import PiCamera
from utils.tmail import mail
from utils.tpath import resolve

__author__ = 'LY'

'''
    @author: ly
    @file: surveillance.py
    @time: 2018/6/8 20:04
    @desc: 拍照或录像监控
'''


def _loop_photograph(duration):
    r"""
    循环拍照任务
    :param duration:
    :return:
    """
    while True:
        sleep(duration)
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        now_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        img_path = resolve(__file__, '../../configs/photos/%s.jpg' % now_time_str)
        camera.capture(img_path)
        mail(img_path)


def photograph(duration):
    r"""
    使用子进程进行循环拍照
    :param duration:
    :return:
    """
    process = multiprocessing.Process(_loop_photograph, args=(duration,))
    print("Start photograph surveillance...")
    process.daemon = True
    process.start()


if __name__ == '__main__':
    pass