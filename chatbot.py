import os
import time
import socket
import requests
from colorama import Fore
from pystyle import Center, Colors, Colorate

os.system(f"title Kichi779 - Twitch Chat bot v1.5 ")

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
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.  
                             Github  github.com/kichi779
                             Discord discord.gg/3Wp3amnNr3  """)))
announcement = print_announcement()
print("")
print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
print(Colors.yellow, Center.XCenter(f"{announcement}"))
print("")
print("")


server = "irc.chat.twitch.tv"
port = 6667
channel = input(Colorate.Vertical(Colors.green_to_blue, "Enter your channel name: "))
message_option = input(Colorate.Vertical(Colors.green_to_blue,"How do you want to send messages? (1. Send messages from messages.txt, 2. Send messages by selecting a bot): "))
oauths = []

if message_option == "1":
    with open("messages.txt", "r") as file:
        messages = file.readlines()

    interval = int(input(Colorate.Vertical(Colors.green_to_blue,"How often should your messages be sent? (Seconds): ")))
    index = 0

while True:
    if message_option == "1":
        message = messages[index % len(messages)].strip()
        index += 1
        time.sleep(interval)
    else:
        with open("oauths.txt", "r") as file:
            oauths = file.readlines()

        print("Available bots:")
        for i in range(len(oauths)):
            print(f"{i+1}. Bot {i+1}")

        bot_choice = int(input(Colorate.Vertical(Colors.green_to_blue,"Select a bot to send the message with (1, 2, 3, ...): ")))
        if bot_choice > len(oauths):
            print("Invalid bot choice!")
            time.sleep(5)
            exit()

        oauth = oauths[bot_choice-1].strip()
        nickname = f"bot_{bot_choice}"
        message = input(Colorate.Vertical(Colors.green_to_blue,"Enter the message you want to send: "))

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))

    if message_option == "1":

        with open("oauths.txt", "r") as file:
            oauths = file.readlines()

        print(f"[{time.strftime('%X')}] Sending message: {message}")
        irc.send(f"PASS {oauths[index % len(oauths)]}\n".encode("utf-8"))
        irc.send(f"NICK bot\n".encode("utf-8"))
        irc.send(f"JOIN #{channel}\n".encode("utf-8"))
        irc.send(f"PRIVMSG #{channel} :{message}\n".encode("utf-8"))
    else:
        print(f"[{time.strftime('%X')}] Sending message: {message}")
        irc.send(f"PASS {oauth}\n".encode("utf-8"))
        irc.send(f"NICK {nickname}\n".encode("utf-8"))
        irc.send(f"JOIN #{channel}\n".encode("utf-8"))
        irc.send(f"PRIVMSG #{channel} :{message}\n".encode("utf-8"))

    irc.close()
