import socket
import casual
import online
import datetime

now = datetime.datetime.now()
casualTalk = casual.Casual()
ask = online.Online()

def serverProcess(data, s, addr):
    try:
        data = data.lower()

        sysC = (
                    "what is the current directory",
                    "list items",
                    "delete",
                    "make a folder",
                    "enter into",
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
                            "activate night mode",
                            "deactivate night mode"
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

        if data == "help":
            items = "You can ask me anything plus the following commands too,\n"
            for item in sysC:
                items += item + "\n"
            for item2 in casualC:
                items += item2 + "\n"
            for item3 in onlineC:
                items += item3 + "\n"
            return  items
        elif data in sysC:
            result = str(data)
            return result
        elif data[:6] == "delete":
            result = str(data)
            return result
        elif data[:13] == "make a folder":
            result = str(data)
            return result
        elif data[:10] == "enter into":
            result = str(data)
            return result
        elif data in casualC:
            result = casualTalk.parse(data, fromServer=True)
            return result
        elif data[:2] in casualC:
            result = casualTalk.parse(data, fromServer=True)
            return result
        elif data[:3] in casualC:
            result = casualTalk.parse(data, fromServer=True)
            return result
        elif data[:15] in casualC:
            result = casualTalk.parse(data, fromServer=True)
            return result
        elif data[:3] in onlineC or data[:4] in onlineC or data[:5] in onlineC or data[:6] in onlineC or data[:2] in onlineC:
            try:
                result = ask.parse(data, fromServer=True)
                return result
            except:
                return "Please check your internet connection"
        else:
            return "Sorry, I dont understand that"
    except:
        print("A device disconnnected")


def server():
    s = socket.socket()

    host, port = "192.168.1.105", 7007

    s.bind((host, port))

    while True:
        if now.hour < 12:
            message = "Good Morning, Iam Rocky and what can I do for you"
        elif 12 <= now.hour < 20:
            message = "Good afternoon, Iam Rocky and what can I do for you"
        else:
            message = "Hello night owl, Iam Rocky and what can I do for you"
        try:
            s.listen(5)
            c, addr = s.accept()

            while True:

                c.send(message.encode())
                command = c.recv(1024).decode()

                if command == "disconnect":
                    if now.hour < 12:
                        message = "Good Morning, Iam Rocky and what can I do for you"
                    elif 12 <= now.hour < 20:
                        message = "Good afternoon, Iam Rocky and what can I do for you"
                    else:
                        message = "Hello night owl, Iam Rocky and what can I do for you"
                    break
                message = serverProcess(command, s, addr)
        except:
            c.close()
            continue
