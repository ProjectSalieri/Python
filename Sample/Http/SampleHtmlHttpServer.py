# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleHtmlHttpServer.py
# @note Httpサーバーで表示する情報をhtmlを使う

from http.server import HTTPServer, SimpleHTTPRequestHandler

import urllib.parse

class SampleHandler(SimpleHTTPRequestHandler):

    # オーバーライドしなければ、通常のHttpサーバー通り指定htmlがあれば内容を返す
    def do_GET(self):
        super().do_GET()

# test code
if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    httpd = HTTPServer((host, port), SampleHandler)
    print('serving at port', port)
    httpd.serve_forever()
