# Copyright (c) 2016 Precious Kindo
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

#!/usr/bin/env python

import json
import requests

class KongaOauth():
  """
  Oauth Object Constructor
  :input oauth_merchant_id
  :input oauth_client_secret
  :input is_test
  """
  self.version = '1.0.0'
  self.OAUTH_ENDPOINT_URL = 'http://api.smsgh.com/v3/messages/send'
  self.oauth_merchant_id = oauth_merchant_id
  self.oauth_client_secret = oauth_client_secret
  self.oauth_access_token = False
  self.refresh_token = False
  self.error = False
  self.is_test = is_test

  def __init__(self, **kwargs oauth_merchant_id=None, oauth_client_secret=None, is_test=True):
    

  def send(self, **kwargs):
    sender_id = kwargs['sender'] if kwargs['sender'] else self.api_senderid
    response = None
    if not kwargs['msg'] or not kwargs['receiver']:
      raise ValueError("*msg and *to params expected")

    if self.api_client_id != None and self.oauth_client_secret != None:
      payload = {
      'From': sender_id,
      'To': kwargs['receiver'],
      'Content': kwargs['msg'],
      'ClientId': self.api_client_id,
      'ClientSecret': self.oauth_client_secret 
      }
      response = requests.post(self.SMSGH_ENDPOINT_URL, data=payload)
    print(response)
    