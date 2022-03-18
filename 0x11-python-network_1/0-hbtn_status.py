#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
use the package urllib
 body of the response must be displayed in tabulation before -
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print('Body response:\n\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
