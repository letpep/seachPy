#!/usr/bin/python3
# coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpclient
from python.coreseek.searchQ import searchQ

class Searchhandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://www.baidu.com")
        self.write(response.body)

    def post(self):
        key = self.get_argument("key")
        seap = searchQ()
        p = seap.search(qm=key)
        self.write(p)
