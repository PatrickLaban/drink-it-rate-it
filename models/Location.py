from google.appengine.ext import ndb

from ModelBase import ModelBase


class Location(ModelBase):
    name = ndb.StringProperty(required=True)
    country = ndb.StringProperty(default="USA")
    state = ndb.StringProperty(default="Washington")
    city = ndb.StringProperty(default="Seattle")
    location_type = ndb.StringProperty()
    company_key = ndb.KeyProperty(kind='Company')

    def __init__(self, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)
        self._company = None

    @property
    def company(self):
        if self._company is None and self.company_key is not None:
            self._company = Company.get_by_id(self.company_key.id())
            return self._company
        return None

    @classmethod
    def create_location(cls, **kwargs):
        new_location = Location(
            name=kwargs['name'],
            location_type=kwargs['location_type'],
            adult_ads_restricted=kwargs['adult_ads_restricted'],
        )
        new_location.put()
        return new_location
        #
        #
        # def edit_company(self, name):
        # self.name = name
        #     self.put()
