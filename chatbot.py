import os
import time
import socket
from colorama import Fore
from pystyle import Center, Colors, Colorate

os.system(f"title Kichi779 - Twitch Chat bot v1 ")

print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter("""
           
                             ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                             ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                             ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                            ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                           ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                             ███▐██▄   ███   ███    █▄    ███    ███   ███  
                             ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                             ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                             ▀                                             
                    Edit the code, but please don't remove my name. do not make the sale.
                               Discord https://discord.gg/aVk4JUFukk       
                               Github  https://github.com/kichi779          
                       
                      
                      """)))


server = "irc.chat.twitch.tv"
port = 6667
channel = input("Enter your channel name.: ")
interval = int(input("How often should your messages be sent? (Seconds): "))

with open("messages.txt", "r") as file:
    messages = file.readlines()

with open("oauths.txt", "r") as file:
    oauths = file.readlines()

index = 0 

while True:
    oauth = oauths[index % len(oauths)].strip()
    nickname = f"bot_{index}"
    message = messages[index % len(messages)].strip()
    index += 1

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    irc.send(f"PASS {oauth}\n".encode("utf-8"))
    irc.send(f"NICK {nickname}\n".encode("utf-8"))
    irc.send(f"JOIN #{channel}\n".encode("utf-8"))

    try:
        irc.send(f"PRIVMSG #{channel} :{message}\n".encode("utf-8"))
        print(f"[{time.strftime('%X')}] Message sent: {message}")
        time.sleep(interval)
    except Exception as e:
        print(f"[{time.strftime('%X')}] Message could not be sent: {e}")
