#!/usr/bin/python3
"""
Github ID
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    URL = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    req = requests.get(URL, auth=(username, password))
    r = req.headers.get('id')
    print(r)
