# Requirements
Create a very small Python web server that handles one HTTP request:
- [ ] accept a TCP connection from a browser,
- [ ] receive the HTTP request,
- [ ] read the path from the request line to find the file name,
- [ ] read that file from disk,
- [ ] send a valid HTTP response (status line + blank line + body),
- [ ] close the connection. If the file does not exist, send 404 Not Found. 
