#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import json
from urllib import request
import base64
import os

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
'''

try:
    app_cfg = json.load(open("../configs/baidu_yuyin.json", "r"))
except Exception as e:
    debug("解析配置信息出现问题:", e)


def get_token_url():
    r"""
    读取配置,拼凑用来获取访问令牌的url,并返回该url
    :return:
    """
    token_url = f'https://aip.baidubce.com/oauth/2.0/token?' \
                f'grant_type=client_credentials&' \
                f'client_id={app_cfg["API_Key"]}&client_secret={app_cfg["Secret_Key"]}'
    return token_url


def get_token():
    r"""
    返回访问令牌
    :return:
    """
    token_url = get_token_url()
    try:
        with request.urlopen(token_url) as ug:
            data = json.loads(ug.read().decode("utf-8"))
            token = data["access_token"]
    except Exception as exp:
        debug('获取token异常,请检查网络', exp)

    return token


def voice_to_text(audio_path):
    r"""
    访问百度语音restAPI,语音转文字
    :param audio_path:
    :return: 解析后的语音
    """
    token = get_token()

    # 设置格式
    RATE = "16000"
    FORMAT = "wav"
    CUID = "120.78.173.232"
    DEV_PID = "1536"

    # 以字节格式读取文件之后进行编码
    with open(audio_path, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(audio_path)
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": FORMAT,
        "rate": RATE,
        "dev_pid": DEV_PID,
        "speech": speech,
        "cuid": CUID,
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header("Content-Length", size)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)'
                                 ' AppleWebKit/536.26 (KHTML, like Gecko) '
                                 'Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req, data=json.dumps(data).encode('utf-8')) as f:
        data = json.loads(f.read().decode('utf-8'))
        if "result" in data:
            result = data["result"][0]
            debug(f"语音转文字结果: {result}")
            return result
        else:
            return None


def main():
    # audio_path = r'../static/audios/A2_1.wav'
    audio_path = r'F:\codingSpace\Python\rspi\output\audios\1527496724.082431.wav'
    print(voice_to_text(audio_path)[0])


if __name__ == '__main__':
    main()
