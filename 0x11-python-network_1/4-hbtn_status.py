#!/usr/bin/python3
"""
My Status
"""
if __name__ == "__main__":
    import requests

    URL = "https://intranet.hbtn.io/status"
    req = requests.get(url=URL)
    r = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r))
