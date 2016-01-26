__author__ = 'flg8r77'

import tkinter as tk

LARGE_FONT = ('Verdana', 12)

class SeaOfBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

''' Define an empty dictionary. 
	this dictionary will contain all the frames the we defined for
	for our program.
'''
        self.frames = {} 

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="SeaOfBTC", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

app = SeaOfBTCapp()
app.mainloop()