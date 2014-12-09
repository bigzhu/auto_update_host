#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import sys
import time
the_ip = ''


def sendIP():
    global the_ip
    ip = json.load(urllib2.urlopen('http://httpbin.org/ip'))['origin']
    if the_ip != ip:
        urllib2.urlopen('http://42.96.204.146:9001/setIP/%s' % ip)
        the_ip = ip
        print 'new ip = %s' % ip
    else:
        print 'ip = %s not change' % ip

if __name__ == '__main__':
    while True:
        try:
            sendIP()
        except Exception:
            info = sys.exc_info()
            print str(info[1])
        time.sleep(5)
