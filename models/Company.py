from google.appengine.ext import ndb

from ModelBase import ModelBase


class Company(ModelBase):
    name = ndb.StringProperty(required=True)

    @classmethod
    def create_company(cls, name):
        new_company = Company(name=name)
        new_company.put()
        return new_company

    def edit_company(self, name):
        self.name = name
        self.put()


