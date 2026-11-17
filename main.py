#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""启动入口垫片:有些部署平台默认找 main.py,而本项目入口是 app.py。
直接运行本文件等价于运行 app.py。"""
import runpy
from pathlib import Path

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).parent / 'app.py'), run_name='__main__')
