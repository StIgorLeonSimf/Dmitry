import os
from datetime import datetime as dt
from tkinter import *
from tkinter import filedialog as fd

# os.mkdir('new')
# print(os.path.abspath(''))
os.makedirs(r'D:\UNITS\Python\Units\DMITRY_BUGR\new\new2', exist_ok=True)
# with open(r'D:\UNITS\Python\Units\DMITRY_BUGR\new\new2\new2.py', 'a') as f:
#     f.write('#1234')
ps = os.path.join('new', 'new1')
path = os.path.abspath(ps)



# print(path)
# tm = os.path.getmtime(r'D:\UNITS\Python\Units\DMITRY_BUGR\new\new2\new2.py')
# print(dt.fromtimestamp(tm).replace(microsecond=0))
# print(os.path.exists(r'D:\UNITS\Python\Units\DMITRY_BUGR\new\new2\new2.py'))
# print(os.path.basename(r'D:\UNITS\Python\Units\DMITRY_BUGR\new\new2\new10.py'))


def size_count(target):
    size = 0
    count_folders = 0
    count_files = 0
    ps = os.path.join(target)
    # print(ps)
    p = os.path.abspath(ps)
    # print(p)
    for i in os.listdir(p):
        ps = os.path.join(p, i)
        if os.path.isfile(ps):
            count_files += 1
            size += os.path.getsize(ps)
        else:
            count_folders += 1
            s, cf, cfl = size_count(ps)
            size += s
            count_folders += cf
            count_files += cfl

    return size, count_folders, count_files

# print(size_count('new'))
# size_count(r'D:\UNITS\Python\Units\DMITRY_BUGR\new')

window = Tk()
window.withdraw()
dir_ = fd.askdirectory()
# print(dir_)
# print(size_count(dir_))
if dir_:
    pass

