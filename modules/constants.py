#!/opt/python_env/sycochuck/bin/python
'''
Menu of syco chuck.

'''

__author__ = "daniel.lindh@cybercow.se"
__copyright__ = "Copyright 2011, The System Console project"
__maintainer__ = "Daniel Lindh"
__email__ = "syco@cybercow.se"
__credits__ = ["???"]
__license__ = "???"
__version__ = "1.0.0"
__status__ = "Production"

import os

GITHUB_AUTH = {
    'sycochuck.fareoffice.com' : {
        'client_id'     : 'c8acfb43b6e3fea9dfe9',
        'client_secret' : '538ea51e65dc64f25f83b6fb2866c8ae438d64e0'
    },
    'sycochuck-tech.fareoffice.com' : {
        'client_id'     : '2bd837d953225142535a',
        'client_secret' : 'd03211b9cec1b6da683717e7757fb678959b07e2'
    },
    'sycochuck-uat.fareoffice.com' : {
        'client_id'     : 'a438b365ae4913ef4cbc',
        'client_secret' : '4738354eec55ebd18be5d1d9627dda897057a6a6'
    },
    'sycochuck-rc.fareoffice.com' : {
        'client_id'     : '32957b8e0f6f81c7785f',
        'client_secret' : '5af1bf3f1641fb275660799464394eaf5d367db4'
    },
    'sycochuck-stable.fareoffice.com' : {
        'client_id'     : '4f897a3015500c3ac59c',
        'client_secret' : '3ad24c69f687b637f40e6e651565aacce1921235'
    },
    'sycochuck-int.fareoffice.com' : {
        'client_id'     : '5c0f559cfd8c5992c212',
        'client_secret' : 'd26f4fb74e3984bfb7f6750df06de208c77bf406'
    }

}

if os.getenv("SERVER_NAME") == 'sycochuck-tech.fareoffice.com':
    import cgitb
    cgitb.enable()
    cgitb.enable(display=1)
