import socket
import tkinter as tk
from PIL import Image, ImageTk

# server = socket.socket()
# server.bind(('127.0.0.1', 8888))
# server.listen(1)
# user, addr = server.accept()
#
# print("connect")
# user.send("connect".encode("utf-8"))

# while True:
#     data = user.recv(1024)
#     print(data.decode("utf-8"))
#     user.send(input().encode("utf-8"))


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

btn_img = Image.open("button.png")
btn_img = btn_img.resize((100, 100), Image.LANCZOS)

bg_img = Image.open("bg.png")
bg_img = ImageTk.PhotoImage(bg_img)
bg = tk.Label(win, image=bg_img)
bg.pack()

pressed_btn_img = Image.open("buttonpressed.png")
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
        # user.send(btn1_img_counter)
    elif btn1_img_counter == 1:
        btn1_img_counter -= 1
        btn.config(image=btn_img_list[btn1_img_counter])


def btn2_command(btn):
    global btn2_img_counter
    if btn2_img_counter == 0:
        btn2_img_counter += 1
        btn.config(image=btn_img_list[btn2_img_counter])
    elif btn2_img_counter == 1:
        btn2_img_counter -= 1
        btn.config(image=btn_img_list[btn2_img_counter])


def btn3_command(btn):
    global btn3_img_counter
    if btn3_img_counter == 0:
        btn3_img_counter += 1
        btn.config(image=btn_img_list[btn3_img_counter])
    elif btn3_img_counter == 1:
        btn3_img_counter -= 1
        btn.config(image=btn_img_list[btn3_img_counter])


# server = socket.socket()
# server.bind(('127.0.0.1', 8888))
# server.listen(1)
# user, addr = server.accept()

win.mainloop()





