# TCP Programming + HTTP Protocol Request

---

<div align="center">
  
Server, Client programming using socket communication</br>
(programming languages are implemented in C, Java, Python)</br>
After creating TCP-based socket programming, the Client requests an HTTP protocol GET/HEAD/POST/PUT Request</br>
Server configures response messages according to Client's Request and implements them to respond</br>
(TCP-based Client submits program files implemented by Server)</br>
Ex) 
Method-Response xxx to perform at least 5 cases </br>
GET-response 4xx, GET-response 2xx, HEAD-response 1xx, POST-response 2xx, POST-response 1xx, etc

HTTP format capture for that method with wireshark</br>
Socket communication is recommended if there are more than two PCs, separate Client and Server runs</br>
If more than two environments are not available, you can also proceed to localhost

</div>

---

### TCP Programming Characteristics
- How to create a new socket for each request, communication between the client and the server
- It is done using multiple sockets.


### Socket
##### Protocol
- Tells you which protocol to use as an argument for the Socket() function,
- Assign socket (AF_INET, SOCK_STREAM) because it is a TCP method</br>

#### Source's Address and Port Number
- Address and port number of the destination
- Associate address with port number as a bind() function</br>

#### Destination's Address and Port Number
- Address and port number of the destination
- In TCP, the address and port number of the destination are bundled with the connect() function.
- UDP sends only the address and port number of the destination as an argument for the sendto() function.</br>
  
---

### Socket
Create Server.py , client.py separately
Language: Python

### How it works
1. Server Operation</br>
Run server code on the PC you want to run as the server</br>
>> python server.py</br>
2. Request according to Client HTTP method -> Send to server</br>
Run client code on PC to run as the client</br>
>> python client.py
3. Server's Response -> Send to client


---

#### Caution
- Check if the firewall is turned off
- Verify PC-Specific IP Address
- Ensure client and server IP, PORT are matched

