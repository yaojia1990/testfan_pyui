#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-24 22:16
# @Author  : YaoJa
import requests


if __name__ == "__main__":
    r = requests.get("http://www.baidu.com")
    print(r.text)
