# import os
# import winreg
# import socket
# import smtplib
# from email.mime.text import MIMEText
# from random import randint
from tkinter import *
# import tkinter.messagebox as tm
# import time
# import sys
# import datetime
# import tkinter.filedialog
# import tkinter.ttk as ttk
# from configparser import ConfigParser


root = Tk()
root.configure(background="grey")


class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_1 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_2 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_3 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_4 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_5 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_6 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_7 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_8 = Label(self, width=10, anchor=E, justify=RIGHT, text="Hey")
        self.label_1.grid(row=0, rowspan=3)
        self.label_2.grid(row=1, rowspan=3)
        self.label_3.grid(row=2, rowspan=3)
        self.label_4.grid(row=3, rowspan=3)
        self.label_5.grid(row=4, rowspan=3)
        self.label_6.grid(row=5, rowspan=3)
        self.label_7.grid(row=6, rowspan=3)
        self.label_8.grid(row=7, rowspan=3)

        self.closebtn = Button(self, text="Close", command=self._close_btn_clickked)
        self.closebtn.grid(row=1, column=4)
        self.pack()

    def _close_btn_clickked(self):
        self.master.destroy()


mf = MainFrame(root)
mf.mainloop()
