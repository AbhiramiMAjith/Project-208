import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDR = '127.0.0.1'
PORT = 5550
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window,text="Select song", bg ='LightSkyBlue',font=("Calibri",8))
    selectLabel.place(x=2,y=1)

    listbox = Listbox(window,height=10,width=39,activestyle='dotbox',bg='LightSkyBlue',borderwidth=2,font=("Calibri",10))
    listbox.place(x=10,y=10)

    scroll_bar_1 = Scrollbar(listbox)
    scroll_bar_1.place(relheight=1,relx=1)
    scroll_bar_1.config(command=listbox.yview)

    playbutton = Button(window,text='Play',width=10,bd=1,bg ='SkyBlue',font=("Calibri",10))
    playbutton.place(x=30,y=200)
    
    stop = Button(window,text='Stop',width=10,bd=1,bg ='SkyBlue',font=("Calibri",10))
    stop.place(x=200,y=200)

    upload = Button(window,text='Uplaod',width=10,bd=1,bg ='SkyBlue',font=("Calibri",10))
    upload.place(x=30,y=250)

    download = Button(window,text='Download',width=10,bd=1,bg ='SkyBlue',font=("Calibri",10))
    download.place(x=200,y=250)

    infolabel = Label(window,text='',fg="blue",font=("Calibri",0))
    infolabel.place(x=4,y=200)

    window.mainloop()

def setup():
    global IP_ADDR
    global PORT
    global SERVER

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDR,PORT))

    musicWindow()

setup()