from tkinter import *
from time import strftime
from playsound import playsound
from time import *
from plyer import notification
import tkinter.messagebox

win = Tk()
win.title('Alarm')
win.geometry("900x500")
win.config(background="#2aa19d")

mes = StringVar()
message = StringVar()
hrs = StringVar()
mins = StringVar()


def error():
    tkinter.messagebox.showerror("Invalid Time",
                                 hrs.get() + " : " + mins.get() + " is not a Valid Time\nPlease enter a Valid Time")


def setalarm(present):
    if hrs.get() >= '24' or hrs.get() < '0' or mins.get() > '59' or mins.get() < '0':
        error()
    else:
        while True:
            pre = strftime('%H:%M')
            if pre == present:
                notification.notify(
                    title=mes.get(),
                    message=message.get(),
                    timeout=60
                )
                playsound('pppp.wav')
                win.destroy()


def correct():
    present = hrs.get() + ":" + mins.get()
    setalarm(present)


def clock():
    time = strftime('%H:%M:%S')
    label.config(text=time)
    label.after(1000, clock)


head = Label(win, text="Alarm Setter", font=('Comic Sans MS', 25, "bold"), background="#2aa19d", fg='White')
head.pack(anchor="center")

msg = Label(text="Description :", font=('Comic Sans MS', 17, "bold"), background="#2aa19d", fg='White')
msg.place(x=100, y=200)
entry = Entry(win, textvariable=message, font=15, bd='3')
entry.place(x=257, y=205)

des = Label(text="Message    :", font=('Comic Sans MS', 17, "bold"), background="#2aa19d", fg='White')
des.place(x=100, y=100)
entry1 = Entry(win, textvariable=mes, font=15, bd='3')
entry1.place(x=257, y=105)

time = Label(text="Set Time   : ", font=('Comic Sans MS', 17, "bold"), background="#2aa19d", fg='White')
time.place(x=100, y=295)
hour = Entry(win, textvariable=hrs, font=15, width=3, bd='3')
hour.place(x=300, y=300)
semi = Label(text=" : ", font=('Comic Sans MS', 20, "bold"), background="#2aa19d", fg='White')
semi.place(x=340, y=290)
minute = Entry(win, textvariable=mins, font=15, width=3, bd='3')
minute.place(x=378, y=300)

set = Button(text="Set Alarm", command=correct, font=('Comic Sans MS', 15), bg='#567', fg='White')
set.place(x=310, y=400)

f1 = Frame(win, background="#2aa19d", highlightbackground="#2aa19d")
f1.place(x=560, y=95, width=267, height=265)
canva = Canvas(f1, width=500, height=270, background="#2aa19d")
canva.pack()
img = PhotoImage(file="pic.png")
canva.create_image(130, 135, image=img)

label = Label(win, font=("ds-digital", 45), background="#2aa19d", foreground="white")
label.place(x=595, y=380)
clock()

win.mainloop()
