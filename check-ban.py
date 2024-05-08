import socket
import time

server = "irc.chat.twitch.tv"
port = 6667
oauth_file = "oauths.txt"

def get_oauth_tokens():
    with open(oauth_file, "r") as file:
        return [line.strip() for line in file.readlines()]

def remove_token(token):
    with open(oauth_file, "r") as file:
        lines = file.readlines()
    with open(oauth_file, "w") as file:
        for line in lines:
            if line.strip() != token:
                file.write(line)
    print(f"Token {token} has been removed from oauths.txt")

def connect_to_irc(oauth_token):
    nickname = "your_twitch_username"
    channel = "#eleezabet"

    irc = socket.socket()
    irc.connect((server, port))

    irc.send(f"PASS {oauth_token}\n".encode())
    irc.send(f"NICK {nickname}\n".encode())
    irc.send(f"JOIN {channel}\n".encode())

    while True:
        data = irc.recv(1024).decode()
        print(data)

        if "Login authentication failed" in data:
            print("Login authentication failed. Removing token...")
            remove_token(oauth_token)
            break

        if data.startswith(f":{nickname}!{nickname}@{nickname}.tmi.twitch.tv JOIN {channel}"):
            print("Successfully connected.")

        if f"{channel} :End of /NAMES list" in data:
            print("Token alived.")
            break

        if data.startswith("PING"):
            irc.send("PONG\n".encode())
            break

    irc.close()

def main():
    oauth_tokens = get_oauth_tokens()

    for token in oauth_tokens:
        print(f"Connecting with token: {token}")
        connect_to_irc(token)
        time.sleep(30)

if __name__ == "__main__":
    main()
