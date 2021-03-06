import socket
import threading
import sys

class  HttpWebServer():
    def __init__(self, port):
        # 1. 编写一个TCP服务端程序
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定地址及端口
        self.tcp_server_socket.bind(('', port))
        # 设置监听
        self.tcp_server_socket.listen(128)

    def handle_client_request(self, client_socket):        # 获取浏览器的请求信息
        client_request_data = client_socket.recv(1024).decode()
        # print(client_request_data)
        # 获取用户请求资源的路径
        request_data = client_request_data.split(' ')
        if len(request_data) == 1:
            client_socket.close()
            return
        request_path = request_data[1]
        if request_path == "/":
            request_path = "/index.html"

        # 3. 读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
        try:
            with open('.\Python\Web_develop\静态Web服务器'+ request_path, 'rb') as f:
                file_data = f.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: pwb\r\n"
            response_body = "404 Not Found Sorry"
            response_data = (response_line + response_header + "\r\n" + response_body).encode('utf-8')
            client_socket.send(response_data)
            pass
        else:
            # 应答行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 应答头
            response_header = "Server: pwb\r\n"
            # 应答体
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            client_socket.send(response_data)
        finally:
            # 4. HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字
            client_socket.close()

    def start(self):
        while True:
            # 2. 获取浏览器发送的HTTP请求报文数据
            # 建立连接
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            sub_thread.start()
def main():
    # 获取执行python程序的终端命令行参数
    print(sys.argv)
    if len(sys.argv) !=2:
        print("格式错误 python3 xxx.py 9090")
        return
    # 判断参数的类型，设置端口号必须是整形
    if not sys.argv[1].isdigit():
        print("格式错误 python3 xxx.py 9090")
        return
    port = int(sys.argv[1])
    # 创建服务器对象

    my_web_server = HttpWebServer(port)
    # 启动服务器
    my_web_server.start()

if __name__ == '__main__':
    main()