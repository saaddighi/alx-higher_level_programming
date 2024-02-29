#!/bin/bash
# script that that takes in a URL, sends a request to that URL, and displays the size of the body of the response

read -p "Enter URL: " url

# Send a request to the URL and store the response body in a temporary file
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body
echo "Size of the response body: $response bytes"
