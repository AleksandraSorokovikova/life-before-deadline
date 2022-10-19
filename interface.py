import tkinter as tk

import random


win = tk.Tk()  # создание окна
win.title('Lesson')  # название
h = 500
w = 600
x = 500
y = 100

def button_1_func():
    numbers = [1, 2, 3, 4, 5, 6]
    random.shuffle(numbers)
    label_1.config(text=str(numbers[0]))
    label_2.config(text=str(numbers[1]))
    label_3.config(text=str(numbers[2]))
    label_4.config(text=str(numbers[3]))
    label_5.config(text=str(numbers[4]))
    label_6.config(text=str(numbers[5]))




label_1 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_2 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_3 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_4 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_5 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_6 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=0)
label_4.grid(row=1, column=1)
label_5.grid(row=2, column=0)

button_1 = tk.Button(win,
                     text='Бросить кубики',
                     command=button_1_func)

button_1.grid(row=3, column=0)


#
win.geometry(f'{h}x{w}+{x}+{y}')  # размер окна
win.resizable(False, False)  # возможность изменять режим окна в реальном времени


win.mainloop()  # запуск окна