#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado
import tornado.web
import tornado.autoreload


def getURLMap(the_globals):
    '''
        根据定义的tornado.web.RequestHandler,自动生成url map
    '''
    url_map = []
    for i in the_globals:
        try:
            if issubclass(the_globals[i], tornado.web.RequestHandler):
                url_map.append((r'/' + i, the_globals[i]))
                #url_map.append((r"/%s/([0-9]+)" % i, the_globals[i]))
                url_map.append((r"/%s/(.*)" % i, the_globals[i]))
        except TypeError:
            continue
    return url_map


class setIP(tornado.web.RequestHandler):

    '''登录页面'''

    def get(self, ip):
        print ip
        saveHosts(ip)
        self.write("ok")


def saveHosts(ip):
    path_file = '/etc/hosts'
    with open(path_file) as f:
        lines = f.readlines()
        print lines
        curr = lines[:-1]
        f.close()
    f = open(path_file, 'w')
    curr.append(u'%s mygit\n' % ip)
    f.writelines(curr)
    f.close()

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 9000
    print port

    # routeo
    url_map = getURLMap(globals().copy())

    application = tornado.web.Application(url_map)

    application.listen(port)

    ioloop = tornado.ioloop.IOLoop().instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
