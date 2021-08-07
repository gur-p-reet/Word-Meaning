
import json
from difflib import get_close_matches
from tkinter.font import BOLD
from typing import List 
from tkinter import *

window=Tk()
width  = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{int(width/2)}x{int(height/2)}')

window.title(20*" "+'Dictionary')

frame=Frame(window, bg="salmon", relief=GROOVE, borderwidth=10)
# frame.grid(row=0,column=0, rowspan=2,columnspan=2)
frame.pack(fill=BOTH, expand=True)

def meaning(word):
    word=word.lower()

    if word in data:
        return(data[word])
    elif len(get_close_matches(word, data.keys()))>0:
        yesno= input("Do you mean: \"%s\" ? Yes/No  " % get_close_matches(word,data.keys())[0])
        if yesno=="Yes":
            return(data[get_close_matches(word,data.keys())[0]])
        elif yesno=="No":
            return "Please chek the entered word and enter the correct word"
    else:
        return "Please make sure the word is correct"

lb1=Label(frame, text=" Enter the word", font=(16), bd=5,borderwidth=10,bg="salmon" )
lb1.grid(row=0,column=0)

entry1=StringVar()
e1=Entry(frame,textvariable=entry1,font=(16))
e1.grid(row=1,column=0, columnspan=2)


lb2=Label(frame, text=" Meaning ", font=(16), bd=5,borderwidth=10,bg="salmon" )
lb2.grid(row=2,column=0,columnspan=4)

data=json.load(open("data.json"))


word =input("Enter the word:" )

output=meaning(word)

if type(output)==List:
    for item in output:
        print(item)
    
else:
    print(output)

window.mainloop()