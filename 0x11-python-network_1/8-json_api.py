#!/usr/bin/python3
"""
Response Header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    URL = "http://0.0.0.0:5000/search_user"

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    dic = {'q': q}
    req = requests.post(URL, dic).json()
    try:
        if len(req) == 0 or not req.get('id') or not req.get('name'):
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        print("Not a valid JSON")
