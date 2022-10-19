import tkinter as tk
import poker


win = tk.Tk()  # создание окна
win.title('Lesson')  # название
h = 1000
w = 600
x = 500
y = 100

manager = poker.Manager()

def button_1_func():
    numbers = manager.throw()
    label_1.config(text=str(numbers[0]))
    label_2.config(text=str(numbers[1]))
    label_3.config(text=str(numbers[2]))
    label_4.config(text=str(numbers[3]))
    label_5.config(text=str(numbers[4]))
    label_6.config(text=str(numbers[5]))

def button_2_func():
    numbers = manager.throw()
    label_12.config(text=str(numbers[0]))
    label_22.config(text=str(numbers[1]))
    label_32.config(text=str(numbers[2]))
    label_42.config(text=str(numbers[3]))
    label_52.config(text=str(numbers[4]))
    label_62.config(text=str(numbers[5]))





label_1 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED,
                   )
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


label_12 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_22 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_32 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_42 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_52 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)
label_62 = tk.Label(win,
                   bg='#ede1ed',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=20,
                   relief=tk.RAISED)


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