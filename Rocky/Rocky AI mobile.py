import socket
import os
import android
from colorama import init
import colorama

init(autoreset=True)
droid = android.Android()
os.system("clear")

nightMode = False

def speak(string):
    if nightMode == False:
        print(string)
        droid.ttsSpeak(string)
    else:
        print(string)


s = socket.socket()

host = "192.168.1.105"
port = 7007

try:
    s.connect((host, port))
except:
    speak("Cannot connect to the server.")
    input("Press enter to exit")
    exit(0)

while True:
    data = s.recv(1024).decode()
    if str(data) == "what is the current directory":
        try:
            speak("You are currently working in " + os.getcwd())
        except:
            speak("Unable to detect the current working directory")
    elif str(data) == "list items":
        try:
            speak("This directory contains the following")
            files = os.listdir(os.getcwd())
            for item in files:
                print(item)
        except:
            speak("Unable to list items")
    elif str(data)[:6] == "delete":
        file = str(data)[6:]
        file = file.strip()
        try:
            if os.path.isfile(file):
                os.remove(file)
                speak(file + " is successfully deleted.")
            elif os.path.isdir(file):
                os.rmdir(file)
                speak(file + " is successfully deleted.")
            else:
                speak("There is no file named " + file)
        except:
            speak("Unable to delete the file")
    elif str(data)[:13] == "make a folder":
        folderName = str(data)[13:]
        folderName = folderName.strip()
        try:
            os.mkdir(folderName)
            speak(folderName + " is successfully created")
        except:
            speak("Unable to create the folder " + folderName)
    elif str(data)[:10] == "enter into":
        try:
            path = str(data)[10:]
            path = path.strip()
            if os.path.isdir(path) and path == "..":
                os.chdir(path)
                speak("You have gone back a folder")
            elif path == "." or path == "...":
                speak("You are in " + os.getcwd())
            elif os.path.isdir(path):
                os.chdir(path)
                speak("You have entered into " + path)
            else:
                speak("Sorry, that folder doesn't exists")
        except:
            speak("Unable to enter into the folder")
    else:
        speak(data)
    
    if data == "Good bye, see you later.":
        s.send("disconnect".encode())
        s.close()
        exit(0)
    else:

        command = input(colorama.Fore.GREEN + ">>")
        print(colorama.Fore.WHITE)

        if command == "activate night mode":
            if nightMode is False:
                nightMode = True
                print("Night mode activated")
            else:
                print("Night mode is already activated")
        elif command == "deactivate night mode":
            if nightMode is True:
                nightMode = False
                speak("Night mode is deactivated")
            else:
                speak("Night mode is already deactivated")
        s.send(command.encode())