#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from urllib import request
import json
import base64

__author__ = 'LY'

'''
    @author: ly
    @file: facerecognition.py
    @time: 2018/6/11 12:33
    @desc: 
'''

configs = {
    "key": "lto5Pfi3sr3LZsf1Bc7NRO06",
    "secret": "vwlM3e1EPujSmvX7keQqxlQIrplmfWl9",
    "tokenUrl": "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s",
    "fcUrl": "https://aip.baidubce.com/rest/2.0/face/v3/match",
}


with request.urlopen(configs["tokenUrl"] % (configs["key"], configs["secret"])) as gr:
    result = json.loads(gr.read().decode("utf-8"))
    access_token = result["access_token"]


def face_comparison(img_src_path, img_cped_path):
    if access_token is None:
        print("没有获取到access_token!!!")
    with open(img_src_path, 'rb') as sr:
        with open(img_cped_path, 'rb') as cpedr:
            img_src = base64.b64encode(sr.read()).decode("utf-8")
            img_cped = base64.b64encode(cpedr.read()).decode("utf-8")
            post_data = json.dumps(
                [{"image": img_src, "image_type": "BASE64", "face_type": "LIVE",
                  "quality_control": "LOW"},
                 {"image": img_cped, "image_type": "BASE64", "face_type": "IDCARD",
                  "quality_control": "LOW"}]).encode('utf-8')
            req = request.Request(configs["fcUrl"] + "?access_token=" + access_token)
            req.add_header('Content-Type', 'application/json')
            req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)'
                                         ' AppleWebKit/536.26 (KHTML, like Gecko) '
                                         'Version/8.0 Mobile/10A5376e Safari/8536.25')
            with request.urlopen(req, data=post_data) as pr:
                result = json.loads(pr.read().decode("utf-8"))
                if result["error_msg"] == "SUCCESS" and result["result"]["score"] > 50:
                    return True
                else:
                    return False


if __name__ == '__main__':
    print(face_comparison("F:\\codingSpace\\Python\\rspi\\static\\imgs\\cped.jpg",
                    "F:\\codingSpace\\Python\\rspi\\static\\imgs\\src.jpg"))
    print(face_comparison("F:\\codingSpace\\Python\\rspi\\static\\imgs\\cped.jpg",
                    r"F:\codingSpace\Python\rspi\static\imgs\cped1.jpg"))