#!/usr/bin/python3
"""
Display X-Request-Id value
"""
if __name__ == "__main__":
    import urllib.request as request
    import sys

    with request.urlopen(sys.argv[1]) as res:
        x = res.headers.get('X-Request-Id')
    print(x)
