import time
import os
import socket

time.sleep(10)

if os.name == 'nt': os.system('cls')
else: os.system('clear')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    internal_ip = s.getsockname()[0]
except:
    internal_ip = "not connected"

banner = """
    ██████╗  ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║██║   ██║█████╗  ██████╔╝
    ██╔══██╗██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

                                    OBR 2024"""
info = f"""
    Private IP: {internal_ip}
"""
print(banner)
print(info)