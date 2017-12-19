#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
*************************************************
*
* @author  : Free_zhang
* @license :
* @email   : blossom_zhang@163.com
* @software:
* @file    : exceptions.py
* @time    : 2017/12/17 19:28
* @desc    : 
*
*************************************************
"""

from __future__ import unicode_literals


class ResponseError(Exception):
    """
        当BaseResponse的返回值不为0时抛出异常
    """

    def __init__(self,err_code,err_msg):
        super(ResponseError,self).__init__(
            'err_code: {}; err_msg: {}'.format(err_code,err_msg))
        self.err_code = err_code
        self.err_msg = err_msg