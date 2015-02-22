#!/usr/bin/env python3

import json

from gimme.api import GimmeRequest, GimmeCall
from gimme.auth import GimmeAuth


class Gimme(object):

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def request(self, check_sucsess=True, **kwargs):
        req = GimmeRequest(self.auth_token, **kwargs)
        return req

    def follow_user(self, username):
        kwargs = {'cmd': 'set_favorite_celebrity_insert',
                  'celebrityCode': username}
        return self.request(**kwargs)

    def unfollow_user(self, username):
        kwargs = {'cmd': 'set_favorite_celebrity_delete',
                  'celebrityCode': username}
        return self.request(**kwargs)

    def timeline(self, username=False, type=0, max_timestamp=False):
        kwargs = {}
        if username:
            kwargs['cmd'] = 'get_celebrity_message_list_for_fan'
            kwargs['code'] = username
        else:
            kwargs['cmd'] = 'get_celebrity_timeline_list'

        kwargs['type'] = str(type)

        if max_timestamp:
            kwargs['createdAt'] = max_timestamp

        return self.request(**kwargs)

    def itimeline(self, username=False, type=0, max_timestamp=False):
        """Like timeline(), except that it returns an generator and yields
        messages until it hits an empty feed."""

        max_timestamp = max_timestamp
        while True:
            feed = self.timeline(type=type,
                                 username=username,
                                 max_timestamp=max_timestamp)

            if len(feed) == 0:
                break

            yield feed
            max_timestamp = feed[-1]['createdAt']

    @property
    def user_info(self):
        kwargs = {'cmd': 'get_my_profile'}
        response = self.request(**kwargs)
        return response

    @property
    def follows(self):
        kwargs = {'cmd': 'get_favorite_celebrity_list'}
        return self.request(**kwargs)

    @property
    def celebrities(self):
        kwargs = {'cmd': 'get_celebrity_list'}
        return self.request(**kwargs)

if __name__ == "__main__":
    pass
