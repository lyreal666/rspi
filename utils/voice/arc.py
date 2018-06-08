#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import json
import os
import base64
import hmac
import hashlib
import time
from urllib import request, parse
from utils.tpath import resolve

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''

arc_cfg = json.load(open(resolve(__file__, "../../configs/arc.json"), "r", encoding="utf-8"))


def audio_recognize(audio_path):
    size = os.path.getsize(audio_path)
    timestamp = time.time()

    string_to_sign = arc_cfg["httpMethod"] + "\n" + arc_cfg["httpUri"] + "\n" + arc_cfg["key"] + "\n" +\
                     arc_cfg["dataType"] + "\n" + arc_cfg["signatureVersion"] + "\n" + str(timestamp)
    sign = base64.b64encode(hmac.new(arc_cfg["key"].encode("utf-8"), string_to_sign.encode("utf-8"), digestmod=hashlib.sha1).digest())
    data = parse.urlencode([
        ('access_key', arc_cfg["key"]),
        ('sample_bytes', size),
        ('timestamp', str(timestamp)),
        ('signature', sign),
        ('data_type', arc_cfg["dataType"]),
        ("signature_version", arc_cfg["signatureVersion"])
    ])

    req = request.Request(arc_cfg["requestUrl"])
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)'
                                 ' AppleWebKit/536.26 (KHTML, like Gecko) '
                                 'Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req, data=data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


def main():
    audio_recognize(os.path.normpath("F:\\codingSpace\\Python\\rspi\\output\\music\\大千世界-许嵩.mp3"))


if __name__ == '__main__':
    main()
