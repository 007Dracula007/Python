"""
This is writtern by Abhijith K A
copyright (c) 30 Nov 2017

The module lets your do casual talk with your model
"""
import win32com.client as wincl
import datetime
import os
import re

speak = wincl.Dispatch("SAPI.SpVoice")
now = datetime.datetime.now()

class Casual:

    def __init__(self):
        self.night_mode = False

    def __talk(self, string):
        if self.night_mode is False:
            print(string)
            speak.Speak(string)
        else:
            print(string)

    def __reply(self, say):
        self.__talk(say)

    def __showTime(self, server=False):
        Time = ""
        Time += str(now.day) + " "
        if now.month == 1:
            Time += "January "
        elif now.month == 2:
            Time += "February "
        elif now.month == 4:
            Time += "March "
        elif now.month == 4:
            Time += "April "
        elif now.month == 5:
            Time += "May "
        elif now.month == 6:
            Time += "June "
        elif now.month == 7:
            Time += "July "
        elif now.month == 8:
            Time += "August "
        elif now.month == 9:
            Time += "September "
        elif now.month == 10:
            Time += "October "
        elif now.month == 11:
            Time += "November "
        else:
            Time += "December "
        Time += str(now.year) + "\n"
        hour = datetime.datetime.now().hour
        meredian = ""
        if 12 < hour < 24:
            meredian = " P.M"
        else:
            meredian = " A.M"
        if hour == 13:
            hour = 1
        elif hour == 14:
            hour = 2
        elif hour == 1:
            hour = 3
        elif hour == 16:
            hour = 4
        elif hour == 17:
            hour = 5
        elif hour == 18:
            hour = 6
        elif hour == 19:
            hour = 7
        elif hour == 20:
            hour = 8
        elif hour == 21:
            hour = 9
        elif hour == 22:
            hour = 10
        elif hour == 23:
            hour = 11
        elif hour == 24:
            hour = 12
        elif hour == 0:
            hour = 12
        Time += str(hour) + " : " + str(datetime.datetime.now().minute) + str(meredian)
        if server == False:
            self.__talk(Time)
        else:
            return Time

    def __calculate(self, exp):
        try:
            self.__answer = eval(exp)
            self.__talk("The answer is " + str(self.__answer))
        except:
            self.__talk("I can't do that. Sorry")

    def __saveTask(self, task):
        alarmTime = re.findall(" \d{1,2}[: ]\d{1,2}[ ]{1}[ap]{1}m$", task)

        try:
            alarmTime[0] = alarmTime[0].strip()
            if int(alarmTime[0].split(":")[0]) <=12 and int(alarmTime[0].split(":")[0]) >=1 and int(alarmTime[0].split(":")[1].split(" ")[0]) <=60 and int(alarmTime[0].split(":")[1].split(" ")[0]) >=0 or int(alarmTime[0].split(" ")[0]) <=12 and int(alarmTime[0].split(" ")[0]) >=1 and int(alarmTime[0].split(" ")[1].split(" ")[0]) <=60 and int(alarmTime[0].split(" ")[1].split(" ")[0]) >=0:

                task = task.replace(alarmTime[0], "")
                data = "Task: " + task + " " + alarmTime[0] + "\n"

                if os.path.isdir("c:/users/adhit/pycharmprojects/rocky/Brain"):
                    os.chdir("c:/users/adhit/pycharmprojects/rocky/Brain")
                    reminders = open("reminders.txt", "a")
                    reminders.write(data)
                    reminders.close()
                else:
                    os.mkdir("c:/users/adhit/pycharmprojects/rocky/Brain")
                    os.chdir("c:/users/adhit/pycharmprojects/rocky/Brain")
                    reminders = open("reminders.txt", "w")
                    reminders.write(data)
                    reminders.close()

                self.__talk("Your reminder is saved successfully")
            else:

                self.__talk("The time format is not valid")
        except:
            self.__talk("The time format is not valid")

    def parse(self, command, fromServer=False):
        if fromServer == False:
            if command == "hello":
                self.__reply("hai")
            elif command == "hai":
                self.__reply("hello")
            elif command == "rocky":
                self.__reply("Iam here")
            elif command == "hi":
                self.__reply("Hello")
            elif command == "hey":
                self.__reply("hey there,")
            elif command == "what is your name":
                self.__reply("My name is Rocky")
            elif command == "how old are you":
                self.__reply("Iam 1 year old")
            elif command == "who created you":
                self.__reply("My master is  Sachi")
            elif command == "how are you":
                self.__reply("iam fine.")
            elif command[:2] == "do":
                self.__expression = command[2:]
                self.__expression = self.__expression.strip()
                self.__calculate(self.__expression)
            elif command == "can i change your name" or command == "may i change your name":
                self.__reply("No, because my master doesn't allow that")
            elif command[:3] == "say":
                word = command[3:].strip()
                if word == "":
                    self.__talk("Say what? hahahahahaha")
                else:
                    self.__talk(word)
            elif command == "who is your master":
                self.__reply("My master is Sachi")
            elif command == "good bye" or command == "see you later":
                self.__reply("Good bye, see you later.")
                exit(0)
            elif command == "what is the time now":
                self.__showTime()
            elif command[:15] == "remind me about":
                task = str(command[15:]).strip()
                if task == "":
                    self.__reply("Remind what?")
                else:
                    self.__saveTask(task)
            else:
                self.__reply("Sorry, I could'nt answer that")
        else:
            if command == "hello":
                return "hai"
            elif command == "hai":
                return "hello"
            elif command == "rocky":
                return "Iam here"
            elif command == "hi":
                return "Hello"
            elif command == "hey":
                return "hey there,"
            elif command == "what is your name":
                return "My name is Rocky"
            elif command == "how old are you":
                return "Iam 1 year old"
            elif command == "who created you":
                return "My master is  Sachi"
            elif command == "how are you":
                return "iam fine."
            elif command[:2] == "do":
                self.__expression = command[2:]
                self.__expression = self.__expression.strip()
                try:
                    self.__answer = eval(self.__expression)
                    return "The answer is " + str(self.__answer)
                except:
                    return "I can't do that. Sorry"
            elif command == "can i change your name" or command == "may i change your name":
                return "No, because my master doesn't allow that"
            elif command[:3] == "say":
                word = command[3:].strip()
                if word == "":
                    return "Say what? hahahahahaha"
                else:
                    return word
            elif command == "who is your master":
                return "My master is Sachi"
            elif command == "good bye" or command == "see you later":
                return "Good bye, see you later."
            elif command == "what is the time now":
                return self.__showTime(server=True)
            elif command == "activate night mode":
                return "."
            elif command == "deactivate night mode":
                return "."
            else:
                return "Sorry, I could'nt answer that"
