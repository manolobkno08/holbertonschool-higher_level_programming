#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
    x = res.read()

with urllib.request.urlopen('https://intranet.hbtn.io/status') as dec:
    y = dec.read().decode('utf-8')

print(f"""Body response:
    - type: {type(x)}
    - content: {x}
    - utf8 content: {y}""")
