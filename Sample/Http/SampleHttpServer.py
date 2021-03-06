# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleHttpServer.py
# @note 

from http.server import HTTPServer, SimpleHTTPRequestHandler

import urllib.parse

class SampleHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        parse_result = urllib.parse.urlparse(self.path)
        #print(parse_result)

        # URLパラメータ解析
        url_params = urllib.parse.parse_qs(parse_result.query)

        body = b'Hello World<br>'
        # テーブルにURLパラメータ表示
        body = body + b'<table>'
        body = body + b'<thead><th>key</th><th>value</th></thead>'
        body = body + b'<tbody>'
        for param_name in url_params:
            for param in url_params[param_name]:
                param_str = '<td>' + param_name + '</td>' + '<td>' + param + "</td>"
                body += b'<tr>' + param_str.encode() + b'</tr>'
        body = body + b'</tbody>'
        body = body + b'</table>'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

# test code
if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    httpd = HTTPServer((host, port), SampleHandler)
    print('serving at port', port)
    httpd.serve_forever()
