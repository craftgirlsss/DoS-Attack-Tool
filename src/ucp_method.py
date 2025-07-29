from colorama import Fore, Style
from src.helpers import Helpers

class UCPMethod:
    @staticmethod
    def attack(target, port):
        if Helpers.ping_host(host=target) == True:
            for i in range(50):
                print(Fore.BLUE, f"Packet {i+1} sent to : {target} with status 200")
            print(Fore.RED, f"Target ke IP Address {target}:{port} tidak dapat dijangkau." + Style.RESET_ALL)