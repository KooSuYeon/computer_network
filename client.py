from socket import *
import threading

serverName = '127.0.0.1'
serverPort = 8891

def send_request(host, port, request):
    # TCP socket 생성
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # TCP -> socket마다 connection 생성
    clientSocket.connect((host, port))
    clientSocket.send(request.encode())

    response = b""
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        response += data
    
    print(response.decode())
    clientSocket.close()

def send_http_get_request(host, port, path):
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    send_request(host, port, request)

def send_http_post_request(host, port, path, data):
    content_length = len(data)
    request = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n{data}"
    send_request(host, port, request)

def send_http_head_request(host, port, path):
    request = f"HEAD {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    send_request(host, port, request)

def send_http_put_request(host, port, path, data):
    content_length = len(data)
    request = f"PUT {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n{data}"
    send_request(host, port, request)

send_http_head_request(serverName, serverPort, "/style.css")
send_http_get_request(serverName, serverPort, "/index.html")
send_http_put_request(serverName, serverPort, '/result.txt', 'Update content')