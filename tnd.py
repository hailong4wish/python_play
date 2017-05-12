import tornado.ioloop
import tornado.web
import tornado.httpclient
import time

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("https://www.google.com.hk",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        # json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + response.body + " entries "
                   "from the FriendFeed API")
        self.finish()
        # print("... code continue goes...")
        # time.sleep()
        # print(".. until now return")
        # return

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()