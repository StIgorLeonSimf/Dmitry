from tkinter import *


# def handler(nm):
#     btns[nm - 1].config(bg='lightgray')
#
#
# root = Tk()
# root.geometry('500x400')
#
# frame1 = Frame(root)
# frame1.pack(pady=10)
# frame2 = Frame(root)
# frame2.pack()
#
# canvas = Canvas(frame1, width=400, height=50)
# canvas.pack()
#
# canvas.create_line(60, 40, 140, 40, width=5, fill='blue')
# canvas.create_text(100, 30, text='500')
# canvas.create_line(160, 40, 240, 40, width=5, fill='light green')
# canvas.create_text(200, 30, text='450')
# canvas.create_line(260, 40, 340, 40, width=5, fill='yellow')
# canvas.create_text(300, 30, text='400')
# color = 'light green'
#
# btns = []
# row = 10
# column = 4
# for i in range(row):
#     for j in range(column):
#         num = i * column + j + 1
#         btn = Button(frame2)
#         btn.config(text=num, width=2, justify='center',
#                    bg=color, command=lambda x=num: handler(x))
#         btn.grid(row=i, column=j)
#         btns.append(btn)
# # btn1 = Button(frame2)
# # btn1.config(text=2, width=2, justify='center', bg=color)
# # btn1.grid(row=0, column=1)
#
# root.mainloop()


def handler(nm):
    btns[nm - 1].config(bg='lightgray')


root = Tk()
root.geometry('570x400')

frame1 = Frame(root)
frame1.pack(pady=10)
frame2 = Frame(root)
frame2.pack(side=LEFT, padx=5)

screen = Label(frame1, text='Экран')
screen.pack()
canvas = Canvas(frame1, width=400, height=50)
canvas.pack()
canvas.create_line(50, 10, 350, 10, width=8, fill='light blue' )
canvas.create_line(60, 40, 140, 40, width=5, fill='blue')
canvas.create_text(100, 30, text='500')
canvas.create_line(160, 40, 240, 40, width=5, fill='light green')
canvas.create_text(200, 30, text='450')
canvas.create_line(260, 40, 340, 40, width=5, fill='yellow')
canvas.create_text(300, 30, text='400')
color = 'light green'

btns = []
row = 10
column = 20
for i in range(row):
    lab = Label(frame2, text=f'Ряд №{i + 1}')
    lab.grid(row=i, column=0)
    for j in range(column):
        num = i * column + j + 1
        btn = Button(frame2)
        btn.config(text=num, width=2, justify='center',
                   bg=color, command=lambda x=num: handler(x))
        btn.grid(row=i, column=j+1)
        btns.append(btn)


root.mainloop()