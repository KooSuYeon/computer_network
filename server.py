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
serverPort = 9002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('172.30.1.56', serverPort))
serverSocket.listen(5)
client_sockets = []


print(f"IP : 172.30.1.56 PORT : {serverPort}")
print(">>> Ready to Listenting maximum 5 Clients <<<")
print(f'...Listening on port {serverPort}...')

# GET handler (REQUEST)
def get_handler(version, url, client_socket):
    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:
        file_path = "." + url
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                # server -> client
                # response code + /index.html 내용
                response = f"HTTP/1.0 200 OK\n\n{content.decode()}"
                client_socket.send(response.encode())
        except FileNotFoundError:
            client_socket.send("HTTP/1.1 404 Not Found\n".encode())

# POST handler : query.html에 입력 후 submit 처리 (INPUT)
def post_handler(version, url, client_socket, message):
    last_line = message.split('\n')[-1]
    age_name = last_line.split(' ')
    name = age_name[0]
    age = age_name[1]
    html_data = "<!DOCTYPE html><html><body><h2>NAME : {}</br>AGE : {}</h2></body></html>".format(name, age)

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:
        # 파일에 데이터 추가 모드('a')로 열고 데이터를 씁니다.
        with open("result.txt", 'w') as file:
            file.write(name + age + '\n')

        response = "HTTP/1.1 200 OK\n\n{}".format(html_data)
        client_socket.send(response.encode())

# HEAD handler : style.css 파일 있는지 여부 확인 (RETURN)
def head_handler(version, url, client_socket):
    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    else:

        file_path = "." + url
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                # server -> client
                # 헤더 정보만을 응답으로 전송
                response = f"HTTP/1.0 200 OK\n\n"
                client_socket.send(response.encode())
        except FileNotFoundError:
            client_socket.send("HTTP/1.1 404 Not Found\n".encode())

        
# PUT handler : result.txt 수정 처리 (UPDATE)
def put_handler(version, url, client_socket, message):
    age_name = message.split(' ')
    name = age_name[0]
    age = age_name[1]

    if version not in ["HTTP/1.0", "HTTP/1.1"]:
        client_socket.send("HTTP/1.1 400 Bad Request\n".encode())
    
    else:

        file_path = "." + url
        update_data = name + age
        with open(file_path, 'a') as file:
            file.write(update_data + '\n')

        with open(file_path, 'r') as read_file:
            result_content = read_file.read()
            
        response = "HTTP/1.1 200 OK\n\nResource updated successfully.\n{}".format(result_content)
        client_socket.send(response.encode())


def request_handler(client_socket):
    # client -> server
    # client로부터 받아오는 HTTP header 정보
    request = client_socket.recv(1024).decode()
    print(f"From Client{len(client_sockets)} HTTP header : {request}")

    http_header = request.split()

    method = http_header[0]
    url = http_header[1]
    version = http_header[2]

    # server -> client 응답 구성
    # 각 요청마다 handler 연결
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
