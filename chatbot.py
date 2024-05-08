import os
import time
import socket
import requests
import random
import socks
from pystyle import Center, Colors, Colorate

def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Chat-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        time.sleep(0)

def main():
    if not check_for_updates():
        return
    print_announcement()

print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter("""
 ФОРКНУТО ШИЗИКОМ ИЗ КИБИТКИ
   
                                """)))

announcement = print_announcement()
print("")
print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
print(Colors.yellow, Center.XCenter(f"{announcement}"))
print("")

proxy_servers = [
    {"host": "162.55.87.48", "port": 5566},
    {"host": "38.54.101.254", "port": 144},
    {"host": "38.54.6.39", "port": 4000},
]

socks.set_default_proxy(socks.SOCKS5, proxy_servers[0]["host"], proxy_servers[0]["port"])
socket.socket = socks.socksocket

server = "irc.chat.twitch.tv"
port = 6667
channel = input(Colorate.Vertical(Colors.green_to_blue, "КАНАЛ ДАЙ ДАЙ ТВАРЬ: "))
message_option = input(Colorate.Vertical(Colors.green_to_blue, "ЧЕ ДЕЛАЕМ? (1. ОТПРАВЛЯЕМ С ОДНОГО, 2. ОТПРАВЛЯЕМ С РАНДОМНЫХ ТОКЕНОВ): "))
oauths = []

if message_option == "1":
    with open("messages.txt", "r", encoding='utf-8') as file:
        messages = file.readlines()
    with open("oauths.txt", "r") as file:
        oauths = file.readlines()
        oauth = oauths[0].strip()  # Берем первый токен из списка    
#    interval = int(input("How often should your messages be sent? (Seconds): "))
    index = 0
else:
    with open("messages.txt", "r", encoding='utf-8') as file:
        messages = file.readlines()

while True:
    proxy = random.choice(proxy_servers)
    socks.set_default_proxy(socks.SOCKS5, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    if message_option == "1":
        time.sleep(random.uniform(16, 45))
        message = random.choice(messages).strip()
#        time.sleep(interval)
    else:
        time.sleep(random.uniform(16, 45))
        with open("oauths.txt", "r") as file:
            oauths = file.readlines()
            oauth = random.choice(oauths).strip()
            nickname = f"bot_{random.randint(1, len(oauths))}"
            message = random.choice(messages).strip()

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    print(f"[{time.strftime('%X')}] Sending message from token: {oauth} - Proxy: {proxy['host']}:{proxy['port']} - {message}")
    if message_option == "1":
        irc.send(f"PASS {oauths[index % len(oauths)]}\n".encode("utf-8"))
    else:
        irc.send(f"PASS {oauth}\n".encode("utf-8"))
    irc.send(f"NICK bot\n".encode("utf-8"))
    irc.send(f"JOIN #{channel}\n".encode("utf-8"))
    irc.send(f"PRIVMSG #{channel} :{message}\n".encode("utf-8"))
    irc.close()
