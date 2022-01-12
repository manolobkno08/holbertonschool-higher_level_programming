#!/usr/bin/python3
"""
Response Header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    URL = argv[1]
    email = {'email': argv[2]}
    req = requests.post(url=URL, data=email)
    print(req.text)
