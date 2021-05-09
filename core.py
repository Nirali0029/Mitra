#import libraries
from time import sleep
from threading import *
import tkinter as tk
import speech_recognition as sr
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import time
import webbrowser
import subprocess
import wolframalpha  # G5WP8V-Q2AGJ7JH8G
import json
import requests
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *
from PIL import Image, ImageTk

#global root;
#root=tk.Tk()

#methods to accomplise tasks
def begin(text):
    root = tk.Tk()
    #root.geometry('700x800')
    style = Style()
    style.configure("BW.TLabel",
                    foreground="black",
                    # background="white",
                    font=("CenturyGothic", 30))
    label_frame = LabelFrame(root)
    label_frame.pack(expand='yes', fill='both')
    app=FullScreenApp(root)

    label1 = Label(label_frame, text=text, style='BW.TLabel')
    label1.place(x=350, y=350)
    root.after(5000, lambda: root.destroy())     
    root.mainloop()
    #root.destroy()


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

        
class Window(Thread):
    def run(self):
        begin("Listening...") 
        #print("Hii")


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'voices[0].id')
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            begin('Pardon me, Please say that again')
            return "None"
        return statement

#threading to run tkinter window and code
class Speech(Thread):
    def wishMe():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak("Hello,Good Morning")
            begin('Good Morning')
            print("Hello,Good Morning")
        elif hour >= 12 and hour < 18:
            speak("Hello,Good Afternoon")
            begin("Good Afternoon")            
            print("Hello,Good Afternoon")
        else:
            speak("Hello,Good Evening")
            begin("Good Evening")
            print("Hello,Good Evening")

    speak("Loading your AI personal assistant Meetra")

    wishMe()
    
 #main method
    def run(self):
        if __name__ == '__main__':
            while True:
                speak("Tell me how can I help you now?")
                statement = takeCommand().lower()
                if statement == 0:
                    continue

                if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                    speak('your personal assistant Mitra is shutting down,Good bye')
                    begin("Byeee, Shutting Down")                    
                    print('your personal assistant Mitra is shutting down,Good bye')
                    break

                if 'wikipedia' in statement:
                    speak('Searching Wikipedia...')
                    begin("Searching Wikipedia")
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in statement:
                    begin('Opening Youtube')
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif 'open google' in statement:
                    begin('Opening Google')
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)

                elif 'open gmail' in statement:
                    begin('Opening Gmail')
                    webbrowser.open_new_tab("gmail.com")
                    speak("Google Mail open now")
                    time.sleep(5)

                elif 'open spotify' in statement:
                    begin('Opening Spotify')

                    webbrowser.open_new_tab("spotify.com")
                    speak("Spotify open now")
                    time.sleep(5)

#tkinter root window to display the messages by Mitra
t2 = Window()
t1 = Speech()

t2.start()
sleep(1)
t1.start()

t1.join()
t2.join()
