import socket
import threading
from queue import Queue
from typing import Iterable

target_ip = "192.168.35.1"  # your default gateway public ip or any safe ip
q = Queue()
open_port_l = []

if __name__ == "__main__":

    def port_scan(port):
        try:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.connect((target_ip, port))
            return True  # connection 성공 = 해당 port가 열려 있음.
        except:
            return False

    def fill_queue(port_list: Iterable[int]):
        for port in port_list:
            q.put(port)

    def worker():
        while not q.empty():
            port = q.get()
            if port_scan(port):
                print(f"port {port} is open")
                open_port_l.append(port)

    port_list = range(1, 1024)
    fill_queue(port_list)

    thread_l = []

    for t in range(100):
        thread = threading.Thread(target=worker)
        thread_l.append(thread)

    for thread in thread_l:
        thread.start()

    for thread in thread_l:
        thread.join()  # wait until all threads terminated

print("open ports:", open_port_l)
