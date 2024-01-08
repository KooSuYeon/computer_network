# TCP programming + HTTP protocol Request



- - - 
<div align="center">
  
소켓 통신을 활용하여 Server, Client 프로그램 작성 (프로그래밍 언어는 C, Java, Python 으로 구현)</br>
TCP 기반 소켓프로그래밍 작성후 Client에서는 HTTP 프로토콜의 GET/HEAD/POST/PUT Request를 요청하여</br>
Server에서는 Client의 Request에따라 응답 메시지를 구성하여 Response하도록 구현 (TCP 기반 Client, Server 구현한 프로그램 파일을 제출)</br>
예) 
Method-응답 xxx의 case 5개 이상 수행 </br>
GET-응답 4xx, GET-응답 2xxx, HEAD-응답 1xx, POST-응답 2xxx, POST-응답 1xx 등

와이어샤크로 해당 메서드의 HTTP format 캡쳐</br>
소켓 통신은 PC가 2대 이상이면 Client, Server 실행은 분리하여 진행을 권장</br>
2대 이상 환경이 안되는 경우는 localhost로 진행도 가능

</div>

- - - 

### TCP programming 
server.py , client.py 분리하여 작성


#### 1. server 작동
#### 2. client HTTP method에 따른 요청 -> server에 보냄
#### 3. server의 응답 -> client에 반환 요청 보냄



- - - 

#### << server.py >>


##### 1. TCP Socket 생성 및 연결 대기 (Python의 socket 모듈 사용)
- TCP 방법이기 떄문에 socket(AF_INET, SOCK_STREAM)
- 내 PC의 IP, 지정해줄 PORT를 Socket에 바인딩 (Socket이 IP, PORT에서 대기하면서 들어오는 연결을 수락할 수 있게 해줌)
- 동시에 들을 수 있는 client 수 지정 (순서를 보여주기 위해 client들이 담길 배열 생성)




##### 2. client 연결 (socket의 accept()함수 이용)
- client와 통신하기 위한 Socket, client의 주소(IP, PORT) 받아옴 (client와의 연결이 될 때까지)



#### <<< client.py >>>


##### 2. client request 요청
- 1. server에게 보낼 method 분류
    - method에 따른 IP, PORT, path, data
- 2. mehtod에 따른 server에게 보낼 HTTP header 구성
- 3. Socket 생성 후 connection 생성
- 4. 생성한 Socket에 앞서 구성한 HTTP header를 전송


##### 3. request method 처리 (request_handler)
- 새로 생성한 Socket으로 들어오는 HTTP header 정보 처리
- HTTP header의 첫 줄에는 HTTP request method, 주소, HTTP version으로 구성되어 있음 (ex. GET /index.html HTTP/1.1)
- 각 method마다 handler를 호출

- - - 

## >>>> GET 요청


#### >>> client
##### 4-1. send_http_get_request (server로 보낼 request 구성)
1. send_http_get_request(host, port, "/index.html")
2. HTTP header 구성 : GET /index.html HTTP/1.1\r\nHOST: {host}\r\n\r\n
3. server와 연결할 Socket 생성 후 Socket으로 만든 header client에게 전송


#### >>> server
##### 4-1. get_handler (client로부터 온 HTTP header GET /index.html HTTP/1.1 처리)
- 172.30.1.56.9002/index.html 접근 -> GET 요청
1. 올바른 version인지 확인 (HTTP/1.0 or HTTP/1.1)
2. 존재하는 html이라면 해당 html읽어옴.</br>
   현재 디렉터리에는 index.html, queryindex.html만 존재 -> 해당 html 내용 앍어온 후 client 에게 전송





### 1. GET Success 200
<img width="955" alt="index" src="https://github.com/KooSuYeon/computer_network/assets/124496650/62c3118c-be5a-41f0-a29d-9314facd84b0">




- - - 

## >>>> POST 요청


#### >>> client
##### 4-1. send_http_post_request (server로 보낼 request 구성)
1. client에게 이름과 나이의 입력을 받음. (spacebar 구분) 
2. send_http_post_request(host, port, "/result", client_input)
3. HTTP header 구성 : POST /result HTTP/1.1\r\nHOST: {host}\r\nContent-length: {content_length}\r\n\r\n{data}
4. server와 연결할 Socket 생성 후 Socket으로 만든 header client에게 전송


#### >>> server
##### 4-1. post_handler (client로부터 온 HTTP header POST /result HTTP/1.1 처리)
- client에게 입력받음 -> POST 요청
1. client에게 입력받은 name, age 분리 및 /result에 보여질 html 구성
2. 올바른 version인지 확인 (HTTP/1.0 or HTTP/1.1)
3. 입력받은 name, age를 file 에 작성
4. client에게 받아온 정보로 구성된 /result의 html 내용을 읽어온 후 client에게 전송



- - - 

## >>>> HEAD 요청


#### >>> client
##### 4-1. send_http_head_request (server로 보낼 request 구성)
1. send_http_head_request(host, port, "/style.css")
2. HTTP header 구성 : HEAD /style.css HTTP/1.1\r\nHOST: {host}\r\n\r\n
3. server와 연결할 Socket 생성 후 Socket으로 만든 header client에게 전송


#### >>> server
##### 4-1. head_handler (client로부터 온 HTTP header HEAD /style.css HTTP/1.1 처리)
- 172.30.1.56.9002/style.css 존재유무 확인 -> HEAD 요청
1. 올바른 version인지 확인 (HTTP/1.0 or HTTP/1.1)
2. 존재하는 css라면 해당 요청의 헤더 정보만을 읽어옴.</br>
   존재하는 css라면 "HTTP/1.0 200 OK" -> client 에게 전송



- - - 

## >>>> PUT 요청


#### >>> client
##### 4-1. send_http_put_request (server로 보낼 request 구성)
1. send_http_put_request(host, port, "/result.txt", "John 25")
2. HTTP header 구성 : PUT /result.txt HTTP/1.1\r\nHost: {host}\r\nContent-Length: {content_length}\r\n\r\n{data}"
3. server와 연결할 Socket 생성 후 Socket으로 만든 header client에게 전송


#### >>> server
##### 4-1. put_handler (client로부터 온 HTTP header PUT /style.css HTTP/1.1 처리)
- client에게 result.txt 수정 요청 -> PUT 요청
1. client에게 수정하고 싶은 이름과 나이의 입력을 받음.
2. send_http_put_request(host, port, "result.txt", data)
3. 올바른 version인지 확인 (HTTP/1.0 or HTTP/1.1)
4. 입력받은 name, age를 file 에 반영
5. client에게 받아온 Update된 정보 -> client에게 전송

