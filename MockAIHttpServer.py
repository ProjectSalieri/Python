# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAIServer.py
# @note 

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

# AI
from AI import AIUtil
from AI import MockAI

import concurrent.futures
from multiprocessing import Process
import os
import re

class MockAIHttpHandler(BaseHTTPRequestHandler):

    # クラス変数 @fimxe 複数AI実装できないぞ。。。このクラスはリクエストごとにインスタンスがくる
    ai = None

    def do_GET(self):
        parse_result = self._parse_url()
        body = MockAIHttpHandler._create_body(parse_result["url_path"])
        url_params = {}
        if "url_query" in parse_result:
            url_params = parse_result["url_query"]

        if MockAIHttpHandler._is_valid_bool_param(url_params, "shutdown"):
            print("shutdown")
            import sys
            sys.exit(0)
        elif MockAIHttpHandler._is_valid_bool_param(url_params, "test"):
            # スレッド処理
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            executor.submit(MockAIHttpHandler.ai.look("./EyeSensor/SampleImage/Apple.jpg"))

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

        print("end get request", self.path)
    # def do_GET

    def do_POST(self):
        body = b'Post'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

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
                import tempfile
                # fixme .jpg以外 拡張子取得する fixme : tmp画像にすると、内部でプロセス処理にしたときに生存期間が...
                with tempfile.NamedTemporaryFile(suffix=".jpg", dir=AIUtil.ai_image_memory_path(), delete=False) as fp:
                    print(fp.name)
                    with open(fp.name, "wb") as f:
                        f.write(file_data)
                    # スレッド処理 スレッド処理と画像の生存期間が怪しいかも...
                    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
                    executor.submit(MockAIHttpHandler.ai.look(fp.name))
                    # テスト(本番は別スレッドでループしている)
                    #executor.submit(MockAIHttpHandler.ai._think_core())
                    #executor.submit(MockAIHttpHandler.ai._action_core())
            else:
                # 通常のフォーム値
                print('\t%s=%s\n' % (field, form[field].value))
    # def do_POST

    def _parse_url(self):
        parse_result = urllib.parse.urlparse(self.path)
        url_params = urllib.parse.parse_qs(parse_result.query)
        return {"url_query":url_params, "url_path":parse_result.path}
    # def _parse_url

    def _is_valid_bool_param(url_params, key):
        if key in url_params and 'true' in url_params[key]:
            return True
        else:
            return False

    def _get_html_path_from_handler_path(handler_path):
        return os.path.join(os.path.abspath(os.getcwd()), handler_path[1:]) # self.pathは「/」から始まる。joinの仕様のため先頭「/」を削除

    def _create_body(handler_path):
        html_path = MockAIHttpHandler._get_html_path_from_handler_path(handler_path)
        body = b''
        try:
            with open(html_path) as f:
                content = f.read()
                ret = re.search('<body>(.*)</body>', content, re.DOTALL)
                body = ret.groups()[0].encode()
        except:
            import sys
            error_str = ""
            for e_str in sys.exc_info():
                error_str += str(e_str) + "\n"
            print(error_str)
            body = ('<h3><font color=\"#ff0000\">' + html_path + "<br>" + error_str.replace(">", "&gt;").replace("<", "&lt;").replace("\n", "<br>") + '</font></h3>').encode()
            body += b'<br><h3><font color=\"#ff0000\">Recommend to go to [UserInterface/SimpleImagePost.html]</font></h3><br>'
        return body
# class MockAIHttpHandler

class MockAIHttpServer(HTTPServer):
    # クラス変数
    ai = MockAI.MockAI.create_mock_ai() # MockAIモジュールのMockAIクラスのクラススタテイック関数呼び出し
    
#    def __init__(self, info, handler):
#        HTTPServer.__init__(info, handler)
#        handler.ai = MockAIHttpServer.ai

    def activate_ai(self):
        process_list = []
        
        # AIのthinkとactionをスレッド実行
        print("think function register")
        p1 = Process(target=MockAIHttpHandler.ai.think)
        p1.start()
        process_list.append(p1)
        print("action function register")
        p2 = Process(target=MockAIHttpHandler.ai.action)
        p2.start()
        process_list.append(p2)
        
# class MockAIHttpServer

if __name__ == '__main__':
    # AI
    AIUtil.initialize()
    
    host = 'localhost'
    port = 8000
    httpd = MockAIHttpServer(
        (host, port),
        MockAIHttpHandler
    )
    MockAIHttpHandler.ai = httpd.ai
    httpd.activate_ai()
    print('serving at port', port)
    httpd.serve_forever()
