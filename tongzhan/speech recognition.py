import socket
server_sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sk.bind(('127.0.0.1',9999))
server_sk.listen(128)
while True: #持续提供服务
	#等待传入连接
    new_sk,addr = server_sk.accept()
    content = new_sk.recv(1024)
    content = content.decode('utf-8')
    print('接收到了数据：')  #不用写
    print(content)  #不用写
    new_sk.send('HTTP/1.1 200 ok\r\n\r\n'.encode('utf-8'))
    # new_sk.send(b'HTTP/1.1 200 ok\r\n\r\n')
    # 此例响应头为空
    new_sk.send('ok'.encode('utf-8'))
    # new_sk.send('你好世界'.encode())   #输出为乱码：浣犲ソ涓栫晫
    # new_sk.send(b'ok')
    new_sk.close()