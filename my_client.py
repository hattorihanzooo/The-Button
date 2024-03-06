import socket
import time
import tkinter as tk
from PIL import Image, ImageTk
import sys
from PySide6.QtWidgets import QApplication, QLabel


client = socket.socket()
client.connect(('localhost', 8888))

time.sleep(3)






WEIGHT = 800
HEIGHT = 600


win = tk.Tk()
win.title('button')
logo = tk.PhotoImage(file='buttonimg.png')
win.iconphoto(False, logo)
win.config(bg='#afb3b6')
win.geometry(f'{WEIGHT}x{HEIGHT}+400+100')
win.resizable(False, False)

fr = tk.Frame(win)
fr.pack(side="bottom")

btn_img = Image.open("img/buttons/button.png")
btn_img = btn_img.resize((100, 100), Image.LANCZOS)

bg_img = Image.open("bg.png")
bg_img = ImageTk.PhotoImage(bg_img)
bg = tk.Label(win, image=bg_img)
bg.pack()

pressed_btn_img = Image.open("img/buttons/buttonpressed.png")
pressed_btn_img = pressed_btn_img.resize((100, 100), Image.LANCZOS)

btn_img_list = [
    ImageTk.PhotoImage(btn_img),
    ImageTk.PhotoImage(pressed_btn_img)
]

btn1_img_counter = 0
btn2_img_counter = 0
btn3_img_counter = 0

btn1 = tk.Button(fr, image=btn_img_list[0], highlightthickness=0, bd=0, bg="#afb3b6", activebackground="#afb3b6")
btn2 = tk.Button(fr, image=btn_img_list[0], highlightthickness=0, bd=0, bg="#afb3b6", activebackground="#afb3b6")
btn3 = tk.Button(fr, image=btn_img_list[0], highlightthickness=0, bd=0, bg="#afb3b6", activebackground="#afb3b6")

btn1.config(command=lambda: btn1_command(btn1))
btn2.config(command=lambda: btn2_command(btn2))
btn3.config(command=lambda: btn3_command(btn3))

btn1.grid(row=0, column=0, ipadx=50, ipady=50)
btn2.grid(row=0, column=1, ipadx=50, ipady=50)
btn3.grid(row=0, column=2, ipadx=50, ipady=50)

# server = socket.socket()
# server.bind(('127.0.0.1', 8888))
# server.listen(1)
# user, addr = server.accept()

def btn1_command(btn):
    global btn1_img_counter
    if btn1_img_counter == 0:
        btn1_img_counter += 1
        btn.config(image=btn_img_list[btn1_img_counter])
        client.send('1'.encode('utf-8'))
    elif btn1_img_counter == 1:
        btn1_img_counter -= 1
        btn.config(image=btn_img_list[btn1_img_counter])
        client.send('1'.encode('utf-8'))


def btn2_command(btn):
    global btn2_img_counter
    if btn2_img_counter == 0:
        btn2_img_counter += 1
        btn.config(image=btn_img_list[btn2_img_counter])
        client.send('2'.encode('utf-8'))
    elif btn2_img_counter == 1:
        btn2_img_counter -= 1
        btn.config(image=btn_img_list[btn2_img_counter])
        client.send('2'.encode('utf-8'))


def btn3_command(btn):
    global btn3_img_counter
    if btn3_img_counter == 0:
        btn3_img_counter += 1
        btn.config(image=btn_img_list[btn3_img_counter])
        client.send('4'.encode('utf-8'))
    elif btn3_img_counter == 1:
        btn3_img_counter -= 1
        btn.config(image=btn_img_list[btn3_img_counter])
        client.send('4'.encode('utf-8'))


# server = socket.socket()
# server.bind(('127.0.0.1', 8888))
# server.listen(1)
# user, addr = server.accept()

win.mainloop()



#

