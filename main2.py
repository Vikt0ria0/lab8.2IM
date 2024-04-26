import random
import tkinter as tk


def button2_click():
    summ = 0
    for i in range(8):
        summ += prob[i]
        a = random.random()
        if summ > a :
            label2.config(text="Ответ:")
            label3.config(text=pred[i])
            break

    if textBox1.get() == "":
        label2.config(text="Введите вопрос")
        label3.config(text=" ")



prob = [0.125]*8
pred = ['Да', 'Нет', 'Возможно', 'Маловероятно', 'Высоковероятно', 'Может быть', 'Не может быть', 'Вероятно']
root = tk.Tk()

textBox1 = tk.Entry(root)
textBox1.pack()

button2 = tk.Button(root, text="Спросить", command=button2_click)
button2.pack()

label2 = tk.Label(root, text="")
label2.pack()

label3 = tk.Label(root, text="")
label3.pack()

root.mainloop()
