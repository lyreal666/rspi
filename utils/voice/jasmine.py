#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from urllib import request
from urllib.parse import quote

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def say2xiaoMei(text):
    if text is None:
        debug(f"传给小美的数据有问题: {text}")
        return None
    config = {
              "name": "小美",
              "api_key": "9183698feb3db651de542542d44ddde5",
              "api_secret": "hfwbftot5hd4",
              "url": "http://i.itpk.cn/api.php"
            }
    key = config["api_key"]
    secret = config["api_secret"]
    base_url = config["url"]
    try:
        text = quote(text)
    except TypeError as te:
        debug("Error text say to xiaoMei: %s", text)
        debug(te)
    url = f"{base_url}?api_key={key}&api_secret={secret}&limit=8&question={text}"
    with request.urlopen(url) as ug:
        ret_text = ug.read().decode("utf-8")
        debug(f"小美回答的文字: {ret_text}")
        return ret_text


def main():
    say2xiaoMei("你爸是谁")


if __name__ == '__main__':
    main()
