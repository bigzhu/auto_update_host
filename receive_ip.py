#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado
import tornado.web
import tornado.autoreload
import save_local


the_ip = ''


def getURLMap(the_globals):
    '''
        根据定义的tornado.web.RequestHandler,自动生成url map
    '''
    url_map = []
    for i in the_globals:
        try:
            if issubclass(the_globals[i], tornado.web.RequestHandler):
                url_map.append((r'/' + i, the_globals[i]))
                url_map.append((r"/%s/(.*)" % i, the_globals[i]))
        except TypeError:
            continue
    return url_map


class setIP(tornado.web.RequestHandler):

    '''登录页面'''

    def get(self, ip):
        global the_ip
        the_ip = ip
        save_local.saveHosts(ip)
        self.write("ok")


class getIP(tornado.web.RequestHandler):

    '''登录页面'''

    def get(self):
        global the_ip
        self.write(the_ip)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 9001
    print port

    # routeo
    url_map = getURLMap(globals().copy())

    application = tornado.web.Application(url_map)

    application.listen(port)

    ioloop = tornado.ioloop.IOLoop().instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
