from tkinter import *
from tkinter import ttk
import tkinter as tk
import psutil

import random


def open_texteditor():
    text_window = Toplevel()
    text_window.title('Text Editor')
    text = Text(text_window, width=200, height=100)
    text.pack()
def open_dice():
    text_window = Toplevel()
    text_window.title('Dice')
    ttk.Label(text_window, text='Dice Roll...', font=fontie2).grid(column=0, row=0)
    ttk.Label(text_window, text=random.randint(1,6), font=fontie2).grid(column=0, row=5)

def open_cam():
    import tkinter as tk
    from PIL import Image, ImageTk
    import cv2

    class CameraApp:
        def __init__(self, root):
            self.root = root
            self.root.title('ulOS Camera')

            self.label = tk.Label(root)
            self.label.pack()

            self.cap = cv2.VideoCapture(0)
            self.show_camera()

        def show_camera(self):
            ret, frame = self.cap.read()
            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame)
                img_tk = ImageTk.PhotoImage(image=img)
                self.label.img = img_tk
                self.label.configure(image=img_tk)

            self.root.after(10, self.show_camera)

    if __name__ == '__main__':
        root = Toplevel()
        app = CameraApp(root)
        root.mainloop()

def open_camt():
    import tkinter as tk
    from PIL import Image, ImageTk
    import cv2

    class CameraApp:
        def __init__(self, root):
            self.root = root
            self.root.title('ulOS Camera')

            self.label = tk.Label(root)
            self.label.pack()

            self.cap = cv2.VideoCapture(0)
            self.show_camera()

        def show_camera(self):
            ret, frame = self.cap.read()
            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                thermal = cv2.applyColorMap(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_JET)
                img = Image.fromarray(thermal)
                img_tk = ImageTk.PhotoImage(image=img)
                self.label.img = img_tk
                self.label.configure(image=img_tk)

            self.root.after(10, self.show_camera)

    if __name__ == '__main__':
        root = Toplevel()
        app = CameraApp(root)
        root.mainloop()

def open_cpuM():

    def update_cpu_usage():
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_label.config(text=f'CPU usage: {cpu_usage}%')
        root.after(1000, update_cpu_usage)

    root = Toplevel()
    root.title('CPU MONITOR')

    cpu_label = tk.Label(root, text='CPU usage: 0%', font=('Helvetica', 14))
    cpu_label.pack(pady=20)

    update_cpu_usage()

    root.mainloop()



root1 = Tk()
root1.title('ulOS Launcher')
frm = ttk.Frame(root1, padding=10)
frm.pack()
fontie = ('Times', 20)
fontie2 = ('Times', 15)


frm.grid()
root1.config(cursor='star')

ttk.Label(frm, text='Welcome to the ulOS application launcher', font=fontie).grid(column=200, row=0)
ttk.Label(frm, text='Existing Applications', font=fontie2).grid(column=200, row=5)

te_image = PhotoImage(file='a.png')
te_button = tk.Button(frm, text='Text Editor', command=open_texteditor, image=te_image)
te_button.grid(column=0, row=20)

dc_image = PhotoImage(file='b.png')
dc_button = tk.Button(frm, text='Text Editor', command=open_dice, image=dc_image)
dc_button.grid(column=50, row=20)

cm_image = PhotoImage(file='c.png')
cm_button = tk.Button(frm, text='Text Editor', command=open_cam, image=cm_image)
cm_button.grid(column=100, row=20)

cmt_image = PhotoImage(file='d.png')
cmt_button = tk.Button(frm, text='Text Editor', command=open_camt, image=cmt_image)
cmt_button.grid(column=150, row=20)

cpu_image = PhotoImage(file='f.png')
cpu_button = tk.Button(frm, text='Text Editor', command=open_cpuM, image=cpu_image)
cpu_button.grid(column=170, row=20)

root1.mainloop()