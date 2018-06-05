#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import json
from urllib import request

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def say2tutu(text):
    config = json.load(open("../configs/tuling.json", "r"))
    url = config["url"]
    key = config["key"]
    secret = config["secret"]

    req = request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)'
                                 ' AppleWebKit/536.26 (KHTML, like Gecko) '
                                 'Version/8.0 Mobile/10A5376e Safari/8536.25')
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            },
            "selfInfo": {
                "location": {
                    "city": "江西省",
                    "province": "南昌市",
                    "street": "紫阳大道"
                }
            }
        },
        "userInfo": {
            "apiKey": key,
            "userId": secret
        }
    }

    with request.urlopen(req, data=json.dumps(data).encode('utf-8')) as f:
        data = json.loads(f.read().decode('utf-8'))
        if data["intent"]["code"] == 10004:
            ret_text = data["results"][0]["values"]["text"]
            return ret_text


def main():
    say2tutu("你好")


if __name__ == '__main__':
    main()
