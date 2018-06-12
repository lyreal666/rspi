#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import multiprocessing
from time import sleep
from datetime import datetime
from picamera import PiCamera
from utils.tpath import resolve
from utils.tmail import mail


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
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    count = 1
    while True:
        sleep(duration)
        print("开始第%d次拍照" % count)
        count += 1
        now_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        img_path = resolve(__file__, '../../output/photos/%s.jpg' % now_time_str)
        camera.capture(img_path)
        print("开始发送邮件")
        mail(img_path)


def photograph(duration):
    r"""
    使用子进程进行循环拍照
    :param duration:
    :return:
    """
    print("Start photograph surveillance...")
    process = multiprocessing.Process(target=_loop_photograph, args=(duration,))
    process.daemon = True
    process.start()
    return process


def take_photo(camera):
    now_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    img_path = resolve(__file__, '../../static/photos/%s.jpg' % now_time_str)
    print("开始拍照...")
    camera.capture(img_path)
    return img_path


if __name__ == '__main__':
    pass