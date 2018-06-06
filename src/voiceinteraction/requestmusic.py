# -*- encoding:utf-8 -*-

import logging
from urllib import request
from urllib.parse import quote
import json
import os
import re
from utils.voice.play_audio import play_mp3
from utils.voice.au_to_text import voice2txt

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''

music_cfg = json.load(open("../configs/music.json", "r"))
pattern = re.compile(r"(.+?)-(.+?)\.mp3$")


def search_music(music_name):
    musics = os.listdir("../output/music/")
    for music in musics:
        result = pattern.match(music)
        if result and result.group(1) == music_name:
            print(music_name)
            return {
                    "name": result.group(1),
                    "singer": result.group(2),
                    "downloadLink": None,
                    "filePath": os.path.abspath(os.path.join("../../output/music/", music))
                }

    search_url = "%s%s" % (music_cfg["search_url"], quote(music_name))
    with request.urlopen(url=search_url) as gr:
        rs = json.loads(gr.read().decode("utf-8"))
        if not rs["success"]:
            debug("搜索歌曲%s失败" % music_name)
            return None

        first_song_name = rs["songList"][0]["name"]
        first_song_singer = rs["songList"][0]["artists"][0]["name"]
        first_song_id = rs["songList"][0]["id"]

        get_url = music_cfg["get_url"]
        query_str = (
            music_cfg["vendor"][0],
            first_song_id,
            music_cfg["query"]["raw"],
            music_cfg["query"]["br"]
        )
        get_url += "%s?id=%s&row=%s&br=%d" % query_str
        with request.urlopen(get_url) as gr:
            rs = json.loads(gr.read().decode("utf-8"))
            if rs["success"]:
                return {
                    "name": first_song_name,
                    "singer": first_song_singer,
                    "downloadLink": rs["url"],
                    "filePath": None
                }
            else:
                debug("请求歌曲%s下载连接失败, id: %d" % (music_name, first_song_id))


def save_music(music):
    if music is None:
        debug("保存的歌曲为空")
    elif music["filePath"]:
        debug("已存在")
        return music["filePath"]
    file_name = "%s-%s.mp3" % (music["name"], music["singer"])
    with request.urlopen(url=music["downloadLink"]) as gr:
        data = gr.read()
        file_path = "../output/music/%s" % file_name
        with open(file_path, "wb+") as fw:
            fw.write(data)
            return file_path


def play_by_search(music_name):
    music = search_music(music_name)
    file_path = save_music(music)
    play_mp3(file_path,120)


def request_music():
    play_mp3("../static/musics/点歌.mp3")
    text = voice2txt()
    play_by_search(text)


def main():
    play_by_search("大千世界")


if __name__ == '__main__':
    main()
