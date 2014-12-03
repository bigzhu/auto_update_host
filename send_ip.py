#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
the_ip = ''


def sendIP():
    global the_ip
    ip = json.load(urllib2.urlopen('http://httpbin.org/ip'))['origin']
    if the_ip != ip:
        urllib2.urlopen('http://42.96.204.146:8009/setIP/%s' % ip)
        the_ip = ip

if __name__ == '__main__':
    sendIP()
