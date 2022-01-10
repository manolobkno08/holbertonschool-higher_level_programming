#!/usr/bin/python3

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        x = res.read()
        print(f"Body response:")
        print(f"\t- type: {type(x)}")
        print(f"\t- content: {x}")
        print(f"\t- utf8 content: {x.decode('utf-8')}")
