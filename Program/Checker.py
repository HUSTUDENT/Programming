import os
import winreg
import socket
import smtplib
from email.mime.text import MIMEText
from random import randint
from tkinter import *
import tkinter.messagebox as tm
import time
import sys
import datetime
import tkinter.filedialog
import tkinter.ttk as ttk
from configparser import ConfigParser

parser = ConfigParser()
parser.read("Config.ini")
parser.sections()
parser.set("Main", "Pop", "1")
parser.set("Main", "Pop2", "3")
with open("Config.ini", "w") as configfile:
    parser.write(configfile)

print(parser.sections())
