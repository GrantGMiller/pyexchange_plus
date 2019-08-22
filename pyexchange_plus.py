from pyexchange import log, Exchange2010Service
from pyexchange.connection import ExchangeBaseConnection
from pyexchange.exceptions import FailedExchangeException
import requests


class ExchangeOauthConnection:
    """ Connection to Exchange that uses Oauth authentication """

    def __init__(self, url, access_token, **kwargs):
        self.url = url
        self._access_token = access_token

        self.handler = None
        self.session = requests.session()
        self.password_manager = None

    def build_password_manager(self):
        return

    def build_session(self):
        return self.session

    def send(self, body, headers=None, retries=2, timeout=30, encoding=u"utf-8"):

        headers = headers or dict()
        headers.update({'Authorization': 'Bearer {}'.format(self._access_token)})

        try:
            response = self.session.post(self.url, data=body, headers=headers)
            print('101 response.headers=', response.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            log.debug(err.response.content)
            raise FailedExchangeException(u'Unable to connect to Exchange: %s' % err)

        log.info(u'Got response: {code}'.format(code=response.status_code))
        log.debug(u'Got response headers: {headers}'.format(headers=response.headers))
        log.debug(u'Got body: {body}'.format(body=response.text))

        return response.text


class ExchangeBasicAuthConnection(ExchangeBaseConnection):
    """ Connection to Exchange that uses Basic authentication """

    def __init__(self, url, username, password, **kwargs):
        self.url = url
        self.username = username
        self.password = password

        self.handler = None
        self.session = requests.session()
        self.session.auth = (self.username, self.password)
        self.password_manager = None

    def build_password_manager(self):
        return

    def build_session(self):
        return self.session

    def send(self, body, headers=None, retries=2, timeout=30, encoding=u"utf-8"):

        try:
            response = self.session.post(self.url, data=body, headers=headers)
            print('101 response.headers=', response.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            log.debug(err.response.content)
            raise FailedExchangeException(u'Unable to connect to Exchange: %s' % err)

        log.info(u'Got response: {code}'.format(code=response.status_code))
        log.debug(u'Got response headers: {headers}'.format(headers=response.headers))
        log.debug(u'Got body: {body}'.format(body=response.text))

        return response.text


class Office365Service(Exchange2010Service):
    pass
