#!/usr/bin/python3
# coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpclient
from searchQ import searchQ

class Searchhandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        key = self.get_argument("key")
        seap = searchQ()
        p = seap.search(qm=key)
        self.write(p)

    def post(self):
        key = self.get_argument("key")
        seap = searchQ()
        p = seap.search(qm=key)
        self.write(p)
