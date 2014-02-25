import tornado.web
import tornado.wsgi

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello 测试中文 tornado!<br><a href="/source">View the source code</a>')

class ViewHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type","text/plain")
        code = ["##requirements.txt:"]
        code.append(open("requirements.txt").read())
        code.append("##wsgi.py:")
        code.append(open("wsgi.py").read())
        self.write("\n\n".join(code))

application = tornado.wsgi.WSGIApplication([
(r"/", MainHandler),
(r"/source", ViewHandler),
])


if __name__ == "__main__":
    import wsgiref.simple_server
    server = wsgiref.simple_server.make_server('', 8888, application)
    server.serve_forever()