#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2

def sendIP():
    ip = json.load(urllib2.urlopen('http://httpbin.org/ip'))['origin']
    urllib2.urlopen('http://0.0.0.0:8009/setIP/%s' % ip)

if __name__ == '__main__':
    sendIP()
