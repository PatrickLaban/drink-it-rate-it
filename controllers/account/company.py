import json

from google.appengine.ext import ndb

from models.Company import Company
from models.CompanyAccount import CompanyAccount
from controllers.account.account_base import AccountBaseHandler


class CompanyInfoHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self, company_id):
        company = Company.get_by_id(int(company_id))
        self.response.write(company.name)


class CompanyCreateHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self):
        self.render_template('account/company/company_new_edit.html')


    @ndb.toplevel
    def post(self):
        name = self.request.get('name')
        if Company.query(Company.name == name).count() > 0:
            response = {'success': False, 'error_message': "A company already exists with the name {0}".format(name)}
            self.response.write(json.dumps(response))
            return
        new_company = Company.create_company(name)
        _ = CompanyAccount.create_company_account(company=new_company, user_account=self.user_account)
        response = {'success': True, 'goto_url': '/account/company/{0}'.format(new_company.key.id())}
        self.response.write(json.dumps(response))


class CompanyEditHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self, company_id):
        company = Company.get_by_id(int(company_id))
        self.template_values['company'] = company
        self.render_template('account/company/company_new_edit.html')

    @ndb.toplevel
    def put(self, company_id):
        company = Company.get_by_id(int(company_id))
        name = self.request.get('name')
        if Company.query(Company.name == name).count() > 0:
            response = {'success': False, 'error_message': "A company already exists with the name {0}".format(name)}
            self.response.write(json.dumps(response))
            return
        company.edit_company(name=name)
        response = {'success': True, 'goto_url': '/account/company/{0}'.format(company.key.id())}
        self.response.write(json.dumps(response))