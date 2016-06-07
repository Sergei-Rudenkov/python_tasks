import tornado.web
from tornado import gen, httpclient
import json


class StackOverflowHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, look_up_pattern):
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=votes&intitle=%s&site=stackoverflow&page=1&pagesize=1"
        response = yield self.async_get(url % look_up_pattern)
        data = json.loads(response)
        data = [n['link'] for n in data['items']]
        response_json = {'links': data,
                         'lookup': look_up_pattern}
        self.write(response_json)

    @gen.coroutine
    def async_get(self, url):
        link = httpclient.AsyncHTTPClient()
        request = httpclient.HTTPRequest(url)
        response = yield link.fetch(request)
        data = response.body.decode('utf-8')
        return data


application = tornado.web.Application([
    (r"/search/(.*)", StackOverflowHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
