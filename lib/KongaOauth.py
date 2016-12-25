#!/usr/bin/python

# Copyright (c) 2016 Precious Kindo
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import sys, time, urllib
import json, requests

version = '1.0.0'

class KongaOauth():
    """
    Oauth Object Constructor  
    :input merchant_id  
    :input client_secret  
    :input is_test 
    """
    result = False
    error = False

    __merchant_id = False
    __access_token = False
    __client_secret = False
    __refresh_token = False
    __is_test = True

    __oauth_url = None
    __oauth_client_secret = False

    def __init__(self, **kwargs):

        # Get (required) keys...
        if kwargs.has_key('merchant_id'):
            self.__merchant_id = kwargs['merchant_id']
        else:
            # merchant_id is required but not specified, raise exception
            raise NameError('MerchantIdRequired', 'Merchant id is required, but not specified')

        # Get (required) keys...
        if kwargs.has_key('client_secret'):
            self.__client_secret = kwargs['client_secret']
        else:
            # client_secret is required but not specified, raise exception
            raise NameError('ClientSecretRequired', 'client secret is required, but not specified')

        # Get (optional) key...
        if kwargs.has_key('is_test'):
            self.__is_test = kwargs['is_test']

    def versionInfo(self):
        sys.stderr.write("Using KongaPay Python version:%s\n" % (version))

    def KPUrl(self):
        return 'https://staging-auth.kongapay.com' if self.__is_test else 'https://auth.kongapay.com'

    # 'Performs an API call
    def __KPConnect(self, url, method, params = '', decode = True):
        http_status = None
        self.result = None
        self.error = False

        fields = '' 

    def set_KPAccessToken(self, token):
        self.__access_token = self.token

    def get_KPAccessToken(self):
        if not self.__access_token:   
            self.__access_token = self.__Generate_KPAccessToken()
        return self.__access_token

    def __Generate_KPAccessToken(self):
        KPaccessCode = self.__Fetch_KPAccessCode()
        return KPaccessCode

    # 'Fetches OAuth2 Access Code
    def __Fetch_KPAccessCode(self):
        kp_end_point = '/authorize?response_type=code&client_id=%s&state=%s' % (self.__merchant_id, time.time())
        return kp_end_point

    # 'Fetches OAuth2 Access Token from the OAuth2 Access Code
    def __Fetch_KPAccessTokenByAccessCode(self, token):
        # Construct query string
        data = {
            'grant_type': 'authorization_code',
            'code': token,
            'client_id': self.__merchant_id,
            'client_secret': self.__client_secret
        }

        kp_end_point = '/token'

        #self.__KPConnect()

    # 'Refresh Access Token using Refresh token
    def Refresh_KPAccessToken(self, token):
        # Construct query string
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': token,
            'client_id': self.__merchant_id,
            'client_secret': self.__client_secret
        }

        kp_end_point = '/token'

        #self.__KPConnect()

    def get_KPRefreshToken(self):
        return self.__refresh_token

    def set_KPRefreshToken(self, token):
        self.__refresh_token = token