from socket import *
import os
import mimetypes
from urllib.parse import parse_qs, unquote

CURR_MY_PATH_ROOT = os.getcwd()

# server의 client listen 준비
# 1. TCP socket 생성
# 2. IP, PORT를 socket에 바인딩
# 3. 해당 socket이 최대로 들을 수 있는 client 수를 지정
# 동시에 들을 수 있는 client 수 지정 : 5개로 지정
serverPort = 8891
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)
client_sockets = []


print(f"IP : 127.0.0.1 PORT : {serverPort}")
print(">>> Ready to Listenting maximum 5 Clients <<<")
print(f'...Listening on port {serverPort}...')

def get_handler(version, url, client_socket):
    URL = "/index.html" if len(url) == 1 and url[0] == "/" else url
    FIANL_PATH = CURR_MY_PATH_ROOT + URL

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:
        if os.path.isfile(FIANL_PATH):
            content_type, _ = mimetypes.guess_type(FIANL_PATH)
            with open(FIANL_PATH, 'rb') as file:
                content = file.read()
                response = "HTTP/1.0 200 OK\nContent-Type: {}\n\n".format(content_type)
                client_socket.send(response.encode() + content)
        
        else:
            client_socket.send("HTTP/1.1 404 Not Found\n".encode())

def post_handler(version, url, client_socket, message):
    post_information = message.split('\n')[-1]
    html_data = "<!DOCTYPE html><html><body><h2>{}</h2></body></html>".format(post_information)

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:
        # 파일에 데이터 추가 모드('a')로 열고 데이터를 씁니다.
        with open("result.txt", 'a') as file:
            file.write(post_information + '\n')

        response = "HTTP/1.1 200 OK\n\n{}".format(html_data)
        client_socket.send(response.encode())


def head_handler(version, url, client_socket):
    URL = "/style.css" if len(url) == 1 and url[0] == "/" else url
    FIANL_PATH = CURR_MY_PATH_ROOT + URL

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:
        if os.path.isfile(FIANL_PATH):
            
            # 헤더 정보만을 응답으로 전송
            response = "HTTP/1.0 200 OK\n\n"
            client_socket.send(response.encode())
        
        else:
            client_socket.send("HTTP/1.1 404 Not Found\n".encode())

        

def put_handler(version, url, client_socket, message):
    resource_path = os.path.join(CURR_MY_PATH_ROOT, "result.txt")

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    
    else:

        update_data = message.split('\n')[-1]

        with open(resource_path, 'w') as file:
            file.write(update_data)
            
        response = "HTTP/1.1 200 OK\n\nResource updated successfully.\n{}".format(update_data)
        client_socket.send(response.encode())


def request_handler(client_socket):
    # client로부터 받아오는 http_method
    request = connectionSocket.recv(1024).decode()
    print(f"From Client{len(client_sockets)} Sentence : {request}")

    lines = request.split('\n')
    first_line = lines[0].split()

    method = first_line[0]
    url = first_line[1]
    version = first_line[2]

    # server -> client 응답 구성
    # HTTP 메소드에 따른 응답 생성
    # GET
    if method == "GET":
        get_handler(version, url, client_socket)

    # POST
    elif method == "POST":
        post_handler(version, url, client_socket, request)
    
    # HEAD
    elif method == "HEAD":
        head_handler(version, url, client_socket)

    # PUT
    elif method == "PUT":
        put_handler(version, url, client_socket, request)

    
    # else:
    connectionSocket.close()
    

while True:

    # client -> server
    connectionSocket, addr = serverSocket.accept()
    client_sockets.append(connectionSocket)
    print(f">>> Client{len(client_sockets)} Connection Succeess! <<<")

    request_handler(connectionSocket)
    
    # # server -> client 응답 구성
    # # HTTP 메소드에 따른 응답 생성
