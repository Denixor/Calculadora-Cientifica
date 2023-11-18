import tkinter as tk
from libs.funcs import *
class App(Funcs):
    def __init__(self):
        self.root = tk.Tk()
        self.viewer_values = ''
        self.cfg_root()
        self.frames()
        self.upper_frame_widgets()
        self.lower_frame_widgets()
        self.root.mainloop()
    def cfg_root(self):
        self.root.configure(bg='Black')
    def frames(self):
        self.upper_frame = tk.Frame(self.root, width=300, height=100)
        self.lower_frame = tk.Frame(self.root, width=300, height=200)
        self.upper_frame.pack()
        self.lower_frame.pack()
    def upper_frame_widgets(self):
        self.viewer_text = tk.StringVar(self.upper_frame, self.viewer_values)
        self.viewer = tk.Label(self.upper_frame, textvariable=self.viewer_text, font=('Times', 16))
        self.viewer.place(relx=0.5, rely=0.5, anchor='center')
    def lower_frame_widgets(self):
        font_bt=('Times', 12)
        number_1 = tk.Button(self.lower_frame, text='1',font=font_bt, command=lambda:Funcs.add(self, 1)).grid(row=0, column=0)
        number_2 = tk.Button(self.lower_frame, text='2',font=font_bt, command=lambda:Funcs.add(self, 2)).grid(row=0, column=1)
        number_3 = tk.Button(self.lower_frame, text='3',font=font_bt, command=lambda:Funcs.add(self, 3)).grid(row=0, column=2)
        number_4 = tk.Button(self.lower_frame, text='4',font=font_bt, command=lambda:Funcs.add(self, 4)).grid(row=1, column=0)
        number_5 = tk.Button(self.lower_frame, text='5',font=font_bt, command=lambda:Funcs.add(self, 5)).grid(row=1, column=1)
        number_6 = tk.Button(self.lower_frame, text='6',font=font_bt, command=lambda:Funcs.add(self, 6)).grid(row=1, column=2)
        number_7 = tk.Button(self.lower_frame, text='7',font=font_bt, command=lambda:Funcs.add(self, 7)).grid(row=2, column=0)
        number_8 = tk.Button(self.lower_frame, text='8',font=font_bt, command=lambda:Funcs.add(self, 8)).grid(row=2, column=1)
        number_9 = tk.Button(self.lower_frame, text='9',font=font_bt, command=lambda:Funcs.add(self, 9)).grid(row=2, column=2)
        number_0 = tk.Button(self.lower_frame, text='0',font=font_bt, command=lambda:Funcs.add(self, 0)).grid(row=3, column=1)
        plus = tk.Button(self.lower_frame, text='+',font=font_bt, command=lambda:Funcs.add(self, '+')).grid(row=0, column=3)
        minus = tk.Button(self.lower_frame, text='-',font=font_bt, command=lambda:Funcs.add(self, '-')).grid(row=1, column=3)
        div = tk.Button(self.lower_frame, text='/',font=font_bt, command=lambda:Funcs.add(self, '/')).grid(row=2, column=3)
        mult = tk.Button(self.lower_frame, text='*',font=font_bt, command=lambda:Funcs.add(self, '*')).grid(row=3, column=3)
        clear = tk.Button(self.lower_frame, text='C',font=font_bt, command=lambda:Funcs.clear(self)).grid(row=3, column=0)
        result = tk.Button(self.lower_frame, text='=',font=font_bt, command=lambda:Funcs.equals(self)).grid(row=3, column=2)

App()