from datetime import datetime
from tkinter import *

def time():
    dt = datetime.now()
    timeframe = dt.strftime("%H:%M:%S %p")
    my_label.config(text=timeframe)
    my_label.after(1000, time)

root = Tk()
root.title("Clock App")

my_label = Label(root, fg="blue", bg="yellow", font=("ds-digital", 100, "bold"))
my_label.pack()

time()
root.mainloop()