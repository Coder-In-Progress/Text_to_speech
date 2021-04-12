/***********************************************************************
Application    : Google enhancement
Author         : Coder_In_Progress
Version        : 1.0
***********************************************************************/

from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime

plus_var = (var1 + var2)
var1 = input("Type what you want the computer to say \n")
var2 = input("Is there anything else? Type n/a if you have nothing to say")

if var2 == "n/a"
  Continue


def speak(plus_var):
	tts = gTTS(text=plus_var, lang="en")
	filename = "recording.mp3"
	tts.save(filename)
	playsound.playsound(filename)
