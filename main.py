import webapp2

from controllers.index import IndexHandler


app = webapp2.WSGIApplication([
                                  ('/', IndexHandler)
                              ], debug=True)
