#!/usr/bin/python3
"""
Display value from POST
"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys

    x = {'email': sys.argv[2]}
    email = parse.urlencode(x).encode('utf-8')
    url = sys.argv[1]
    req = request.Request(url, email)
    with request.urlopen(req) as r:
        print(r.read())
