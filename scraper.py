# -*- coding: utf-8 -*-

#### IMPORTS 1.0

import os
import re
import scraperwiki
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
from splinter import Browser

with Browser("phantomjs") as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    browser.visit("https://www.beyondmenu.com/address/search.aspx")

    # submit the search form...
    browser.find_by_css('.search_textbox').fill('San Francisco')
    button = browser.find_by_css("input[type='submit']")
    button.click()

    # Scrape the data you like...
    links = browser.find_by_css(".search_results .resultname")
    for link in links:
        print link.text
