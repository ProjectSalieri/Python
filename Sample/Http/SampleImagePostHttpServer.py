# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleImagePostHttpServer.py
# @note 

from http.server import HTTPServer, BaseHTTPRequestHandler

import urllib.parse

class SampleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        import os
        import re
        sample_html = os.path.join(os.path.abspath(os.getcwd()), self.path[1:]) # self.pathは「/」から始まる。joinの仕様のため先頭「/」を削除
        body = b""
        try:
            with open(sample_html) as f:
                content = f.read()
                ret = re.search('<body>(.*)</body>', content, re.DOTALL)
                body = ret.groups()[0].encode()
        except:
            error_str = ""
            for e_str in sys.exc_info():
                error_str += str(e_str) + "\n"
            print(error_str)
            body = ('<h3><font color=\"#ff0000\">' + html_path + "<br>" + error_str.replace(">", "&gt;").replace("<", "&lt;").replace("\n", "<br>") + '</font></h3>').encode()
            
        parse_result = urllib.parse.urlparse(self.path)
        #print(parse_result)

        # URLパラメータ解析
        url_params = urllib.parse.parse_qs(parse_result.query)

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

    def do_POST(self):
        body = b'Post'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

        #content_len=int(self.headers.get('content-length'))
        #post_body = self.rfile.read(content_len)
        #print(post_body)

        # POST されたフォームデータを解析する
        import cgi
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # フォームに POST されたデータの情報を送り返す
        import os
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # field はアップロードされたファイルを含みます
                file_data = field_item.file.read()
                file_len = len(file_data)
                print('\tUploaded %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
                tmp_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "tmp.jpg")
                with open(tmp_file, "wb") as f:
                    f.write(file_data)
            else:
                # 通常のフォーム値
                print('\t%s=%s\n' % (field, form[field].value))

# test code
if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    httpd = HTTPServer((host, port), SampleHandler)
    print('serving at port', port)
    httpd.serve_forever()
