import random
import tkinter as tk

def bt_choose_click():
    a = 0.5
    p = random.random()
    if p > a:
        txt_answer.config(text="Да")
    else:
        txt_answer.config(text="Нет")
root = tk.Tk()

txt_answer = tk.Label(root, text="Пойти сегодня в университет?")
txt_answer.pack()

bt_choose = tk.Button(root, text="Выбрать", command=bt_choose_click)
bt_choose.pack()

txt_answer = tk.Label(root, text="")
txt_answer.pack()

root.mainloop()
