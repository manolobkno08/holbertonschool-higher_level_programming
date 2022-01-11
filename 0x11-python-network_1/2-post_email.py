#!/usr/bin/python3
"""
Display value from POST
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    x = {'email': argv[2]}
    email = parse.urlencode(x).encode('utf-8')
    req = request.Request(url, email)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
