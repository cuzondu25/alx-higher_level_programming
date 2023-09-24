#!/usr/bin/python3
<<<<<<< HEAD
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
=======
"""A script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
>>>>>>> 575589ae510611ac76410978f07d787777c5a004
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
