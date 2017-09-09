# -*- coding: utf-8 -*-
# structure based on nicholasamorim/chuk
import os
import sys
import json
import base64
import logging
from collections import namedtuple
from helper_functions import merge_two_dicts, log_bulk, debug_bulk

if (sys.version_info > (3, 0)):
    # Python 3
    from urllib.request import urlopen, Request
    from urllib.parse import urljoin, urlencode
else:
    # Python 2
    from urlparse import urljoin
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError

from constants import DEBUG_DATA_LEVEL, STOP_TYPES



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
        debug_bulk(url, payload, auth)

        if payload is None:
            payload = {}

        if auth is not None:
            payload = merge_two_dicts(payload, auth)
        full_url = '{}?{}'.format(url, urlencode(payload))

        debug_bulk(payload, full_url)

        request = Request(full_url)

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
        logging.info("TfLAPI instance being created")
        debug_bulk(app_id, app_key, url)


        if app_id is None or app_key is None:
            self._app_id = None
            self._app_key = None
            logging.info("Anoymous use of API, please initialise API with an app_id and app_key")  # Replace by logging

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
        debug_bulk(method, endpoint, parameters)

        method = getattr(self._client, method.lower())
        url = urljoin(self._url, endpoint)
        if parameters is None:
            parameters = {}
        parameters = merge_two_dicts(parameters, self.get_credentials())

        return self._client.get(url, parameters, None)

    def _serialize(self, data):
        logging.log(DEBUG_DATA_LEVEL, data)
        return self._serializer.loads(data)

    def _wrap(self, endpoint, parameters=None, method='get'):
        """Internal method used to make the request and wrap the response.
        """
        status, data = self._make_request(method, endpoint, parameters)
        logging.debug(status)
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
    
    def get_line_arrivals(self, Line, StopPoint):
        debug_bulk(Line, StopPoint)

        endpoint = 'Line/{}/Arrivals'.format(Line)
        parameters = {"stopPointID" : StopPoint}
        return self._wrap(endpoint, parameters)

    def get_arrivals(self, StopPoint):
        endpoint = 'StopPoint/{}/Arrivals'.format(StopPoint)
        return self._wrap(endpoint)

    def get_stop_points_by_location(self, lat, lon, stopTypes = STOP_TYPES, radius = None):
        """Given a location (lat, lon) will return a the stop points near a radius (200mts default)
        Still to add other parameters """
        debug_bulk(lat, lon, stopTypes, radius)

        endpoint = 'StopPoint'
        parameters = {
            "lat" : lat,
            "lon" : lon,
            "stopTypes" : ",".join(stopTypes),
        }

        if radius is not None:
            parameters["radius"] = radius

        return self._wrap(endpoint, parameters)


