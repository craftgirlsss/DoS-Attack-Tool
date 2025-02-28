import os
import subprocess
import sys
from colorama import Fore

class Helpers:
    @staticmethod
    def signal_handler():
        print(Fore.RED, f'You pressed Ctrl+C!')
        sys.exit(0)

    @staticmethod
    def ping_host(host) -> bool:
      try:
         result = subprocess.run(
            ["ping", "-c", "3", host] if not subprocess.os.name == "nt" else ["ping", "-n", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
         )
         if result.returncode == 0:
            print(Fore.GREEN,f"Ping to {host} was successful:\n{result.stdout}")
            return True
         else:
            print(f"Ping to {host} failed:\n{result.stderr}")
            return False
      except Exception as e:
         print(f"An error occurred: {e}")
         return False
    
    @staticmethod
    def clear_terminal():
        if os.name == 'nt':
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)