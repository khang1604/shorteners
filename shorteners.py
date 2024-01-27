from tkinter import *
import pyshorteners
import pyperclip 

def short_link():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    short_url_label.config(text=f'Shortened URL: {short_url}')
    pyperclip.copy(short_url)

win = Tk()

def setup():
    win.geometry('350x200')
    win.title('URL Shortener')
    win['bg'] = 'white'
    win.resizable(False, False)
    win.attributes("-topmost", True)

entry = Entry(win, width=30, font=('Time New Roman', 10))
entry.place(x=50, y=20)

but = Button(win, text='Shorten', width=10, font=('Time New Roman', 10), command=short_link)
but.place(x=50, y=150)

short_url_label = Label(win, text='Shortened URL: ', font=('Arial', 10))
short_url_label.place(x=20, y=80)

copy_button = Button(win, text='Copy', width=10, font=('Time New Roman', 10), command=lambda: pyperclip.copy(short_url_label.cget("text").split(': ')[1]))
copy_button.place(x=170, y=150)

setup()
win.mainloop()