#### << server.py >>
1. Create TCP Socket and wait for connection (using Python's socket module)
![server1](https://github.com/KooSuYeon/computer_network/assets/124496650/687f2c26-6e60-42e6-acf7-249752b9f173)

- socket (AF_INET, SOCK_STREAM) because it is a TCP method
- Bind my PC's IP, PORT to be specified to Socket
(Allows Socket to accept incoming connections while waiting at IP, PORT)
- Specify the number of clients that can be heard at the same time (create an array of clients to contain to show the order)

2. client connection (use accept() function in the socket)
![picture2](https://github.com/KooSuYeon/IBookLeague/assets/124496650/a87b1026-9805-4b90-aa11-24179825e44b)
</br>
-Socket to communicate with the client, get the client's address (IP, PORT) (until it is connected to the client)


#### << server.py >>
2. client request
![server2](https://github.com/KooSuYeon/computer_network/assets/124496650/c624809a-c05e-48f4-8a2b-283985dd419a)

1. Classify methods to send to the server
    - method에 따른 IP, PORT, path, data
2. Configuring HTTP Header to send to the server according to the method
3. Create a connection after creating a socket
4. Send the HTTP header that you configured prior to the Socket you created


3. request method (request_handler)
![picture4](https://github.com/KooSuYeon/IBookLeague/assets/124496650/a08a6bcb-f6f6-44b1-a246-3b25888c983d)
- Processing HTTP header information coming into the newly created Socket
- The first line of the HTTP header consists of the HTTP request method, address, and HTTP version
(ex. GET /index.html HTTP/1.1)
- Call Handler for each method

- - - 

## >>>> GET Request

#### >>> Client
##### 4-1. send_http_get_request (compose request to send to the server)
![picture5](https://github.com/KooSuYeon/IBookLeague/assets/124496650/21cca91a-92b7-4aa2-88b9-f7e3f38d3860)
![picture6](https://github.com/KooSuYeon/IBookLeague/assets/124496650/b52c9fa8-2f9b-440c-934a-11b731fdacdc)

1. send_http_get_request(host, port, "/index.html")
2. HTTP header : GET /index.html HTTP/1.1\r\nHOST: {host}\r\n\r\n
3. Create a socket to connect to the server and send it to the header client made of the socket

#### >>> Server
##### 4-1. get_handler (handle HTTP header GET /index.html HTTP/1.1 from the client)

![picture7](https://github.com/KooSuYeon/IBookLeague/assets/124496650/0a48170e-5467-4417-8789-42b29de91127)

- IP/index.html -> GET request
1. Verify correct version (HTTP/1.0 or HTTP/1.1)
2. If it exists, read the corresponding HTML.</br>
   Only index.html, query index.html exists in the current directory -> After the corresponding HTML contents are found, send to the client

Response code: 200</br>
Server Terminal</br>
![getterminal](https://github.com/KooSuYeon/computer_network/assets/124496650/b803e006-303d-4011-8418-a7256baa32d8)

</br>

Header information requested by the client, displayed in IP address -> server</br>
Client Terminall</br>
![picture9](https://github.com/KooSuYeon/computer_network/assets/124496650/626c6cf8-51c3-4ee5-a288-ca5128b9203b)
</br>

Response code sent by the server, page requested by the client (index.html) -> displayed in the clientl</br>

![get1](https://github.com/KooSuYeon/computer_network/assets/124496650/56637e00-587b-429c-ab38-2ce38086b347)


</br>

Response code: 404</br>
Page 404 GET Requestl</br>
![picture11](https://github.com/KooSuYeon/computer_network/assets/124496650/b071ef05-8657-459a-aa50-054e8a2336aa)
</br>

Server Terminall</br>
![getno](https://github.com/KooSuYeon/computer_network/assets/124496650/8c25f42e-473a-4895-ab6e-629086fb21df)

</br>

Header information requested by the client, displayed in IP address -> server</br>
Client Terminall</br>
![picture13](https://github.com/KooSuYeon/computer_network/assets/124496650/c01db021-16a6-44ad-9711-20d7294b6ac8)
</br>

Response code sent by the server, displayed in the clientl</br>
![get2](https://github.com/KooSuYeon/computer_network/assets/124496650/f921281b-f4a3-4d85-8909-12a60acaf2eb)

</br>

- - - 

## >>>> POST Request

#### >>> Client
##### 4-1. send_http_post_request (compose request to send to the server)

![picture14](https://github.com/KooSuYeon/computer_network/assets/124496650/13a7ab29-9cf6-4b32-ae35-92334f138d12)
![picture15](https://github.com/KooSuYeon/computer_network/assets/124496650/c980d806-6478-4853-a427-a7da64e64d7c)

1. send_http_post_request(host, port, "/index.html")
2. HTTP header : POST /index.html HTTP/1.1\r\nHOST: {host}\r\n\r\n
3. Create a socket to connect to the server and send it to the header client made of the socket

#### >>> Server
##### 4-1. post_handler (handle HTTP header POST /index.html HTTP/1.1 from the client)

![picture16](https://github.com/KooSuYeon/computer_network/assets/124496650/a97f3234-b8f7-4191-984b-0b6bdd77a7f3)

- Received from the client -> POST Request
1. Configuring HTML to be seen in name, age isolation, and /result received from the client
2. Verify correct version (HTTP/1.0 or HTTP/1.1)
3. Create input name, age in the file
4. Read the HTML contents of the /result consisting of the information received from the client and send it to the client

Response code: 200</br>
Server Terminal</br>
![post](https://github.com/KooSuYeon/computer_network/assets/124496650/279d483c-fe80-43b9-ad38-efbb38910946)



Header information requested by the client, IP address, content-length entered, content -> server displayed</br>

Client Terminal</br>
![picture18](https://github.com/KooSuYeon/computer_network/assets/124496650/c20081da-9e94-46ea-8c8c-adad61724c6d)
</br>
Response code sent by the server, post request result -> displayed in the client</br>

(After calling the page where you can enter information - GET method, enter information - POST method)</br>
Request POST by entering the name and age to write to the user</br>
The value received is written in result.txt.</br>
![post2](https://github.com/KooSuYeon/computer_network/assets/124496650/c1815a5d-a964-431f-8950-547b56b13cc4)


</br>

Result.txt</br>
![picture20](https://github.com/KooSuYeon/computer_network/assets/124496650/bf64ac02-f60a-4a2b-8620-cf4c51f1787e)
</br>

- - - 

## >>>> HEAD Request

#### >>> Client
##### 4-1. send_http_head_request (compose request to send to the server)
![picture21](https://github.com/KooSuYeon/computer_network/assets/124496650/dedc78c8-8eba-4f2e-87c8-ddb97cb75dc7)
![picture22](https://github.com/KooSuYeon/computer_network/assets/124496650/4fc6a592-f176-482e-9dcb-45bfc38a5411)

1. send_http_head_request(host, port, "/style.css")
2. HTTP header : HEAD /style.css HTTP/1.1\r\nHOST: {host}\r\n\r\n
3. Create a socket to connect to the server and send it to the header client made of the socket

#### >>> Server
##### 4-1. head_handler (handle HTTP header HEAD /style.css HTTP/1.1 from the client)
![picture23](https://github.com/KooSuYeon/computer_network/assets/124496650/842dcbac-7ebb-4909-a39b-82ed90a02977)

- IP/style.css Presence Confirmation -> HEAD Request
1. Verify correct version (HTTP/1.0 or HTTP/1.1)
2. If there is a CSS, only the header information of the request is read.</br>
   If CSS exists, send "HTTP/1.0 200 OK" -> to the client

Response code: 200</br>
Server Terminal</br>
![head1](https://github.com/KooSuYeon/computer_network/assets/124496650/21a97792-92ad-4f12-a71d-24496df0c79e)

</br>
Header information requested by the client, displayed in IP address -> server</br>
Client Terminal</br>

![picture20](https://github.com/KooSuYeon/computer_network/assets/124496650/bf64ac02-f60a-4a2b-8620-cf4c51f1787e)

</br>
Show in response code -> client sent by server</br>

![head2](https://github.com/KooSuYeon/computer_network/assets/124496650/0439bf6a-a10c-4435-9f8a-5e3721f6c48b)


</br>

Response code: 404</br>
404 CSS page request</br>
![picture27](https://github.com/KooSuYeon/computer_network/assets/124496650/201203be-bb16-4bb7-98e9-51aa021f4cce)
</br>
Server Terminal</br>
![head3](https://github.com/KooSuYeon/computer_network/assets/124496650/4dd12cef-781e-4935-aa44-bbaa342ed19b)

</br>

Client Terminal</br>
![picture29](https://github.com/KooSuYeon/computer_network/assets/124496650/43a4e319-a7b1-4092-8da0-266872957f57)
</br>

![head4](https://github.com/KooSuYeon/computer_network/assets/124496650/8b216392-039b-4c35-b0af-7907e357ff1f)

</br>

- - - 

## >>>> PUT Request

#### >>> client
##### 4-1. send_http_put_request (compose request to send to the server)

![put1](https://github.com/KooSuYeon/computer_network/assets/124496650/268b839f-58f8-4366-b3dc-8207179f88fe)
![put2](https://github.com/KooSuYeon/computer_network/assets/124496650/56e4b1a1-f376-4e21-9fe2-efbc64c7ee7c)


- Receive name and age to modify result.txt from client
1. send_http_put_request(host, port, "/result.txt", data)
2. HTTP header: PUT /result.txt HTTP/1.1\r\nHOST: {host}\r\nContent-length: {content_length}\r\n\r\n{open}\”name\”: {name} ,\n\”age\”: {age} {close}”
3. Create a socket to connect to the server and send it to the header client made of the socket

#### >>> server
##### 4-1. put_handler (handle HTTP header HEAD /style.css HTTP/1.1 from the client)
- Request result.txt modification to client -> Request PUT


![put3](https://github.com/KooSuYeon/computer_network/assets/124496650/de52ab96-5dd3-4273-95b2-3b9e3a115b04)

1. Receive input from client of the name and age you want to modify.
2. send_http_put_request(host, port, "result.txt", data)
3. Verify correct version (HTTP/1.0 or HTTP/1.1)
4. Reflect the input name, age in the file
5. Updated information received from client -> Send to client

Response code : 200</br>
Server Terminal</br>
![post](https://github.com/KooSuYeon/computer_network/assets/124496650/b2f6d788-f2e8-49bd-8cec-45d50b02b67b)

</br>

Header information requested by the client, IP address, content-length entered, content -> server displayed</br>

Read the changed result.txt content when the PUT request was successful.</br>
response code sent by server, updated information -> display in client</br>
![put5](https://github.com/KooSuYeon/computer_network/assets/124496650/cf1a5187-9cff-4082-a73a-399aa0e4ab4b)


Result.txt</br>
![put6](https://github.com/KooSuYeon/computer_network/assets/124496650/8f759c60-747c-495c-b176-e0c7b4c6ec49)
</br>


![post2](https://github.com/KooSuYeon/computer_network/assets/124496650/c09d627f-26c7-42b2-ba64-be991d179261)
