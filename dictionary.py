from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox

data = json.load(open("data.json"))

window = Tk()

def dictionary():
    word = e1.get()
    word = word.lower()
    if word in data:
        txt.delete("1.0", END)
        txt.insert(END, data[word])
    elif word.title() in data:
        txt.delete("1.0", END)
        txt.insert(END, data[word.title()])  
    elif word.upper() in data:
        txt.delete("1.0", END)
        txt.insert(END, data[word.upper()])   
    elif len(get_close_matches(word, data.keys())) > 0:
        ask = tkinter.messagebox.askquestion("Word not found", "Trying to search %s? " % get_close_matches(word, data.keys())[0])
        # ask = ask.lower()
        if ask == 'yes':
            # if word in data:
            #     txt.delete("1.0", END)
            #     txt.insert(END, data[word])
            # elif word.title() in data:
            #     txt.delete("1.0", END)
            #     txt.insert(END, data[word.title()])  
            # elif word.upper() in data:
            #     txt.delete("1.0", END)
            #     txt.insert(END, data[word.upper()]) 
            # else:
            #     window.destroy()

l1 = Label(window, text="Enter the word: ")
l1.grid(row=0, column=0)

text=StringVar()
e1 = Entry(window, textvariable=text, width=30)
e1.grid(row=0, column=1)

b1 = Button(window, text="Search", width=25, command=dictionary)
b1.grid(row=1, column=1)

txt=Text(window, height=11, width=50, wrap=WORD)
txt.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

txt.configure(yscrollcommand=sb1.set)
sb1.configure(command=txt.yview)

txt.bind('<<TextSelect>>')

window.mainloop()