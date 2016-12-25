#!/usr/bin/python

# Copyright (c) 2016 Precious Kindo
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from lib.KongaOauth import KongaOauth 

KO = KongaOauth(merchant_id='xxxxxxx', client_secret='xxxxxxx')

# 'API version
KO.versionInfo()