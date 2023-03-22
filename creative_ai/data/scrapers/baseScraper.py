#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import http.client
import urllib.error
import urllib.request
import codecs
import re
from time import sleep
from tqdm import tqdm

URL_ENCODINGS = {
                    "%20": " ", "%21": "!", "%22": '"', "%23": "#",
                    "%24": "$", "%25": "%", "%26": "&", "%27": "'",
                    "%28": "(", "%29": ")", "%2A": "*", "%2B": "+",
                    "%2C": ",", "%2D": "-", "%2E": ".", "%2F": "/"
                }

class BaseScraper(object):

    def __init__(self):
        """
        This is the constructor for the BaseScraper class.
        It is called when you create an instance of the BaseScraper class,
        but in practice you should only create instances of child classes.
        BaseScraper has four data members, with examples below.
        """
        self.hostUrl = "" # example: www.chartlyrics.com (without http://)
        self.delay = 1.0 # 1 second delay between requests: IMPORTANT

    def __str__(self):
        """
        This gets returned when you call print on a BaseScraper instance.
        """
        return "This is a scraper for " + self.hostUrl

    def getPageHtml(self, relativeUrl, ssl=False):
        """
        Returns a string of the HTML for the page given by
        self.hostUrl + relativeUrl. Program will delay for 1 second afterwards.
        DO NOT alter this delay.
        """
        relativeUrl = relativeUrl

        if (ssl):
            conn = http.client.HTTPSConnection(host=self.hostUrl, timeout=30)
        else:
            conn = http.client.HTTPConnection(host=self.hostUrl, timeout=30)

        if relativeUrl[0] != "/":
            relativeUrl = "/" + relativeUrl

        relativeUrl.encode('utf-8')

        # print("GET: {}".format(self.hostUrl + relativeUrl))
        conn.request("GET", relativeUrl)
        html = conn.getresponse().read()
        html = html.decode("utf-8", errors="ignore")

        sleep(self.delay)
        return html
