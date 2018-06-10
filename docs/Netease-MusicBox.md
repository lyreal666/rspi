# NetEase-MusicBox

#### 感谢为 MusicBox 的开发付出过努力的[每一个人](https://github.com/darknessomi/musicbox/graphs/contributors)！

高品质网易云音乐命令行版本，简洁优雅，丝般顺滑，基于Python编写。

[![Software License](https://camo.githubusercontent.com/e7302c620b3589a361fc5503732f3505347205d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d627269676874677265656e2e737667)](https://github.com/darknessomi/musicbox/blob/master/LICENSE.txt) [![versions](https://camo.githubusercontent.com/75530bb011a14726292348a94a1c5a39b59aae75/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f4e6574456173652d4d75736963426f782e737667)](https://pypi.org/project/NetEase-MusicBox/) [![platform](https://camo.githubusercontent.com/adef70c7b1e71ca011fa75a4e22f51fd24d5075c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d322e372d677265656e2e737667)](https://github.com/darknessomi/musicbox/blob/master) [![platform](https://camo.githubusercontent.com/9b901eba929a486a5a2077369f0fa28e9bdd9099/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e352d677265656e2e737667)](https://github.com/darknessomi/musicbox/blob/master)

[![NetEase-MusicBox](https://camo.githubusercontent.com/5b0f2a90c5eaf8f4e235291c40ffee31f21c06de/687474703a2f2f376a317976332e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f707265766965772e676966)](https://pypi.org/project/NetEase-MusicBox/)

### 功能特性

1. 320kbps的高品质音乐
2. 歌曲，艺术家，专辑检索
3. 网易22个歌曲排行榜
4. 网易新碟推荐
5. 网易精选歌单
6. 网易主播电台
7. 私人歌单，每日推荐
8. 随心打碟
9. 本地收藏，随时加❤
10. 播放进度及播放模式显示
11. 现在播放及桌面歌词显示
12. 歌曲评论显示
13. 一键进入歌曲专辑
14. 定时退出
15. Vimer式快捷键让操作丝般顺滑
16. 可使用数字快捷键
17. 可使用自定义全局快捷键

### 键盘快捷键

| J     | Down            | 下移               |
| ----- | --------------- | ------------------ |
| K     | Up              | 上移               |
| H     | Back            | 后退               |
| L     | Forword         | 前进               |
| U     | Prev page       | 上一页             |
| D     | Next page       | 下一页             |
| F     | Search          | 快速搜索           |
| [     | Prev song       | 上一曲             |
| ]     | Next song       | 下一曲             |
| =     | Volume +        | 音量增加           |
| -     | Volume -        | 音量减少           |
| Space | Play/Pause      | 播放/暂停          |
| ?     | Shuffle         | 手气不错           |
| M     | Menu            | 主菜单             |
| P     | Present/History | 当前/历史播放列表  |
| I     | Music Info      | 当前音乐信息       |
| ⇧+P   | Playing Mode    | 播放模式切换       |
| A     | Add             | 添加曲目到打碟     |
| ⇧+A   | Enter album     | 进入专辑           |
| G     | To the first    | 跳至首项           |
| ⇧+G   | To the end      | 跳至尾项           |
| Z     | DJ list         | 打碟列表           |
| S     | Star            | 添加到收藏         |
| C     | Collection      | 收藏列表           |
| R     | Remove          | 删除当前条目       |
| ⇧+J   | Move Down       | 向下移动当前项目   |
| ⇧+K   | Move Up         | 向上移动当前项目   |
| ⇧+C   | Cache           | 缓存歌曲到本地     |
| ,     | Like            | 喜爱               |
| .     | Trash FM        | 删除 FM            |
| /     | Next FM         | 下一FM             |
| Q     | Quit            | 退出               |
| T     | Timing Exit     | 定时退出           |
| W     | Quit&Clear      | 退出并清除用户信息 |

### PyPi安装（推荐）

```
$ pip(3) install NetEase-MusicBox
```

### Git clone最新版

```
$ git clone https://github.com/darknessomi/musicbox.git && cd musicbox
$ python(3) setup.py install
```

### macOS安装

```
$ pip(3) install NetEase-MusicBox
$ brew install mpg123
```

### Linux安装

#### Fedora

首先添加[FZUG](https://github.com/FZUG/repo/wiki)源，然后`sudo dnf install musicbox`（通过此方法安装可能仍然需要`pip install NetEase-MusicBox`更新到最新版）。

#### Ubuntu/Debian

```
$ (sudo) pip install NetEase-MusicBox

$ (sudo) apt-get install mpg123
```

#### Arch Linux

```
$ pacaur -S netease-musicbox-git # or $ yaourt musicbox
```

### 依赖

#### 必选

1. `mpg123` 用于播放歌曲

#### 可选

1. `aria2` 用于缓存歌曲
2. `libnotify-bin` 用于支持消息提示（Linux平台）
3. `pyqt python-dbus dbus qt` 用于支持桌面歌词 (Mac 用户需要 `brew install qt --with-dbus` 获取支持 DBus 的 Qt)

### 配置文件

配置文件地址: `~/.netease-musicbox/config.json` 可配置缓存，快捷键，消息，桌面歌词。 由于歌曲 API 只接受中国大陆地区访问，港澳台及海外用户请自行设置代理：

```
export http_proxy=http://ip:port
curl ip.cn
```

显示IP属于中国大陆地区即可。

### 已测试的系统兼容列表

| macOS    | 10.13 / 10.12 / 10.11 |
| -------- | --------------------- |
| Ubuntu   | 14.04                 |
| Kali     | 1.1.0 / 2.0 / Rolling |
| CentOS   | 7                     |
| openSUSE | 13.2                  |
| Fedora   | 22                    |
| Arch     | Rolling               |

### 错误处理

当某些歌曲不能播放时，总时长为 00:01 时，请检查是否为版权问题导致。

如遇到在特定终端下不能播放问题，首先检查**此终端**下mpg123能否正常使用，其次检查**其他终端**下musicbox能否正常使用，报告issue的时候请告知以上使用情况以及出问题终端的报错信息。

同时，您可以通过`tail -f ~/.netease-musicbox/musicbox.log`自行查看日志。

### 已知问题及解决方案

- [#374](https://github.com/darknessomi/musicbox/issues/374) i3wm下播放杂音或快进问题，此问题常见于Arch Linux。尝试更改mpg123配置。
- [#405](https://github.com/darknessomi/musicbox/issues/405) 32位Python下cookie时间戳超出了32位整数最大值。尝试使用64位版本的Python或者拷贝cookie文件到对应位置。
- [#347](https://github.com/darknessomi/musicbox/issues/347) 暂停时间超过一定长度（数分钟）之后mpg123停止输出，导致切换到下一首歌。此问题是mpg123的bug，暂时无解决方案。

### 使用

```
$ musicbox
```

Enjoy it !

### 更新日志

2018-06-05 版本 0.2.5.0 全部迁移到新版api，大量错误修复

2018-05-21 版本 0.2.4.3 更新依赖，错误修复

2017-11-28 版本 0.2.4.2 更新获取歌曲列表的api

2017-06-03 版本 0.2.4.1 修正mpg123状态异常导致的cpu占用，增加歌词双行显示功能

2017-03-17 版本 0.2.4.0 修复通知可能造成的崩溃

2017-03-03 版本 0.2.3.9 邮箱用户登录修复

2017-03-02 版本 0.2.3.8 登录接口修复

2016-11-24 版本 0.2.3.7 新增背景色设置

2016-11-07 版本 0.2.3.6 已知错误修复

2016-10-16 版本 0.2.3.5 新增进入歌曲专辑功能

2016-10-13 版本 0.2.3.4 新增查看歌曲评论

2016-09-26 版本 0.2.3.3 keybinder 错误修复

2016-09-15 版本 0.2.3.2 已知错误修复

2016-09-12 版本 0.2.3.1 已知错误修复

2016-09-11 版本 0.2.3.0 Python 2 和 3 支持

2016-05-09 版本 0.2.2.10 修复最后一行歌名过长的问题

2016-05-08 版本 0.2.2.9 缓存问题修复

2016-05-07 版本 0.2.2.8 解决通知在Gnome桌面持续驻留（#303）的问题

[更多>>](https://github.com/darknessomi/musicbox/blob/master/ChangeLog.md)

### The MIT License (MIT)

CopyRight (c) 2015 omi <[4399.omi@gmail.com](mailto:4399.omi@gmail.com)>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.