from google.appengine.ext import ndb

from controllers.handler_base import BaseHandler


class IndexHandler(BaseHandler):
    @ndb.toplevel
    def get(self):
        self.render_template('index.html')