__author__ = 'Hao'

import tornado.ioloop
import tornado.web
import tornado.websocket

mobile_write = 0

class WebControlSocket(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket HTML opened")

    def on_message(self, message):
        #self.write_message(u"You said: " + message)
        print message
        if mobile_write!= 0:
            mobile_write(message)

    def on_close(self):
        print("WebSocket closed")

class MobileGimbalSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WS Mobile Opened")
        if mobile_write == 0:
            mobile_write = self.write_message

    def on_message(self, message):
        print message

    def on_close(self):
        pass
    
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/html_controller_server" , WebControlSocket),
    (r"/android",MobileGimbalSocket),
])

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.current().start()