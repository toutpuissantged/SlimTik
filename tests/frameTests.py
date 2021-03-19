import tkinter as tk
from tkinter import *


class MainWin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.page_1 = Page1(self.parent)
        self.page_2 = Page2(self.parent)

        self.init_UI()

    def init_UI(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        self.parent.title('Frame Switching test app')
        file_menu = Menu(menubar)
        pages_menu = Menu(menubar)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Exit', command=self.on_exit)
        menubar.add_cascade(label='Pages', menu=pages_menu)
        pages_menu.add_command(label='Pages 1', command=self.page_1.show)
        pages_menu.add_command(label='Page 2', command=self.page_2.show)

    def on_exit(self):
        self.quit()


class Page1(LabelFrame):
    def __init__(self, parent):
        LabelFrame.__init__(self, parent)
        self.parent = parent
        self.config(text='This is page 1 label Frame')
        self.sample_text = Label(self, text='You are viewing Page 1')

    def show(self):
        self.pack(fill=BOTH, expand=1)
        self.sample_text.grid(in_=self)
        self.lift()

    def close(self):
        self.pack_forget()


class Page2(LabelFrame):
    def __init__(self, parent):
        LabelFrame.__init__(self, parent)
        self.parent = parent
        self.config(text='This is page 2 label Frame')
        self.sample_text = Label(self, text='You are viewing Page 2')

    def show(self):
        self.pack(fill=BOTH, expand=1)
        self.sample_text.grid(in_=self)
        self.lift()

    def close(self):
        self.pack_forget()


def main():
    root = tk.Tk()
    app = MainWin(root)
    root.mainloop()


if __name__ == '__main__':
    main()