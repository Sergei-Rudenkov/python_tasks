import tornado.web
from tornado import gen, httpclient, httputil
import json


class StackOverflowHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, look_up_pattern):
        """
        GET request controller for /search/(.*) endpoint
        returns json: link to the most ranked question, lookup string
        """
        url = httputil.url_concat("https://api.stackexchange.com/2.2/search?order=desc",
                                          [("sort", "votes"),
                                           ("intitle", look_up_pattern),
                                           ("site", "stackoverflow"),
                                           ("page", "1"),
                                           ("pagesize", "1")])
        response = yield self.fetch_so(url)
        data = json.loads(response)
        data = [n['link'] for n in data['items']]
        response_json = {'links': data,
                         'lookup': look_up_pattern}
        self.write(response_json)

    @gen.coroutine
    def fetch_so(self, url):
        """
        Fetching json using StackExchange API 2.2
        """
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
