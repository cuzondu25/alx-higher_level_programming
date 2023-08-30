#!/bin/bash
<<<<<<< HEAD
# Get the byte size of the HTTP response header for a given URL.
=======
#  takes in a URL, sends a request to that URL, and displays the size of the body of the response
>>>>>>> b71d8970155fa56a7a833ce6fdfdd371478d7ad1
curl -s "$1" | wc -c
