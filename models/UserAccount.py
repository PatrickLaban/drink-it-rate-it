import logging

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import memcache

from ModelBase import ModelBase


class AccountTypes(object):
    NORMAL = 0
    BUSINESS = 1
    INTERNAL_ADMIN = 2


class AccountStates(object):
    """
    Used to determine if the user has any restrictions.
    Possible states could include being banned from commenting.

    """

    ACTIVE = 0  # For now this will be the only state


class UserAccount(ModelBase):
    google_id = ndb.StringProperty()
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    type = ndb.IntegerProperty(choices=[AccountTypes.NORMAL, AccountTypes.BUSINESS, AccountTypes.INTERNAL_ADMIN],
                               default=AccountTypes.NORMAL)
    state = ndb.IntegerProperty(choices=[AccountStates.ACTIVE], default=AccountStates.ACTIVE)

    @classmethod
    def get_user_account(cls, account_method):
        """
        Gets the current user account based on the method
        :param account_method:
        This is the method to retreive the user account.  Currently only Google accounts are supported.

        :return:
        The instance of the user account for the current user.

        """

        if account_method == "google_user":
            user_account = cls.get_user_account_by_google_user_service()
        else:
            logging.error("Unsupported account method: {}".format(account_method))
            user_account = None
        return user_account

    @classmethod
    def get_user_account_by_google_user_service(cls):
        """
        Gets the current user account using the Google Users service.  If the user does not exist then create a new
        user based on the Google User.

        :return:
        The instance of the user account for the current user.

        """

        google_user = users.get_current_user()
        if google_user is None:
            return None
        user_account = memcache.get("{}:google_user_account".format(google_user.user_id()))
        if user_account is not None:
            return user_account
        user_account_query = cls.query(cls.google_id == google_user.user_id()).fetch()
        if user_account_query:
            user_account = user_account_query[0]
        else:
            user_account = UserAccount(google_id=google_user.user_id(),
                                       email=google_user.email(),
                                       name=google_user.nickname())
            user_account.save()
        if not memcache.add("{}:google_user_account".format(google_user.user_id()), user_account):
            logging.error("Memcache add Google user account failed")
        return user_account
