#!/usr/bin/python3
"""
Response Header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    URL = argv[1]
    req = requests.get(url=URL)
    r = req.headers.get('X-Request-Id')
    print(r)
