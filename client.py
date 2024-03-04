import socket
import tkinter as tk
from PIL import Image, ImageTk

# client = socket.socket()
# client.connect(('127.0.0.1', 8888))
#
# while True:
#     data = client.recv(1024)
#     print(data.decode("utf-8"))
#     client.send(input().encode("utf-8"))

WEIGHT = 800
HEIGHT = 600

win = tk.Tk()
win.title('button')
logo = tk.PhotoImage(file='buttonimg.png')
win.iconphoto(False, logo)
win.config(bg='#afb3b6')
win.geometry(f'{WEIGHT}x{HEIGHT}+400+100')
win.resizable(False, False)

main_lon_wo_img = Image.open("lighton_winopen.png")
main_loff_wo_img = Image.open("lightoff_winopen.png")
main_lon_wc_img = Image.open("lighton_winclosed.png")
main_loff_wc_img = Image.open("lightoff_winclosed.png")

main_img_list = [
    ImageTk.PhotoImage(main_lon_wo_img),
    ImageTk.PhotoImage(main_loff_wo_img),
    ImageTk.PhotoImage(main_lon_wc_img),
    ImageTk.PhotoImage(main_loff_wc_img)
]

# main_img = Image.open("lighton_winopen.png")
# main_img = ImageTk.PhotoImage(main_img)
main = tk.Label(win, image=main_img_list[0])
main.pack()

# client = socket.socket()
# client.connect(('127.0.0.1', 8888))
# data = client.recv(1024)
# data = data
# main.config(image=main_img_list[data])

win.mainloop()