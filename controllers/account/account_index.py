from google.appengine.ext import ndb

from controllers.account.account_base import AccountBaseHandler


class IndexBaseHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self):
        self.render_template('index.html')