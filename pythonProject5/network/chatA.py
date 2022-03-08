import socket

# stream을 만들어야 하는데,
# 한쪽으로만 흐른다.
# 보내는 stream, 받는 stream
# socket은 2개를 따로 만든다.
# sock1은 보내는 용도, sock2는 받는 용도
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('192.168.0.9', 4000))
print('192.168.0.9, 4000 port node start!')
print('----------------A-----------------')
while True:
    # a가 b에 보내는 부분
    data = input("Simple_chat_A >> ")
    sock1.sendto(data.encode('utf-8'), ('192.168.0.9', 3000))

    # a가 b에게 받는 부분
    data, addr = sock2.recvfrom(1024)  # 1024: 잡아놓은 byte 공간
    print("Simple_chat_B >> ", data.decode('utf-8'))