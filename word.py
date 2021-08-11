
import json
from difflib import get_close_matches
from tkinter.font import BOLD
from typing import List 
from tkinter import *
from tkinter import filedialog
from tkinter import font
from colorama import init
from termcolor import colored
import mysql.connector 


con=mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)
cursor=con.cursor()
word='line'

window=Tk()

data=json.load(open("data.json"))

width  = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{int(width/2)}x{int(height/2)}')

window.title(20*" "+'Dictionary')

def output(word):
    t1.delete('1.0',END)
    word1=word.capitalize()
    t1.insert(END, "\n"+  word1 +":\n", 'bold_italics')
    query=cursor.execute("SELECT * FROM Dictionary WHERE Expression=%(wrd)s",{ 'wrd': word})
    results=cursor.fetchall()
    if type(results)==list:
        for item in results:
            t1.insert(END, "- "+item[1])
            t1.insert(END,"\n")
    else:
        t1.insert(END, results)
    
    e1.delete(0,END)
def forget():
    lb3.grid_forget()
    bt2.grid_forget()
    bt3.grid_forget()

def yes():
    word=get_close_matches(e1.get().lower(),data.keys())[0]
    output(word)
    forget()
   
def no():
    t1.delete('1.0',END) 
    t1.insert(END,"Please chek the entered word and enter the correct word")
    e1.delete(0,END)
    forget()

def meaning(*arg):
    forget()
    t1.delete('1.0',END)
    word=e1.get().lower()
    if word in data:
        output(word)
    elif len(get_close_matches(word, data.keys()))>0:
        global lb3, bt2, bt3
        lb3=Label(frame, text="Do you mean: \"%s\" ? Yes/No  " % get_close_matches(word,data.keys())[0], font='Helvetica 13 bold', bd=5,borderwidth=10,bg="salmon" )
        lb3.grid(row=5,column=1, columnspan=3)
                  
        bt2.grid(row=6,column=3,rowspan=2, sticky=N)
        bt3.grid(row=6,column=4,rowspan=2, sticky=N)  
    
frame=Frame(window, bg="salmon", relief=GROOVE, borderwidth=10)
frame.pack(fill=BOTH, expand=True)


Grid.rowconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 0, weight=1)
for x in range(30):
  Grid.columnconfigure(frame, x, weight=1)
for y in range(40):
  Grid.rowconfigure(frame, y, weight=1)
  
for i in range(5):
    lb="Column"
    lb=lb+str(i)
    lb=Label(frame, text="", bg="salmon", width=5)
    lb.grid(row=1,column=i)

for i in range(10):
    lb="Column"
    lb=lb+str(i)
    lb=Label(frame, text="", bg="salmon", width=13)
    lb.grid(row=i,column=1)

def enter(event=None):
    word=e1.get()
    meaning()
lb1=Label(frame, text="Enter The word", font='Helvetica 16 bold', bd=5,borderwidth=10,bg="salmon" )
lb1.grid(row=3,column=1,columnspan=2, sticky=N+S+E+W)

entry1=StringVar()
e1=Entry(frame,textvariable=entry1, font=(10),width=25)
e1.bind('<Return>', meaning)
e1.grid(row=4,column=2,  rowspan=1, columnspan=2, sticky=N+S+E+W)

bt1=Button(frame, text="Submit",command=meaning)

bt1.grid(row=4,column=4,rowspan=1, sticky=N+S+E)


lb3=Label(frame, text="", font='Helvetica 16 bold', bd=5,borderwidth=10,bg="salmon" )
bt2=Button(frame, text="Yes",command=yes)
bt3=Button(frame, text="No",command=no)

lb2=Label(frame, text=" Word Meaning", font='Helvetica 16 bold', bd=5,borderwidth=10,bg="salmon" )
lb2.grid(row=3,column=6, columnspan=2, sticky=N+S+E+W)

t1=Text(frame,height=20,font=(14), width=45)
t1.grid(row=4,column=7, rowspan=20, columnspan=15, sticky=N+S+E+W)

t1.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
t1.tag_configure('big', font=('Verdana', 16, 'bold'))
t1.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))

window.mainloop()