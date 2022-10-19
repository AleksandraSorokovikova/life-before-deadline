import tkinter as tk


win = tk.Tk()  # создание окна
win.title('Lesson')  # название
h = 500
w = 600
x = 500
y = 100

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

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=0)
label_4.grid(row=1, column=1)
label_5.grid(row=2, column=0)


#
win.geometry(f'{h}x{w}+{x}+{y}')  # размер окна
win.resizable(False, False)  # возможность изменять режим окна в реальном времени


win.mainloop()  # запуск окна