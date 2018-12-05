import win32com.client as wincl
import system_interaction
import casual
import online
import os
import speech_recognition as sr
import datetime
import threading
import time
import server
import pentest


now = datetime.datetime.now()
speak = wincl.Dispatch("SAPI.SPVoice")
sys = system_interaction.System()
casualTalk = casual.Casual()
ask = online.Online()
pen = pentest.Pentest()
r = sr.Recognizer()
speak_mode = False
night_mode = False

def reminders():

    file = "c:/users/adhit/pycharmprojects/rocky/brain/reminders.txt"
    while True:
        if os.path.isfile(file):
            hour = datetime.datetime.now().hour
            meredian = ""
            if 12 < hour < 24:
                meredian = " pm"
            else:
                meredian = " am"
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

            times = str(hour) + ":" + str(datetime.datetime.now().minute) + str(meredian)
            flag = 0
            reminder = open(file, "r")
            data = ""
            try:
                for line in reminder:
                    if times in line:
                        flag = 1
                        talk("You have a reminder:" + line + ">>")
                        data = reminder.read()
                        data.replace(line, "")
                        break
                if flag == 1:
                    reminder.close()
                    reminder = open(file, "w")
                    reminder.write(data)
                    reminder.close()
                    time.sleep(65)
            except:
                talk("There's a problem while reading your reminders.")


def talk(string):
    global night_mode
    if night_mode is False:
        print(string)
        speak.Speak(string)
    else:
        print(string)

def process(data):
    global speak_mode
    global night_mode
    data = data.strip()
    data = data.lower()

    sysC =  (
                    "what is the current directory",
                    "list items",
                    "delete",
                    "make a folder",
                    "enter into",
                    "open",
                    "browse",
                    "enter into root",
                    "deploy rico"
                    )

    casualC = (
                        "rocky",
                        "hello",
                        "hai",
                        "hi",
                        "hey",
                        "what is your name",
                        "how old are you",
                        "who created you",
                        "how are you",
                        "good bye",
                        "do",
                        "can i change your name",
                        "may i change your name",
                        "who is your master",
                        "see you later",
                        "say",
                        "what is the time now",
                        "remind me about"
                         )

    onlineC = (
                        "search",
                        "what",
                        "how",
                        "when",
                        "why",
                        "where",
                        "who",
                        "can",
                        "may",
                        "is"
                        )

    pentestC = (
                    "start pentesting",
                    "come to normal",
                    "enable malicious rocky",
                    "create a backdoor",
                    "create backdoor for windows",
                    "create backdoor for linux",
                    "create backdoor for mac",
                    "deploy handler for backdoor",
                    "deploy handler"
    )

    if data == "help":
        talk("You can ask me any questions also you can command me to do something, examples are")
        for item in sysC:
            print("* ", item)
        for item in casualC:
            print("* ", item)
        print("* activate speak mode")
        print("* deactivate speak mode")
        print("* activate night mode")
        print("* deactivate night mode")
    elif data == "activate speak mode":
        if speak_mode is False:
            speak_mode = True
            talk("Speak mode activated")
        else:
            talk("Speak mode is already activated")
    elif data == "deactivate speak mode":
        if speak_mode is True:
            speak_mode = False
            talk("Speak mode deactivated")
        else:
            talk("Speak mode is already deactivated")
    elif data == "activate night mode":
        if night_mode is False:
            night_mode = True
            sys.night_mode = True
            casualTalk.night_mode = True
            ask.night_mode = True
            pen.nightMode = True
            talk("Night mode activated")
        else:
            talk("Night mode is already activated")
    elif data == "deactivate night mode":
        if night_mode is True:
            night_mode = False
            sys.night_mode = False
            casualTalk.night_mode = False
            ask.night_mode = False
            talk("Night mode deactivated")
        else:
            talk("Night mode is already deactivated")
    elif data in sysC:
        sys.parse(data)
    elif data[:4] in sysC:
        sys.parse(data)
    elif data[:6] in sysC:
        sys.parse(data)
    elif data[:13] in sysC:
        sys.parse(data)
    elif data[:10] in sysC:
        sys.parse(data)
    elif data in casualC:
        casualTalk.parse(data)
    elif data[:2] in casualC:
        casualTalk.parse(data)
    elif data[:3] in casualC:
        casualTalk.parse(data)
    elif data[:15] in casualC:
        casualTalk.parse(data)
    elif data[:3] in onlineC or data[:4] in onlineC or data[:5] in onlineC or data[:6] in onlineC or data[:2] in onlineC:
        try:
            ask.parse(data)
        except:
            talk("Please check your Internet connection and try again.")
    elif data in pentestC:
        pen.parse(data)
    else:
        talk("Sorry, I couldn't understand that")

def speech():

    with sr.Microphone() as source:
        print("listening..")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        get = str(r.recognize_google(audio))
        print(">>" + get)
    except sr.UnknownValueError:
        get = "null"
    except sr.RequestError:
        get = "null"
    return get

def type():
    get = str(input(">>"))
    return get

def main():
    global speak_mode, night_mode
    os.system("cls")

    if now.hour < 12:
        message = "Good Morning, Iam Rocky and what can I do for you"
    elif 12 <= now.hour < 20:
        message = "Good afternoon, Iam Rocky and what can I do for you"
    else:
        night_mode = True
        sys.night_mode = True
        casualTalk.night_mode = True
        ask.night_mode = True
        message = "Hello night owl, Iam Rocky and what can I do for you\nNight mode is activated"

    talk(message)

    while True:
        if speak_mode is True:
           get = speech()
        else:
            get = type()
        process(get)

if __name__ == '__main__':
    connections = threading.Thread(target=server.server)
    connections.setDaemon(True)
    connections.start()
    bgPro = threading.Thread(target=reminders)
    bgPro.setDaemon(True)
    bgPro.start()
    main()