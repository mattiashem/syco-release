#!/opt/python_env/sycochuck/bin/python
'''
Used to authorize with githubs oauth api.

Example:
# Need to be done before any headers are printed to browser.
login = GithubAuth('xxx', 'xxx')
token = login.get_access_token()

'''

__author__ = "daniel.lindh@cybercow.se"
__copyright__ = "Copyright 2011, The System Console project"
__maintainer__ = "Daniel Lindh"
__email__ = "syco@cybercow.se"
__credits__ = ["???"]
__license__ = "???"
__version__ = "1.0.0"
__status__ = "Production"

import requests
import sys
import os
import json
import pprint

class Repo():
    data = None
    # Name of repo
    name = None

    def __init__(self, token, owner, name):
        self.name = name
        r = requests.get('https://api.github.com/repos/%s/%s?access_token=%s' %
            (owner, name, token)
        )
        self.data = json.loads(r.text)

    def print_all(self):
        pp = pprint.PrettyPrinter(indent=4)
        print("<pre>")
        pp.pprint(self.data)
        print("</pre>")


    def has_access(self):
        if "name" in self.data and self.data['name'] == self.name:
            return True
        else:
            return False


class GithubAuth():
    form = None
    token = None

    client_id = None
    client_secret = None
    base_uri = None
    gh_authorize_uri = None
    access_uri = None
    gh_access_uri = None

    def __init__(self, form, github_auth):
        self.form = form
        self.token = form.getfirst("token")

        self._set_oauth(github_auth)
        self.base_uri = '%s' % self._get_pyself()
        self.gh_authorize_uri = 'https://github.com/login/oauth/authorize'
        self.access_uri = '%s?auth_action=access_token' % self._get_pyself()
        self.gh_access_uri = 'https://github.com/login/oauth/access_token'

    def get_access_token(self):
        if not self.token:
            auth_action = self.form.getfirst("auth_action")
            if auth_action != 'access_token':
                self._authorize()
            else:
                code = self.form.getfirst("code")
                self.token = self._access_token(code)
        return self.token

    def check_access(self, owner, repo):
        repo = Repo(self.token, owner, repo)
        if not repo.has_access():
            print "Content-Type: text/html"
            print
            print "You don't have access to this function."
            sys.exit()

    def _set_oauth(self, github_auth):
        auth = github_auth["sycochuck.fareoffice.com"]
        self.client_id = auth['client_id']
        self.client_secret = auth['client_secret']

    def _get_pyself(self):
        if os.getenv("HTTPS") == 'on':
            pyself='https://'
        else:
            pyself='http://'

        pyself += "%s%s" % ('sycochuck.fareoffice.com', os.getenv("SCRIPT_NAME"))
        return pyself


    def _authorize(self):
        url = '%s?client_id=%s&scope=repo&redirect_uri=%s' % (
            self.gh_authorize_uri,
            self.client_id,
            self.access_uri
        )
        print "Location: %s" % url
        print
        #sys.exit()

    def _access_token(self, code):
        payload = {
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
            'code' : code
        }
        r = requests.post(self.gh_access_uri, data=payload)
        response_args = dict(x.split("=") for x in r.text.split("&"))
        token = response_args['access_token']

        print "Location: %s?token=%s" % (self.base_uri, token)
        print
        sys.exit()
