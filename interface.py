import tkinter as tk
import poker

win = tk.Tk()  # создание окна
win.title('Lesson')  # название
h = 1000
w = 600
x = 500
y = 100

manager = poker.Manager()

combs_buts1 = []
combs_buts2 = []

for j in range(12):
    combs_buts1.append(tk.Button(win, text='combination 1'))
    combs_buts1[-1].grid(row=j, column=6)

for j in range(12):
    combs_buts2.append(tk.Button(win, text='combination 2'))
    combs_buts2[-1].grid(row=j, column=7)


def button_1_func():
    numbers = manager.throw()
    label_1.config(text=str(numbers[0]))
    label_2.config(text=str(numbers[1]))
    label_3.config(text=str(numbers[2]))
    label_4.config(text=str(numbers[3]))
    label_5.config(text=str(numbers[4]))
    combs = manager.get_combinations(numbers)
    for but, c in zip(combs_buts1, combs):
        but.config(text=f'{c}: {str(combs[c])}')


def button_2_func():
    numbers = manager.throw()
    label_12.config(text=str(numbers[0]))
    label_22.config(text=str(numbers[1]))
    label_32.config(text=str(numbers[2]))
    label_42.config(text=str(numbers[3]))
    label_52.config(text=str(numbers[4]))
    combs = manager.get_combinations(numbers)
    for but, c in zip(combs_buts2, combs):
        but.config(text=f'{c}: {str(combs[c])}')


def change_1():
    number = manager.re_throw(1)
    label_1.config(text=str(number[0]))


def change_2():
    number = manager.re_throw(1)
    label_2.config(text=str(number[0]))


def change_3():
    number = manager.re_throw(1)
    label_3.config(text=str(number[0]))


def change_4():
    number = manager.re_throw(1)
    label_4.config(text=str(number[0]))


def change_5():
    number = manager.re_throw(1)
    label_5.config(text=str(number[0]))


def change_12():
    number = manager.re_throw(1)
    label_12.config(text=str(number[0]))


def change_22():
    number = manager.re_throw(1)
    label_22.config(text=str(number[0]))


def change_32():
    number = manager.re_throw(1)
    label_32.config(text=str(number[0]))


def change_42():
    number = manager.re_throw(1)
    label_42.config(text=str(number[0]))


def change_52():
    number = manager.re_throw(1)
    label_52.config(text=str(number[0]))


def choose():
    pass


button_combination_1 = tk.Button(win,
                                 command=choose)
button_combination_2 = tk.Button(win,
                                 command=choose)
button_combination_3 = tk.Button(win,
                                 command=choose)

label_1 = tk.Button(win,
                    bg='#ede1ed',
                    fg='white',
                    font=('Arial', 20, 'bold'),
                    padx=20,
                    pady=20,
                    relief=tk.RAISED,
                    command=change_1)
label_2 = tk.Button(win,
                    bg='#ede1ed',
                    fg='white',
                    font=('Arial', 20, 'bold'),
                    padx=20,
                    pady=20,
                    relief=tk.RAISED,
                    command=change_2)
label_3 = tk.Button(win,
                    bg='#ede1ed',
                    fg='white',
                    font=('Arial', 20, 'bold'),
                    padx=20,
                    pady=20,
                    relief=tk.RAISED,
                    command=change_3)
label_4 = tk.Button(win,
                    bg='#ede1ed',
                    fg='white',
                    font=('Arial', 20, 'bold'),
                    padx=20,
                    pady=20,
                    relief=tk.RAISED,
                    command=change_4)
label_5 = tk.Button(win,
                    bg='#ede1ed',
                    fg='white',
                    font=('Arial', 20, 'bold'),
                    padx=20,
                    pady=20,
                    relief=tk.RAISED,
                    command=change_5)

label_12 = tk.Button(win,
                     bg='#ede1ed',
                     fg='white',
                     font=('Arial', 20, 'bold'),
                     padx=20,
                     pady=20,
                     relief=tk.RAISED,
                     command=change_12)
label_22 = tk.Button(win,
                     bg='#ede1ed',
                     fg='white',
                     font=('Arial', 20, 'bold'),
                     padx=20,
                     pady=20,
                     relief=tk.RAISED,
                     command=change_22)
label_32 = tk.Button(win,
                     bg='#ede1ed',
                     fg='white',
                     font=('Arial', 20, 'bold'),
                     padx=20,
                     pady=20,
                     relief=tk.RAISED,
                     command=change_32)
label_42 = tk.Button(win,
                     bg='#ede1ed',
                     fg='white',
                     font=('Arial', 20, 'bold'),
                     padx=20,
                     pady=20,
                     relief=tk.RAISED,
                     command=change_42)
label_52 = tk.Button(win,
                     bg='#ede1ed',
                     fg='white',
                     font=('Arial', 20, 'bold'),
                     padx=20,
                     pady=20,
                     relief=tk.RAISED,
                     command=change_52)

button_1 = tk.Button(win,
                     text='Бросить кубики',
                     command=button_1_func)

button_1.grid(row=3, column=0)

button_1 = tk.Button(win,
                     text='Бросить кубики',
                     command=button_1_func)

button_1.grid(row=3, column=0)

button_2 = tk.Button(win,
                     text='Бросить кубики',
                     command=button_2_func)

button_2.grid(row=3, column=2, stick='e')


def start():
    label_1.grid(row=0, column=0, stick='w')
    label_2.grid(row=0, column=1, stick='w')
    label_3.grid(row=1, column=0, stick='w')
    label_4.grid(row=1, column=1, stick='w')
    label_5.grid(row=2, column=0, stick='w')

    label_12.grid(row=0, column=2, stick='e')
    label_22.grid(row=0, column=3, stick='e')
    label_32.grid(row=1, column=2, stick='e')
    label_42.grid(row=1, column=3, stick='e')
    label_52.grid(row=2, column=3, stick='e')

    win.geometry(f'{h}x{w}+{x}+{y}')  # размер окна
    win.resizable(False, False)  # возможность изменять режим окна в реальном времени
    win.mainloop()  # запуск окна
