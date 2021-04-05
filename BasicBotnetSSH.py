import paramiko
import sys

bot = [["192.168.1.54", "22", "root", "hack"], ["192.168.1.53", "22", "kali", "kali"]]

def simpleLogin(hostname, port, username, password, compteur):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        print("[\033[0;92m+\033[0;00m]", hostname, "was \033[0;92mconnected \033[0;00mon the botnet")
    except:
        print("[\033[0;91m!\033[0;00m]", hostname, "\033[0;91mcannot connect\033[0;00m to the botnet")

def sshCommand(hostname, port, username, password, command, hide):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command(command)
        if hide == "y":
            print(stdout.read().decode())
    except:
        print("[\033[0;91m!\033[0;00m] Erreur")

def main(bot):
    print("\n\033[0;92mBasic Botnet with SSH connection \n       \033[0;91mDev by Sword\033[0;00m\n\n")
    for x in range(len(bot)):
        simpleLogin(bot[x][0], bot[x][1], bot[x][2], bot[x][3], x+1)
    while True:
        choice = input("\n>>> Do you want a return of the order ? (y/n) : ")
        if choice == "y":
            command = input(">>> Enter the command to be executed on all bots in the botnet : ")
            for x in range(len(bot)):
                sshCommand(bot[x][0], bot[x][1], bot[x][2], bot[x][3], command, "y")
        else:
            command = input(">>> Enter the command to be executed on all bots in the botnet : ")
            for x in range(len(bot)):
                sshCommand(bot[x][0], bot[x][1], bot[x][2], bot[x][3], command, "n")

main(bot)










