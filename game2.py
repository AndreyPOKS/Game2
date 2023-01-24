import tkinter as tk
import random
Computer = random.randrange(10)
def get_entry():
    value = number.get()
    global Computer
    if value:
        lbl = tk.Label(win,text="!Ответ!").grid(row=3, column=0)
        if int(value) != Computer:
            btk2 = tk.Button(win, text="Ваше число больше ?", command=add_Buttun2,).grid(row=4, column=0)
            btk3 = tk.Button(win, text="Ваше число меньше ?",command=add_Buttun3,).grid(row=5, column=0)
            btk4 = tk.Label(win, text=Computer).grid(row=2, column=0)
        else:
            btk1 = tk.Label(win, text="Отгадал", )
            btk1.grid(row=3, column=0)
    else:
        print("Error")
def add_Buttun2():
    global Computer
    global hell
    hell = Computer
    print(hell)
    Computer = random.randrange(hell, 10)
    btk1 = tk.Label(win, text=Computer, ).grid(row=2, column=0)
def add_Buttun3():
    global Computer
    global hell
    hell = Computer
    print(hell)
    Computer = random.randrange(0, hell)
    btk1 = tk.Label(win, text=Computer, ).grid(row=2, column=0)




win = tk.Tk()
win.config(bg="#de7aff")
win.title("Загадай число/POKS44b")
win.geometry("150x200+100+200")
win.resizable(False, False)
number = tk.Entry(win,)
btk1 = tk.Label(win, text=Computer, ).grid(row=2, column=0)
label1 = tk.Button(win, text="Играть", command = get_entry,).grid(row=1, column=0)
number.grid(row=0, column=0)
win.mainloop()