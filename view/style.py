import os
import sys

# Colores de texto
class Colors:
    white = "\033[37m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    bold = "\033[1m"
    sub = "\033[4m"
    reset = "\033[0m"

# Funcion para colorear texto
def color_text(color, text):
    return f"{color}{text}{Colors.reset}"

def start():
    if sys.stdout.isatty():
        os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Colors.yellow}{Colors.bold}{ "    - - Inicio Sistema de Gestion de Talleres Escolares - - " }{Colors.reset}\n")

def header(text):
    print(f"\n{Colors.green}{"   "+text}{Colors.reset}\n")

def subheader(text):
    print(f"\n{Colors.yellow}{"   "+text}{Colors.reset}\n")

def normal_cyan(text):
    print(f"\n{Colors.cyan}{"   "+text}{Colors.reset}\n")

def footer():
    print(f"\n{Colors.red}{Colors.bold}{'////////////////////////////////////'}{Colors.reset}\n")
    print(f"{Colors.red}{"        "+ "Fin del Programa"}{Colors.reset}\n")
