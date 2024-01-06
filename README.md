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


#### << server.py >>


##### 1. TCP Socket 생성 및 연결 대기 (Python의 socket 모듈 사용)
- TCP 방법이기 떄문에 socket(AF_INET, SOCK_STREAM)
- IP, PORT를 Socket에 바인딩 (Socket이 IP, PORT에서 대기하면서 들어오는 연결을 수락할 수 있게 해줌)
- 동시에 들을 수 있는 client 수 지정 (순서를 보여주기 위해 client들이 담길 배열 생성)




##### 2. client 연결 (socket의 accept()함수 이용)
- client와 통신하기 위한 Socket, client의 주소(IP, PORT) 받아옴 (client와의 연결이 될 때까지)




##### 3. request method 처리 (request_handler)
- 새로 생성한 Socket으로 들어오는 HTTP header 정보 처리
- HTTP header의 첫 줄에는 HTTP request method, 주소, HTTP version으로 구성되어 있음 (ex. GET /index.html HTTP/1.1)
- 각 method마다 handler를 호출


##### 4-1. get_handler (GET /index.html HTTP/1.1 처리)
- 
- HTTP header의 첫 줄에는 HTTP request method, 주소, HTTP version으로 구성되어 있음 (ex. GET /index.html HTTP/1.1)
- 각 method마다 handler를 호출


### 1. GET Success 200
<img width="955" alt="index" src="https://github.com/KooSuYeon/computer_network/assets/124496650/62c3118c-be5a-41f0-a29d-9314facd84b0">
