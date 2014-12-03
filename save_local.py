#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2


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
    ip = urllib2.urlopen('http://42.96.204.146:9001/getIP').read()
    if ip != '':
        saveHosts(ip)
