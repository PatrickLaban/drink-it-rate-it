from google.appengine.ext import ndb

from ModelBase import ModelBase
from Company import Company


class CompanyAccount(ModelBase):
    company_key = ndb.KeyProperty(kind="Company")
    user_account_key = ndb.KeyProperty(kind="UserAccount")
    access_level = ndb.IntegerProperty(default=100)

    def __init__(self, *args, **kwds):
        super(CompanyAccount, self).__init__(*args, **kwds)
        self._company = None

    @property
    def company(self):
        if self._company is None:
            self._company = Company.get_by_id(self.company_key.id())
        return self._company

    @classmethod
    def create_company_account(cls, company, user_account):
        company_key = company.key
        user_account_key = user_account.key
        new_company_account = CompanyAccount(company_key=company_key, user_account_key=user_account_key)
        new_company_account.put()
        return new_company_account
