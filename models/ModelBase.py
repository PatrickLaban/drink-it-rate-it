from google.appengine.ext import ndb


class ModelBase(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    def save(self):
        # TODO: Add memcache controllers
        self.put()
