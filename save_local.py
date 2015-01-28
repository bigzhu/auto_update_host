#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import time
#公司有多条宽带, ip 会变化,因此用一个 list 来存放,避免反复写 hosts
ip_list = []


def saveHosts(ip):
    path_file = '/etc/hosts'
    with open(path_file) as f:
        lines = f.readlines()
        curr = lines[:-1]
        f.close()
    f = open(path_file, 'w')
    curr.append(u'%s mygit\n' % ip)
    f.writelines(curr)
    print 'now hosts is:'
    for i in curr:
        print i
    f.close()

if __name__ == '__main__':
    while True:
        try:
            new_ip = urllib2.urlopen('http://42.96.204.146:9001/getIP', timeout=10).read()
            if new_ip != '' and new_ip not in ip_list:
                saveHosts(new_ip)
                ip_list.append(new_ip)
                if len(ip_list) > 4:
                    ip_list = []
            else:
                print 'same ip'
        except Exception:
            print "出错了"
        time.sleep(5)
