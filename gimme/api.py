#!/usr/bin/env python3

import json
from urllib.parse import quote

import requests


class GimmeResponse(object):

    """
    Attributes:
        headers: The headers from GimmeCall.headers.
        payload: The payload sent to the Gimme API.
    """


class GimmeResponseList(list, GimmeResponse):
    pass


class GimmeResponseDict(dict, GimmeResponse):
    pass


class GimmeCall(object):
    host = 'https://gimme.co.kr:6001/'

    user_agent = 'gimmeSponsor/1.055 (iPad; iOS 7.1.1; Scale/2.00)'

    client_headers = {
        'User-agent': user_agent,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-us;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}

    def __init__(self, auth_token, **kwargs):
        self.auth_token = auth_token
        self._kwargs = kwargs

        self.text = self._get_text()
        self.dict = json.loads(self.text)

    @property
    def payload(self):
        payload = {}

        for kw in self._kwargs:
            payload[kw] = self._kwargs[kw]

        payload['authToken'] = self.auth_token

        data = {'_JSON_': json.dumps(payload)}
        return data

    def _get_text(self):
        self.req = requests.post(self.host,
                                 headers=self.client_headers,
                                 data=self.payload)

        self.headers = self.req.headers
        self.req.raise_for_status()
        return self.req.text


def GimmeRequest(auth_token, **kwargs):
    """A wrapper for the GimmeCall response and GimmeResponse lists/dicts."""
    request = GimmeCall(auth_token, **kwargs)
    data = request.dict

    if data['code'] != 'SUCCESS':
        raise ValueError('Gimme API returned error: {} for payload: {}'.format(
            data['code'],
            repr(request.payload)))

    # The API returns a dictionary, but we want to wrap and return the
    # actual relevant data returned, which can be either a list or dictionary.
    data_keys = [k for k in data if k not in ('code')]

    # If the dictionary returned by the API for whatever reason has more than
    # two keys in it, we instead wrap the full dictionary.
    if len(data_keys) != 1:
        response = GimmeResponseDict(data)
    else:
        data_key = data_keys[0]
        data_type = type(data[data_key])
        if data_type is list:
            response = GimmeResponseList(data[data_key])
        elif data_type is dict:
            response = GimmeResponseDict(data[data_key])

    response.headers = request.headers
    response.payload = request.payload

    return response


if __name__ == "__main__":
    pass
