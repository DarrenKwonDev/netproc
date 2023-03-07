## 소켓

소켓 = BSD 소켓 = 버클리 소켓
네트워크 간 통신 프로그램을 만들 때 널리 사용됨

## 파일 소켓과 네트워크 소켓

-   파일 소켓 : linux, mac
    -   window는 없다. window는 자체 소켓 구현인 WinSock을 사용
    -   실행 중인 proc 간에 데이터 교환을 위해 `임의의 파일을 네트워크 소켓 장치로 취급`
    -   파일 타입 찍어보면 's'로 뜨는 것들.
-   네트워크 소켓 : 모든 os
    -   유선(LAN 케이블), 무선(WAP) 으로 연결된 단말 장치간 데이터를 주고 받기 위해 컴퓨터에 생성하는 가상의 장치.
    -   네트워크 연결이 가능한 모든 단말은 네트워크 소켓이 있어야 함.

## socket.socket

```python
# family, type, proto, fileno
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

-   주소 패밀리
    -   AF_INET: IPv4
    -   AF_INET6: IPv6
    -   AF_UNIX: IPC(internal proc communication) 즉, 내부 프로세스 통신용 소켓에 사용하는 주소 패밀리임. win32면 지원 안함. (모듈 내부 코드를 살펴보셈)
-   전송 타입(type)
    -   데이터를 어떤 형태로 보낼 것인가
    -   SOCK_STREAM : 연결 지향형 소켓. TCP. 데이터 손실 없고 순서대로 전달됨. 그래서 `실시간 데이터에 사용`
    -   SOCK_DGRAM : 비연결 지향형 소켓.(connection less) UDP. 전송 순서가 보장되지 않음. 따라서 연속된 데이터의 경우 이 방식은 안됨. 데이터 손실 가능성이 있음. 대신 빠름.
    -   SOCK_RAW : 저수준 소켓. 특정 프로토콜을 사용하는 것이 아니라 인터넷 프로토콜 기반으로 직접 주고 받는 것으로 3계층 헤더와 4계층 헤더를 직접 제어. TCP, UDP 아닌 다른 프로토콜과 통신하는데 사용

## Byte Order : big endian(빅 엔디안)과 little endian(리틀 엔디안)

-   빅엔디안과 리틀 엔디안

    -   CPU 마다 데이터를 메모리에 쓰는 방식을 말한다. 이는 CPU마다 다르다.
    -   빅엔디안은 상위 바이트의 값이 메모리상에 먼저 표시되는 방법 입니다.
    -   리틀 엔디안은 하위 바이트의 값이 메모리상에 먼저 표시되는 방법 입니다
    -   예시
        -   0x12345678를 표현하려고 한다.
        -   빅엔디안은 0x12, 0x34, 0x56, 0x78 순으로 표현
        -   리틀엔디안은 0x78, 0x56, 0x34, 0x12 순으로 표현

-   `h : host`, `n : network`, `s : short`, `l : long`
    -   htonl -> host to network long
    -   htons -> host to network short
    -   ntohl -> network to host long
    -   ntohs -> network to host short

## 호스트 바이트 순서와 네트워크 바이트 순서, NBO(network byte order), HBO(host byte order)

네트워크 바이트 순서는 `빅엔디안 방식`만 사용하기로 약속되어 있다. 따라서 리틀 엔디안 방식을 사용하는 컴퓨터는 데이터를 보내기 전에 빅엔디안 방식으로 데이터를 바꿔야 하고 받을 때는 역순으로 받아 조합해야 한다.
