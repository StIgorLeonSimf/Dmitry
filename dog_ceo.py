from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
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


# def forward():
#     img = load_image(url)
#     if img:
#         label.config(image=img)
#         label.image = img
def get_dog_image():
    try:
        resp = requests.get('https://dog.ceo/api/breeds/image/random')
        resp.raise_for_status()
        data = resp.json()
        return data['message']
    except Exception as err:
        messagebox.showerror('Oшибка', 'Нет ответа API')
        return None


def show_image():
    global img_s
    image_url = get_dog_image()
    try:
        resp = requests.get(image_url, stream=True)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        img_s.thumbnail((600, 480), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img_s)
        label.config(image=img)
        label.image = img
    except Exception as err:
        messagebox.showerror('Ошибка', 'Ошибка загрузки файла')
        return None


img_s = None
root = Tk()
root.title("Kittens")
root.geometry('650x600')

frame1 = Frame(root)
frame1.pack(pady=10)
frame2 = Frame(root)
frame2.pack()


forw = Button(frame1)
forw.config(width=10, text='Следующая', command=show_image)
forw.grid(row=1, column=0)

save = Button(frame1)
save.config(width=10, text='Сохранить', command=save_picture)
save.grid(row=1, column=1)

label = Label(frame2)
label.pack()
show_image()


root.mainloop()
