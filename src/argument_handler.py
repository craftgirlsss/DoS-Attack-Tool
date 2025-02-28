import argparse
from colorama import Fore
from src.helpers import Helpers
from src.tcp_method import TCPMethod
from src.udp_method import UDPMethod

class ArgumentHandler():
    def __init__(self):
        self.handler()

    def handler(self):
        parser = argparse.ArgumentParser(description="Simulasi Serangan TCP/UDP DDoS")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-tC", "--tcp", action="store_true", help="Gunakan metode TCP Attack")
        group.add_argument("-uD", "--udp", action="store_true", help="Gunakan metode UDP Attack")

        parser.add_argument("-ip", "--ipaddress", type=str, required=True, help="IP target")
        parser.add_argument("-p", "--port", type=int, default=80, help="Port target (default: 80)")
        parser.add_argument("-t", "--thread", type=int, default=10, help="Jumlah thread penyerangan (default: 10)")

        args = parser.parse_args()

        if args.tcp:
            print(f"TCP method running to IP Address {args.ipaddress} with port {args.port} and thread {args.thread}")
            if Helpers.ping_host(host=args.ipaddress) == True:
                print(Fore.GREEN, "Start to attack")
                tcpMethod = TCPMethod(target_ip=args.ipaddress, target_port=args.port, thread_count=args.thread)
                tcpMethod.start_attack()
            else:
                print(Fore.RED, f"Failed Running code")
        elif args.udp:
            print(f"UDP method running to IP Address {args.ipaddress} with port {args.port} and thread {args.thread}")
            if Helpers.ping_host(host=args.ipaddress) == True:
                print(Fore.GREEN, "Start to attack")
                udpMethod = UDPMethod(target_ip=args.ipaddress, target_port=args.port, thread_count=args.thread, packet_size=512)
                udpMethod.udp_attack()
            else:
                print(Fore.RED, f"Failed Running code")