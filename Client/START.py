import sys
import Tkinter

import threading
import Queue

sys.modules['tkinter'] = Tkinter
import os
import os.path
from Tkinter import *
import ttk
import tkMessageBox
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import time
from tkFileDialog import askopenfilename

import upload_video_to_server

if hasattr(sys, 'frozen'):
  # retrieve path from sys.executable
  rootdir = os.path.abspath(os.path.dirname(sys.executable))
else:
  # assign a value from __file__
  rootdir = os.path.abspath(os.path.dirname(__file__))

class NewRoot(Tk):    
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class MyMain(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.overrideredirect(1)
        # always on top -----> self.attributes('-topmost', 1)
        self.geometry('+100+100')
        #self.bind('<ButtonRelease-3>', self.on_close)  #right-click to get out

    def on_close(self, event):
        self.master.destroy()

def beenClicked():
    global app
    a = tkMessageBox.showinfo("GROUPYT Uploader by Amar Kalabic", "Thanks for using GROUPYT Uploader by Amar Kalabic-")
    time.sleep(3)
    app.destroy()
    root.destroy()
    return

root = NewRoot()
root.lower()
root.iconify()
root.title('GROUPYT Uploader by Amar Kalabic')
app = MyMain(root)
app.resizable(0,0)
root.wm_iconbitmap('%s/img/logo.ico'%rootdir)

def move_window(event):
    app.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def clickedX():
    app.destroy()
    root.destroy()
    sys.exit()

app.overrideredirect(True) # turns off title bar, geometry

app.geometry('850x455+200+200') # set new geometry

# make a frame for the title bar
title_bar = Frame(app, bg='white', relief='raised', bd=2)

# put a close button on the title bar
img_path = "%s/img/x_button.png"%rootdir
x_button_img = ImageTk.PhotoImage(Image.open(img_path))
close_button = Button(title_bar, image=x_button_img, command=clickedX, bd=0)
close_button.image = x_button_img

labelText = StringVar()
labelText.set("GROUPYT Uploader by Amar Kalabic")
label1 = Label(title_bar, textvariable=labelText, height=1, bg="white", fg="black")
label1.place(x=1, y=-3)

# a canvas for the main area of the window
img_fake = "%s/img/yt_logo.png"%rootdir
img = ImageTk.PhotoImage(Image.open(img_fake))
width1 = img.width()
height1 = img.height()
window = Canvas(app, bg='black', width=width1, height=height1)

window.create_image(width1/2.0, height1/2.0, image=img)
window.update()


# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)
app.title("GROUPYT Uploader by Amar Kalabic")

var1 = StringVar()
e1 = Entry(app, textvariable=var1, bg="black", fg="white", width=40)
e1.place(x=350, y=35)


var1.set("YouTube Video #1")

video_title = var1.get()

labelText = StringVar()
labelText.set("Video title")
label1 = Label(app, textvariable=labelText, height=2, bg="#DF1A2B", fg="white")
label1.place(x=250, y=25)

var2 = StringVar()
e2 = Entry(app, textvariable=var2, width=40)
e2.place(x=350, y=65)

video_desc = var2.get()

labelText1 = StringVar()
labelText1.set("Video description")
label2 = Label(app, textvariable=labelText1, height=2, bg="#DF1A2B", fg="white")
label2.place(x=250, y=55)

var3 = StringVar()
e3 = Entry(app, textvariable=var3, width=40)
e3.place(x=350, y=95)

var3.set("vlog, gaming, games, gameplay, dog, cat")

video_keywords = var3.get()

labelText2 = StringVar()
labelText2.set("Keywords")
label3 = Label(app, textvariable=labelText2, height=2, bg="#DF1A2B", fg="white")
label3.place(x=250, y=85)

def open_file():
    global content
    global file_path
    global filename

    filename = askopenfilename()
    file_path = os.path.dirname(filename)
    entry.delete(0, END)
    entry.insert(0, filename)
    return filename

global entry

entry = Entry(app, width=50, textvariable="Path do filea")
entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
entry.place(x=230, y=308)

Button(app, text="Browse", command=open_file).place(x=550, y=305)

class ThreadedTask(threading.Thread):
    print "threaded task start"
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "upload_video_to_server.py"))
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
           print filename
           button1['text'] = "Uploading video details..."
           upload_video_to_server.make_Info(filename=filename, title=video_title, description=video_desc, tags=video_keywords)
           button1['text'] = "Uploading video..."
           upload_video_to_server.upload_Start(filename=filename)

           print "ok"
           prog_bar.stop()
           button1['text'] = "Done! Start again?"
           button1['state'] = 'normal'
        else:
            tkMessageBox.showerror(
                "Error!",
                "Unable to find upload script!"
            )
            return

def tb_click():
    progress()
    prog_bar.start()
    button1['state'] = 'disabled'
    global queue
    queue = Queue.Queue()
    ThreadedTask(queue).start()
    app.after(100, process_queue)

def process_queue():
        try:
            msg = queue.get(0)
            # Show result of the task if needed
            print "MSG: ", msg

        except Queue.Empty:
            print "Queue is empty!"
            app.after(100, process_queue)

def chProgressBarValue(value):
    progress().prog_bar["value"] = value
    print "ProgBarValueChanged to: ", prog_bar["value"]

def chProgressBarMax(max):
    progress().prog_bar["maximum"] = max

def progress():
    global prog_bar
    print "prog bar is being made"
    prog_bar = ttk.Progressbar(
            app, orient="horizontal",
            length=200, mode="determinate",
            value=5,
            max=15
            )
    prog_bar.grid(row=1,column=0,pady=2,padx=2,sticky=E+W+N+S)
    prog_bar.place(x=333, y=395)

button1 = Button(app, text="START", width=20, command=tb_click)
button1.place(x=355, y=420)

app.mainloop()
