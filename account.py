import webapp2

import controllers.account.account_index
import controllers.account.company
import controllers.account.location


app = webapp2.WSGIApplication(
    [('/account/company_create/?', controllers.account.company.CompanyCreateHandler),
     ('/account/company_edit/(\d+)', controllers.account.company.CompanyEditHandler),
     ('/account/company/(\d+)', controllers.account.company.CompanyInfoHandler),
     ('/account/location_create/?', controllers.account.location.LocationCreateHandler),
     ('/account/?', controllers.account.account_index.IndexBaseHandler),
    ], debug=True)
