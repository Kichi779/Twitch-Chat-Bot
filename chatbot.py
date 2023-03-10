import os
import time
import socket
from colorama import Fore
from pystyle import Center, Colors, Colorate

os.system(f"title Kichi779 - Twitch Chat bot v1.5 ")

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
                                       Discord https://discord.gg/aVk4JUFukk       
                                       Github  https://github.com/kichi779          
                       
                      
                      """)))


server = "irc.chat.twitch.tv"
port = 6667
channel = input("Enter your channel name: ")
message_option = input("How do you want to send messages? (1. Send messages from messages.txt, 2. Send messages by selecting a bot): ")
oauths = []

if message_option == "1":
    with open("messages.txt", "r") as file:
        messages = file.readlines()

    interval = int(input("How often should your messages be sent? (Seconds): "))
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

        bot_choice = int(input("Select a bot to send the message with (1, 2, 3, ...): "))
        if bot_choice > len(oauths):
            print("Invalid bot choice!")
            time.sleep(5)
            exit()

        oauth = oauths[bot_choice-1].strip()
        nickname = f"bot_{bot_choice}"
        message = input("Enter the message you want to send: ")

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