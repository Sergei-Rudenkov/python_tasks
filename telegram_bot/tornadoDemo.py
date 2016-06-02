import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Sergei, Welcome to Tornado Web Framework.")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#http://www.tutorialsavvy.com/2013/11/getting-started-with-tornado-web-framework.html/