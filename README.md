🔥 check_security_headers
Description
This script checks if a given URL has the recommended security headers implemented.

Usage
Single URL Check
To check a single URL, run the script and provide the URL as an input.

```sh
python3 check_headers.py
Enter the URL to check: https://example.com
```
Notes
The script sends an HTTP GET request to the specified URL.
It then checks the server response for the presence of security headers.
If any security headers are missing, the script prints a message indicating which headers are missing.
If any headers have incorrect values, the script prints a message indicating which headers have incorrect values and what the expected values are.
Dependencies
Python 3.x
requests library
You can install the requests library using pip:

```sh
pip install requests
```
```sh
python3 check_headers.py
Enter the URL to check: https://example.com
Headers for https://example.com:
server: nginx
date: Thu, 04 Jul 2024 08:52:15 GMT
content-type: text/html
content-length: 19872
vary: Accept-Encoding
last-modified: Fri, 21 Jun 2024 09:23:48 GMT
etag: "667546a4-4da0"
cache: HIT
x-cached-since: 2024-07-03T09:47:49+00:00
x-node: m9-up-gc99
accept-ranges: bytes

Missing security headers for https://example.com:
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Strict-Transport-Security
- X-XSS-Protection
- Referrer-Policy
- Permissions-Policy
```
This setup ensures that you can check a URL for the presence of essential security headers in a straightforward manner.
