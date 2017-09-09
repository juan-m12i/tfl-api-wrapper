# -*- coding: utf-8 -*-
# structure based on nicholasamorim/chuk
import os
import sys
import json
import base64
import logging
from collections import namedtuple
from helper_functions import merge_two_dicts

if (sys.version_info > (3, 0)):
    # Python 3
    from urllib.request import urlopen, Request
    from urllib.parse import urljoin, urlencode
else:
    # Python 2
    from urlparse import urljoin
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError


Response = namedtuple('Response', ['code', 'data'])


class Client(object):
    """Encapsulated client. Used for
    """
    @staticmethod
    def post(*args, **kwargs):
        """Not implemented as TfL doesn't use anything other than GET.
        """
        raise NotImplementedError

    @staticmethod
    def get(url, payload=None, auth=None):
        """Performs a GET HTTP request.
        :param url: The url.
        :param payload: The parameters in a dictionary.
        :param auth: A tuple containing username and password.
        """
        if payload is None:
            payload = {}

        if auth is not None:
            payload = merge_two_dicts(payload, auth)
        full_url = '{}?{}'.format(url, urlencode(payload))
        request = Request(full_url)
        if auth is not None:
            base64_auth = base64.b64encode('{}{}'.format(auth[0], auth[1]))
            request.add_header("Authorization", "Basic {}".format(base64_auth))


        try:
            response = urlopen(request)
        except HTTPError as e:
            return e.code, None

        return response.code, response.read()


class TfLAPI(object):
    """A simple consumer for the TfL API
    You can find detailed documentation about the API here:
    https://api.tfl.gov.uk/
    """
    def __init__(self, app_id = None, app_key = None,
                 url='https://api.tfl.gov.uk/', **kwargs):
        """
        :param app_id: Application ID
        :param app_key: Application key
        :param url. The API base url
        Defaults to https://api.tfl.gov.uk/
        """

        if app_id is None or app_key is None:
            self._app_id = None
            self._app_key = None
            print("using anonymous")  # Replace by logging
        else:
            self._app_id = app_id
            self._app_key = app_key

        self._credentials = {
            "app_id": app_id,
            "app_key": app_key,
        }

        self._url = url
        self._serializer = kwargs.get('serializer', json)
        self._client = kwargs.get('client', Client)

    def _make_request(self, method, endpoint, parameters=None):
        """
        """
        method = getattr(self._client, method.lower())
        url = urljoin(self._url, endpoint)
        print(url)
        parameters = merge_two_dicts(parameters, self.get_credentials())
        print(parameters)

        return self._client.get(url, parameters, None)

    def _serialize(self, data):
        return self._serializer.loads(data)

    def _wrap(self, endpoint, parameters=None, method='get'):
        """Internal method used to make the request and wrap the response.
        """
        status, data = self._make_request(method, endpoint, parameters)
        return Response(status, self._serialize(data))

    def raw(self, method, endpoint, parameters=None):
        """Perform a raw request passing a custom endpoint and parameters.
        :param method: A string containing a http method. Currently TfL only supports GET requests.
        :param endpoint: A string containing an endpoint. E.g: "/Line/c2"
        :param parameters: An optional dictionary containg parameters.
        """
        return self._wrap(endpoint, parameters)

    def get_credentials(self):
        """
        """
        return (self._credentials)


    def get_authentication(self):
        """
        """
        return (self._key, ':')
    
    def get_bus_arrivals(self, Line, StopPoint):
        endpoint = 'Line/{}/Arrivals?stopPointId={}'.format(Line, StopPoint)
        return self._wrap(endpoint)

