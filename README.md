# Requirements
Create a very small Python web server that handles one HTTP request:
- [x] accept a TCP connection from a browser,
- [x] receive the HTTP request,
- [x] read the path from the request line to find the file name,
- [x] read that file from disk,
- [x] send a valid HTTP response (status line + blank line + body),
- [x] close the connection. If the file does not exist, send 404 Not Found. 
