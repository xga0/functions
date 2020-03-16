#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:58:33 2020

@author: seangao
"""

from urllib import parse

def getSite(url):
    site_url = parse.urlsplit(url).netloc
    site_list = site_url.split('.')
    site = site_list[1]
    return site

#TEST
url = 'https://www.nytimes.com/2020/03/16/us/coronavirus-hype-overreaction-social-distancing.html?action=click&module=Top%20Stories&pgtype=Homepage'
print(getSite(url))

