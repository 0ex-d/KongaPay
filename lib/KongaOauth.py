# Copyright (c) 2016 Precious Kindo
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

#!/usr/bin/env python

import json
import requests

version = '1.0.0'

class KongaOauth():
    result = False
    error = False

    __app_id = False
    __key = False
    __secret = False
    __channels = {}
    __globals = {}

    def __init__(self, **kwargs oauth_merchant_id=None, oauth_client_secret=None, is_test=True):
    	pass
