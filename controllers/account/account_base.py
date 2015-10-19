import google.appengine.api.users

from controllers.handler_base import BaseHandler


class AccountBaseHandler(BaseHandler):
    def __init__(self, request, response):
        super(AccountBaseHandler, self).__init__(request, response)
        if self.user_account is None:
            login_url = google.appengine.api.users.create_login_url(self.request.path)
            self.redirect(login_url)
            return
        self.template_values["logout_url"] = google.appengine.api.users.create_logout_url("/")
