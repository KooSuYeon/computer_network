from socket import *

# Socket생성의 두 가지 요소 : IP, PORT
# 1. 내 머신의 IP
# 2. 사용하려는 PORT
serverName = '172.30.1.56'
serverPort = 8892

def send_request(host, port, request):
    # TCP socket 생성 후 connection 생성
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((host, port))
    # client -> server
    # HTTP 요청의 header를 보냄.
    clientSocket.send(request.encode())

    response = b""
    while True:
        # server -> client
        # 요청에 따른 server의 응답
        data = clientSocket.recv(1024)
        if not data:
            break
        response += data
    
    print(response.decode())
    clientSocket.close()

# HTTP GET 요청 header
def send_http_get_request(host, port, path):
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    send_request(host, port, request)

# HTTP POST 요청 header
def send_http_post_request(host, port, path, data):
    content_length = len(data)
    request = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n{data}"
    send_request(host, port, request)

# HTTP HEAD 요청 header
def send_http_head_request(host, port, path):
    request = f"HEAD {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    send_request(host, port, request)

# HTTP PUT 요청 header
def send_http_put_request(host, port, path, data):
    content_length = len(data)
    request = f"PUT {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n{data}"
    send_request(host, port, request)

# send_http_head_request(serverName, serverPort, "/style.css")
# send_http_get_request(serverName, serverPort, "/index.html")
send_http_get_request(serverName, serverPort, "/query.html")
print("Input your name and age (ex. suyeon 21)")
client_input = input(">>> ")
send_http_post_request(serverName, serverPort, '/result', client_input)
# send_http_put_request(serverName, serverPort, '/result.txt', 'Update content')