#!/usr/bin/python3
"""
Display value from POST
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    import sys

    email = parse.urlencode(sys.argv[2]).encode('utf-8')
    with request.urlopen(sys.argv[1], email=email) as res:
        x = res.read()
    print(x)
