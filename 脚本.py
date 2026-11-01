import PyInstaller.__main__
from pathlib import Path
'''
import os
import sys

# resource
base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(base_dir)
'''
PyInstaller.__main__.run([
    '研学文字简介.py',
    '--add-data=ooooo;ooooo',
    '-n=汉字的渊源', 
    '-w',
    '-i=ooooo/研学文字.ico', 
    '-y', # 替换输出目录
])