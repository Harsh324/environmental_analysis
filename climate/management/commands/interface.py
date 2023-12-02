from django.core.management.base import BaseCommand

from ctypes import alignment, sizeof
import tkinter
from tkinter import Canvas, Label, Listbox, Scrollbar, ttk, font
from tkinter.constants import CENTER
from typing import Text

from scipy.ndimage.measurements import label

from climate.gui import interface_global
from climate.gui import interface_rain
from climate.gui import interface_india
from climate.gui import interface_wbd

# About Tab


def About(notebook):
    AbtFrame = tkinter.Frame(notebook, bg='skyblue')
    notebook.add(AbtFrame, text='About')
    frame1 = tkinter.LabelFrame(AbtFrame, text="Analysis of Climate Change",font=("Courier", 14),bg='gold')
    frame1.grid(column=0, row=0, padx=20, pady=4)

    para = tkinter.Label(
        frame1, text="The program will analyze changes in the climate over an interval. It will also generate \nthe distribution curve of the data. ", font=("Courier", 17),bg='gold2')
    para.grid(column=0, row=0, sticky=tkinter.W, pady=10)

    frame2 = tkinter.LabelFrame(AbtFrame, text="Tech stack",bg='seagreen3',font=("Courier",14))
    frame2.grid(column=0, columnspan=2, row=1, padx=8, pady=4)

    para2_1 = tkinter.Label(frame2, text="Numpy & Scipy : Data Analysis",font=(17),bg='palegreen').grid(
        column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
    para2_2 = tkinter.Label(frame2, text="Pandas : Data Manipulation",font=(17),bg='palegreen').grid(
        column=0, row=1, sticky=tkinter.W, padx=10, pady=10)
    para2_3 = tkinter.Label(frame2, text="Matplotlib : Data Representation",font=(17),bg='palegreen').grid(
        column=0, row=2, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="CSV : File Handling",font=(17),bg='palegreen').grid(
        column=0, row=3, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Pyautogui : GUI Automation",font=(17),bg='palegreen').grid(
        column=0, row=4, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Selenium : Browser Automation",font=(17),bg='palegreen').grid(
        column=0, row=5, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Tkinter : Python GUI",font=(17),bg='palegreen').grid(
        column=0, row=6, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Exception Handling",font=(17),bg='palegreen').grid(
        column=0, row=7, sticky=tkinter.W, padx=10, pady=10)


# Temperature tab

def Temp(notebook):
    TempFrame = tkinter.Frame(notebook)
    notebook.add(TempFrame, text='Temperature')
    Tempframe = ttk.Notebook(TempFrame)
    TempNotebook(Tempframe)


# Nested Temperature Tab

def TempNotebook(Tempframe):
    Tempframe.pack(expand=True, fill='both')
    GlobalNotebook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(GlobalNotebook, text="Global_Kaggle_Dataset")

    interface_global.countryBox(
        GlobalNotebook, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 0)
    interface_global.stateBox(
        GlobalNotebook, "States Comparision", "Enter States Name (Comma Seperated)", 1)
    interface_global.cityBox(
        GlobalNotebook, "Cities Comparision", "Enter Cities Name (Comma Seperated)", 2)

    GlobalWBDNoteBook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(GlobalWBDNoteBook, text="Global_WBD_Dataset")

    interface_wbd.countryBox(
        GlobalWBDNoteBook, "Country Analysis", "Enter Country Name", 0)
    interface_wbd.countryBox(GlobalWBDNoteBook, "Countries Comparision",
                            "Enter Countries Name (Comma Seperated)", 1)
    interface_wbd.stateBox(
        GlobalWBDNoteBook, "State Analysis", "Enter State Name", 2)
    interface_wbd.stateBox(GlobalWBDNoteBook, "States Comparision",
                          "Enter States Name (Comma Seperated)", 3)

    IndiaNoteBook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(IndiaNoteBook, text="India_Dataset")

    interface_india.IndiaBox(
        IndiaNoteBook, "India Analysis", "Enter Month (required)", 0)


# Rainfall Tab

def Rain(notebook):
    RainFrame = tkinter.Frame(notebook, border=10,bg='skyblue3')
    notebook.add(RainFrame, text="Rainfall")

    interface_rain.countryBox(RainFrame)
    interface_rain.countriesBox(RainFrame)
    interface_rain.stateBox(RainFrame)
    interface_rain.statesBox(RainFrame)


class Command(BaseCommand):
    help = 'Runs the gui for the environmental analysis'

    def handle(self, *args, **options):
        win = tkinter.Tk()
        win.title("Python Mini Project")
        win.attributes('-zoomed', 1)

        # label=Label(text="Python Mini Project : Climate Change Analysis",font=("Noto Serif",17),bg='khaki')
        # label.pack()
        # win.configure(background='gray55')

        style = ttk.Style()
        style.theme_settings
        ("default",
        {"TNotebook.Tab": {"configure": {"padding": [0, 0]},
                            "map": {"background": [("active", "green"),
                                                ("!disabled", "orange")],
                                    "fieldbackground": [("!disabled", "blue")],
                                    "foreground": [("focus", "blue"),
                                                ("!disabled", "black"),
                                                ("active", 'red')],font:[("15")]}}})

        notebook = ttk.Notebook(win, width=100)
        notebook.pack(expand=0, fill='both', padx=0, pady=0)
        #About(notebook)
        Temp(notebook)
        Rain(notebook)

        win.mainloop()