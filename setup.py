#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
*************************************************
*
* @author  : Free_zhang
* @license :
* @email   : blossom_zhang@163.com
* @software:
* @file    : __init__.py.py
* @time    : 2017/12/17 19:13
* @desc    : 
*
*************************************************
"""

import re
import codecs

from setuptools import find_packages, setup

with codecs.open('wxpy/__init__.py',encoding='utf-8') as fp:
    version =re.search(r"__version__\s*=\s*'([\w\-.]+)",fp.read()).group(1)

with codecs.open('README.rst',encoding='utf-8') as fp:
    readme = fp.read()

setup(
    name='wxpy',
    version=version,
    packages=find_packages,
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'wxpy = wxpy.utils:shell_entry'
        ]
    },
    install_requires=[
        'itchat==1.2.32',
        'requests',
        'future',
    ],
    tests_require=[
        'pytest',
    ],
    url='https://github.com/youfou/wxpy',
    license='MIT',
    author='free_zhang',
    author_email='blossom_zhang@163.com',
    description='微信机器人 / 可能是最优雅的微信个人号API',
    long_description=readme,
    keywords=[
        '微信',
        'Wechat',
        'API',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Pyton',
        'Programming Language :: Pyton :: 2.7',
        'Programming Language :: Pyton :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Utilities',
    ]
)