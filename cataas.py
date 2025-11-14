from tkinter import *
from tkinter import filedialog as fd
import requests
from PIL import Image, ImageTk
from io import BytesIO


def save_picture():
    # global img_s
    if img_s is None:
        print('Изображение не получено')
        return None
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        initialfile='picture.png',
        filetypes=[('PNG file', '*.png'),
                   ('ALL files', '*.*')]
    )
    if fp:
        img_s.save(fp)
        print(f'Запись осуществлена: {fp}')


def forward():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def load_image(url):
    global img_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        img_s.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img_s)
    except Exception as err:
        print('Ошибка: ')
        return None


img_s = None
root = Tk()
root.title("Kittens")
root.geometry('650x600')

frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack(pady=10)

prompt = Entry(frame1, width=40)
prompt.grid(row=0, columnspan=2, pady=10)
forw = Button(frame1)
forw.config(width=10, text='Следующая', command=forward)
forw.grid(row=1, column=0)

save = Button(frame1)
save.config(width=10, text='Сохранить', command=save_picture)
save.grid(row=1, column=1)

label = Label(frame2)
label.pack()
url = 'https://cataas.com/cat'
img = load_image(url)
forward()

root.mainloop()
