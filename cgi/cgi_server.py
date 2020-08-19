#coding:utf-8
import socket,os

class CGIServer:

    def __init__(self):
        self.cgi_directory = "/Users/changba-176/PycharmProjects/FluentPy/cgi/cgi-bin"
        self.socket = None
    
    def start(self,ip,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((ip,port))
        self.socket.listen(10)
        while True:
            new_socket,address = self.socket.accept()
            request_data = new_socket.recv(1024)
            request_lines= request_data.splitlines()
            request_line = str(request_lines[0])
            cgi_file = request_line.split()[1].split("/")[1]
            path = os.path.join(self.cgi_directory, cgi_file)
            print(path)
            if not self.is_python(cgi_file) or not self.is_file(cgi_file):
                response_start_line = "HTTP/1.1 404\r\n"
                response_headers = "Server: My server\r\n"
                response = response_start_line + response_headers + "\r\n"
                new_socket.send(bytes(response, "utf-8"))
                # 关闭客户端连接
                new_socket.close()
            r, w = os.pipe()
            print("22")
            id = os.fork()
            if id:
                os.close(w)
                r = os.fdopen(r)
                rs=r.read()
                print(rs)
                os.wait()
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My server\r\n"
                response_body = "<h1>"+rs+"</h1>"
                response = response_start_line + response_headers + "\r\n" + response_body
                #print(response)
                new_socket.send(bytes(response, "utf-8"))
                # 关闭客户端连接
                new_socket.close()

            else:
                os.close(new_socket.fileno())
                os.close(r)
                os.dup2(w,1)
                os.execl("/usr/bin/python","python",path)

    
    def is_file(self,cgi_file):
        path = os.path.join(self.cgi_directory,cgi_file)
        if os.path.exists(path) and os.path.isfile(path):
            return True
        return False

    
    def is_python(self,cgi_file):
        lines = cgi_file.split(".")
        if len(lines)==1:
            return False
        if lines[len(lines)-1]=="py":
            return True
        return False




server = CGIServer()
server.start("127.0.0.1",9088)
