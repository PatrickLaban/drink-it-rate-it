import json

from google.appengine.ext import ndb

from models.Location import Location
from controllers.account.account_base import AccountBaseHandler


class LocationHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self, location_id):
        location = Location.get_by_id(int(location_id))
        self.template_values['location'] = location
        self.response.out.write("boop")


class LocationCreateHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self):
        self.render_template('account/location/location_new_edit.html')

    @ndb.toplevel
    def post(self):
        location_kwargs = {
            'name': self.request.get('name'),
            'location_type': self.request.get('location-type'),
        }
        new_location = Location.create_location(**location_kwargs)
        response = {'success': True, 'goto_url': '/account/location/{0}'.format(new_location.key.id())}
        self.response.write(json.dumps(response))
