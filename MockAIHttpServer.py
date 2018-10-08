# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAIServer.py
# @note 

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from MockAI import MockAI

import concurrent.futures

class MockAIHttpHandler(BaseHTTPRequestHandler):

    # クラス変数
    ai = MockAI.create_mock_ai()

    def do_GET(self):
        url_params = self._get_url_param()

        if MockAIHttpHandler._is_valid_bool_param(url_params, "shutdown"):
            print("shutdown")
            import sys
            sys.exit(0)
        elif MockAIHttpHandler._is_valid_bool_param(url_params, "test"):
            # スレッド処理
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            executor.submit(MockAIHttpHandler.ai.look("./EyeSensor/SampleImage/Apple.jpg"))

        print("end get request", self.path)
    # def do_GET

    def do_POST(self):
        pass
    # def do_POST

    def _get_url_param(self):
        parse_result = urllib.parse.urlparse(self.path)
        url_params = urllib.parse.parse_qs(parse_result.query)
        return url_params
    # def _getURLParam

    def _is_valid_bool_param(url_params, key):
        if key in url_params and 'true' in url_params[key]:
            return True
        else:
            return False
# class MockAIHttpHandler

class MockAIHttpServer(HTTPServer):
    def __init__(self, info, handler):
        HTTPServer.__init__(info, handler)
# class MockAIHttpServer

if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    httpd = HTTPServer(
        (host, port),
        MockAIHttpHandler
    )
    print('serving at port', port)
    httpd.serve_forever()
