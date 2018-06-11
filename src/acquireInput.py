#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import platform
from time import sleep
from .voiceinteraction.voicechat import chat_once
from utils.voice import play_mp3
from .cameraMonitor.facerecognition import face_comparison

__author__ = 'LY'

'''
    
'''


def acquire():
    process = None
    fc_failed_times = 0
    chat_flag = True
    while True:
        instruction = input("输入命令: ").lower().strip()
        if instruction == "":
            if chat_flag:
                chat_flag = False
                play_mp3(r"F:\codingSpace\Python\rspi\static\audios\语音聊天启动语音.mp3")
                sleep(3)
                chat_once()
            else:
                chat_once()
        elif instruction == "ps":
            if platform.platform().split('-')[0] == "Linux":
                from .cameraMonitor.surveillance import photograph
                process = photograph(20)
        elif instruction == "fc":
            play_mp3(r"F:\codingSpace\Python\rspi\static\audios\人脸识别.mp3")
            if input('请把脸部对准摄像头, 按下回车开始人脸检测。').strip() == '':
                if process is not None:
                    process.terminate()
                from .cameraMonitor.surveillance import take_photo
                checked_photo_path = take_photo()
                cp_result = face_comparison(r"F:\codingSpace\Python\rspi\static\imgs\src.jpg", checked_photo_path)
                if cp_result:
                    print("ok", 'Welcome back!')
                    play_mp3(r"F:\codingSpace\Python\rspi\static\audios\ly识别通过.mp3")
                    fc_failed_times = 0
                else:
                    play_mp3(r"F:\codingSpace\Python\rspi\static\audios\检测不通过.mp3")
                    fc_failed_times += 1
                    print("Remaining for %d times to try..." % (3 - fc_failed_times, ))
                    if fc_failed_times == 3:
                        print("Sorry, please contact the administrator...")
                        play_mp3(r"F:\codingSpace\Python\rspi\static\audios\报警提示.mp3")
        elif instruction == "q":
            exit(0)
        else:
            print("输入命令无法识别")


if __name__ == '__main__':
    acquire()
