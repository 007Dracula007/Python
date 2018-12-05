"""
This is writtern by Abhijith K A
copyright (c) 30 Nov 2017

The module lets your speaking model to interact with the OS(default=windows)
"""
import os
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

class System:

    def __init__(self):
        self.night_mode = False
        self.__message = ""

    def __talk(self, string):
        if self.night_mode is False:
            print(string)
            speak.Speak(string)
        else:
            print(string)

    def __open(self, file):
        if os.path.isfile(file):
            os.system("\"" + file + "\"")
            self.__talk(file + " is opened and closed successfully")
        else:
            self.__talk("Sorry, that file doesn't exist")

    def __getCwd(self):
        self.__message = os.getcwd()
        self.__message = self.__message.replace("\\", " ")
        self.__talk("You are currently working in")
        self.__talk(self.__message)


    def __listItems(self):
        self.__list = os.listdir()
        if self.__list == []:
            self.__talk("This directory is empty")
        else:
            self.__message = "This directory contains the following"
            self.__talk(self.__message)
            for item in self.__list:
                print(item)

    def __delete(self, file):
        file = file.strip()
        if os.path.isfile(file):
            os.remove(file)
            self.__talk(file + " is removed successfully")
        elif os.path.isdir(file):
            try:
                os.rmdir(file)
                self.__talk(file + " is removed successfully")
            except:
                self.__talk(file + " was unable to remove. The folder may not be empty.")
        else:
            self.__talk("Sorry, that file doesn't exist")

    def __mkdir(self, folderName):
        try:
            os.mkdir(folderName)
            self.__talk(folderName + " is created successfully")
        except:
            self.__talk("Unable to create the folder " + folderName)

    def __browse(self, url):
        if url == "":
            self.__talk("The URL seems to be invalid!")
        else:
            try:
                os.system("start chrome " + url)
                self.__talk(url + " is opened up in the browser")
            except:
                self.__talk("Something went wrong, make sure you have installed chrome browser")

    def __chdir(self, folderName):
        if os.path.isdir(folderName):
            os.chdir(folderName)
            if folderName != ".." and folderName != "." and folderName != "...":
                self.__talk("You have enterd into " + folderName)
            elif folderName == "..":
                self.__talk("You have gone back to a directory")
            else:
                folderName = os.getcwd()
                folderName = folderName.replace("\\", " ")
                self.__talk("You are in " + folderName)
        else:
            self.__talk("Sorry, that path doesn't exist")

    def parse(self, command):
        if command == "what is the current directory":
            self.__getCwd()
        elif command == "list items":
            self.__listItems()
        elif command == "deploy rico":
            os.system("\"c:/users/adhit/pycharmprojects/rocky/tools/rico rigid text editor/rico.exe\"")
        elif command == "enter into root":
            os.chdir("c:/users/adhit/pycharmprojects/rocky")
            self.__talk("You are now in root directory")
        elif command[:6] == "delete":
            self.__delete(command[6:])
        elif command[:13] == "make a folder":
            folderName = command[13:].strip()
            self.__mkdir(folderName)
        elif command[:10] == "enter into":
            folderName = command[10:]
            folderName = folderName.strip()
            self.__chdir(folderName)
        elif command[:4] == "open":
            file = command[4:].strip()
            self.__open(file)
        elif command[:6] == "browse":
            url = str(command[6:]).strip()
            self.__browse(url)
        else:
            self.__talk("Sorry I couldn't understand that")