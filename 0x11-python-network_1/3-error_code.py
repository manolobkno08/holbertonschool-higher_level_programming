#!/usr/bin/python3
"""
Display Error code
"""
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(request.Request(argv[1])) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
