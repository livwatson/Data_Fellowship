# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:21:54 2021

@author: owatson2
"""

import tweepy

api = tweepy.api()
auth = tweepy.0AuthHandler("apikey", "apisecret")
auth.set_access_token("accesstoken", "accesssecret")
