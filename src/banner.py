from colorama import Fore

class Header:
    def __init__(self):
        self.display()

    def display(self):
        print(Fore.GREEN, """
                 _____     _____        __      
                |  __ \   |_   _|      / _|     
                | |__) |__  | |  _ __ | |_ ___  
                |  ___/ _ \ | | | '_ \|  _/ _ \ 
                | |  |  __/_| |_| | | | || (_) |
                |_|   \___|_____|_| |_|_| \___/                                  
""")
        print(Fore.GREEN, """
PeInfo v1.0 ( https://nextjiesdev.site )
              
PeInfo simple tool for DoS Attack.
Usage: pinfo [Type Attack] [Options] [target specification]
        """)