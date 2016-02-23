import socket
import threading


def conn_server(sock):
    print "Start"
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            if not data: break
            print data[:5]
            if data[:5] == 'close':
                break
            else:
                conn.send(data)
        conn.close()


def thread_start(thread_name):
    thread_name = threading.Thread(target=conn_server, args=(s,))
    thread_name.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)


for i_thread_name in xrange(10):
    thread_start("thread" + str(i_thread_name))
