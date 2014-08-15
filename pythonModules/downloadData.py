"""
# Script to log in to website and store cookies.
#
# sources of code include:
#
# http://stackoverflow.com/questions/2954381/python-form-post-using-urllib2-also-question-on-saving-using-cookies
# http://stackoverflow.com/questions/301924/python-urllib-urllib2-httplib-confusion
# http://www.voidspace.org.uk/python/articles/cookielib.shtml
#
# mashed together by Martin Chorley, edited by Ben Throssell
#
# Licensed under a Creative Commons Attribution ShareAlike 3.0 Unported License.
# http://creativecommons.org/licenses/by-sa/3.0/
"""

import urllib, urllib2
import cookielib
import sys


class WebLogin(object):

    def __init__(self, username, password):

        # url for website we want to log in to
        self.base_url = 'http://cliflo.niwa.co.nz'
        # login action we want to post data to
        # could be /login or /account/login or something similar
        self.login_action = '/pls/niwp/wa.logindb'
        # file for storing cookies
        self.cookie_file = 'login.cookies'

        # user provided username and password
        self.username = username
        self.password = password

        # set up a cookie jar to store cookies
        self.cj = cookielib.MozillaCookieJar(self.cookie_file)

        # set up opener to handle cookies, redirects etc
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )

        # pretend we're a web browser and not a python script
        self.opener.addheaders = [('User-agent',
            ('Mozilla/4.0 (compatible; MSIE 6.0; '
            'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # open the front page of the website to set and save initial cookies
        response = self.opener.open(self.base_url)
        self.cj.save()

        # try and log in to the site
        response = self.login()

        print response.read()
##        html = response.read()
##        soup = BeautifulSoup(html)

    # method to do login
    def login(self):

        # parameters for login action
        # may be different for different websites
        # check html source of website for specifics
        login_data = urllib.urlencode({
            'cusername' : self.username,
            'cpwd' : self.password,
            'submit' : 'login'
        })
        submit_data = urllib.urlencode({
            'agents':'30988,30999',
            'TSselection':'NZST',
            'dt1':'vcsn,1',
            'prm1':'331',
            'date1_1':'2013',
            'date1_2':'08',
            'date1_3':'01',
            'date1_4':'00',
            'date2_1':'2013',
            'date2_2':'09',
            'date2_3':'28',
            'date2_4':'00',
            'dateformat':'16',
            'Splitdate':'N',
            'cstn_id':'LA',
            'cdata_order':'DS',
            'cRel':'f',
            'cOrg':'f',
            'mimeselection':'csvplain',
            'submit_sq':'Send Query'
        })
        # construct the url
        login_url = self.base_url + self.login_action
        login_url2 = self.base_url + '/pls/niwp/wgenf.genform1'
        login_url3 = 'http://cliflo.niwa.co.nz/pls/niwp/wgenf.genform1_proc'
        # then open it
        response = self.opener.open(login_url, login_data)
        response = self.opener.open(login_url2)
        response = self.opener.open(login_url3,submit_data)

        # save the cookies and return the response
        self.cj.save()
        return response




username = 'pdpchc'
password = 'chc3532'

# initialise and login to the website
WebLogin(username, password)

