import tkinter
import os
import configparser
from tkinter import *
import ttkbootstrap

import constants
from clicking.scrapping import ScrapeWeb


class GuiCreator(object):

    def __init__(self):
        self.path_ico = r"G:\pycharm\pythonProject\DirectClickTkinter\images"
        self.image_name = "click.ico"
        self.scrapper = ScrapeWeb()

    def create_window(self, window):
        global button_git
        global button_linkedin
        global button_flashscore
        label_title = ttkbootstrap.Label(window, text="CHOOSE LINK TO AUTOMATICALLY OPEN",
                                         style='warning.Inverse.TLabel', font=("Comic Sans Ms", 13, "bold"), padding=3)
        label_title.grid(row=0, column=0, padx=10, pady=30)
        # CREATE BUTTONS
        frame_buttons = ttkbootstrap.LabelFrame(window, text="BUTTONS", borderwidth=6, relief=tkinter.GROOVE, width=350,
                                                height=90)
        frame_buttons.grid(row=1, column=0, pady=5)
        button_linkedin = ttkbootstrap.Button(frame_buttons, text="LINKEDIN", width=15, style="info.Tbutton",
                                              command=lambda: self.scrapper.open_browser(constants.LINKEDIN))
        button_linkedin.grid(row=0, column=0, padx=8)
        button_git = ttkbootstrap.Button(frame_buttons, text="GIT", width=15, style="secondary.Tbutton",
                                         command=lambda: self.scrapper.open_browser(constants.GIT))
        button_git.grid(row=0, column=1, padx=8)
        button_flashscore = ttkbootstrap.Button(frame_buttons, text="FILELIST", width=15, style="success.Tbutton",
                                             command=lambda: self.scrapper.open_browser(constants.FILELIST))
        button_flashscore.grid(row=0, column=2, padx=8)

    def create_main_gui(self):
        root = ttkbootstrap.Window(themename="superhero")
        root.title("LinkOpener")
        root.geometry("400x200")
        root.iconbitmap(os.path.join(self.path_ico, self.image_name))
        self.create_window(root)
        root.mainloop()
