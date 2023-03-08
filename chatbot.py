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
                          Edit the code, but please don't remove my name. 
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


# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
