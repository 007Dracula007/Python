"""
This is writtern by Abhijith K A
copyright (c) 30 Nov 2017

The module lets your search, ask questions or doubts to your model
"""

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import win32com.client as wincl
import re


speak = wincl.Dispatch("SAPI.SpVoice")

class Online:

    def __init__(self):
        self.night_mode = False

    def __talk(self, string):
        if self.night_mode is False:
            print(string)
            speak.Speak(string)
        else:
            print(string)

    def __prettifyCont(self, content):
        content = content.replace("Wikipedia", "Wikipedia\n")
        keywords = ("Born", "Died", "Full name", "ODI", "Test", "Last", "T20I", "Height", "Parents", "Assassinated", "Siblings", "Available on", "Awards", "Nicknames", "Spouse", "Salary", "Children", "Did you know")
        for item in keywords:
            if content.find(item):
                content = content.replace(item, "\n"+item)
        return content

    def __getInfo(self, query, server=False):
        if server == False:
            query = urllib.parse.quote(str(query))
            url = "https://www.google.com/search?q=" + query
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            data = BeautifulSoup(data, "html5lib")
            data = data.find("span", {"class": "st"})
            if data != None:
                data = str(data).replace(".", ".\n")
                data = re.sub("<[^>]+>", "", str(data))
                self.__talk(data)
            else:
                self.__talk("I don't get any information about that, sorry!")
        else:
            query = urllib.parse.quote(str(query))
            url = "https://www.google.com/search?q=" + query
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            data = BeautifulSoup(data, "html5lib")
            data = data.find("span", {"class": "st"})
            if data != None:
                data = str(data).replace(".", ".\n")
                data = re.sub("<[^>]+>", "", str(data))
                return str(data)
            else:
                return "I don't get any information about that, sorry!"

    def __search(self, query, server=False):
        if server == False:
            query = urllib.parse.quote(str(query))
            url = "https://www.google.com/search?q=" + query
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            html = BeautifulSoup(data, "html5lib")
            content = html.find("div", {"class": "_G1d _wle _xle"})
            if content == None:
                self.__talk("Sorry, I can't get any information about " + query)
            else:
                content = re.sub("<[^>]+>", "", str(content))
                content = self.__prettifyCont(content)
                self.__talk(content)
        else:
            query = urllib.parse.quote(str(query))
            url = "https://www.google.com/search?q=" + query
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            html = BeautifulSoup(data, "html5lib")
            content = html.find("div", {"class": "_G1d _wle _xle"})
            if content == None:
                return "Sorry, I can't get any information about " + query
            else:
                content = re.sub("<[^>]+>", "", str(content))
                content = self.__prettifyCont(content)
                return content

    def parse(self, command, fromServer=False):
        if fromServer == False:
            if command[:6] == "search":
                query = command[6:]
                query = query.strip()
                self.__search(query)
            elif command[:3] == "who" or command[:3] == "how" or command[:4] == "when" or command[:3] == "why" or command[:4] == "what" or command[:5] == "where" or command[:3] == "can" or command[:3] == "may" or command[:2] == "is":
                self.__getInfo(command)
            else:
                self.__talk("Sorry, I cant do that")
        else:
            if command[:6] == "search":
                query = command[6:]
                query = query.strip()
                return str(self.__search(query, server=True))
            elif command[:3] == "who" or command[:3] == "how" or command[:4] == "when" or command[:3] == "why" or command[:4] == "what" or command[:5] == "where" or command[:3] == "can" or command[:3] == "may" or command[:2] == "is":
                return str(self.__getInfo(command, server=True))
            else:
                return "Sorry, I cant do that"
