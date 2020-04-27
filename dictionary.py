from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox

data = json.load(open("data.json"))

window = Tk()

window.configure(bg='#81de90')

window.title("Dictionary")

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
            def exception():
                txt.delete("1.0", END)
                txt.insert(END, data[word])
        else:
            tkinter.messagebox.showinfo("No such word", "There is no such word as %s " % get_close_matches(word, data.keys())[0])

def clear():
    e1.delete("0", END)
    txt.delete("1.0", END)

l1 = Label(window, bd=10, font="Times 15", text="Enter the word: ", bg='#81de90', fg="#000000")
l1.grid(row=0, column=0)

text=StringVar()
e1 = Entry(window, textvariable=text, width=30, bd=5, fg="#000000", bg='#81de90')
e1.grid(row=0, column=1)

b1 = Button(window, bd=5, font="Times 10 bold", text="Search", width=25, command=dictionary, fg="#000000")
b1.grid(row=1, column=1)

b2 = Button(window, bd=5, font="Times 10 bold", text="Clear", width=25, command=clear, fg="#000000")
b2.grid(row=1, column=0)

txt=Text(window, height=11, width=50, wrap=WORD, fg="#000000", bg='#81de90')
txt.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

txt.configure(yscrollcommand=sb1.set)
sb1.configure(command=txt.yview)

txt.bind('<<TextSelect>>')

window.mainloop()
