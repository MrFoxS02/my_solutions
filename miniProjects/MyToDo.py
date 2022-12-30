from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import *

ACTIVE_FILE_NAME = 'tasks.txt'

window = Tk()
window.title('ToDo')
window.geometry('700x350')
window.configure(bg='green')
window.resizable(width=False, height=False)

mainmenu = Menu(window)
window.config(menu=mainmenu)

def add_data():
    box.insert(END, text.get(1.0, END))
    text.delete(1.0, END)

def remove_data():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)

def clear_data():
    box.delete(0, END)

def add_data_from_file():
    global ACTIVE_FILE_NAME
    save_data()
    clear_data()
    file_name = fd.askopenfilename()
    ACTIVE_FILE_NAME = file_name
    with open(ACTIVE_FILE_NAME, 'r', encoding='utf-8') as file:
        lst = file.readlines()
    for item in lst:
        box.insert(END, item)


def save_data():
    f = open(ACTIVE_FILE_NAME, 'w', encoding='utf-8')
    f.writelines("".join(box.get(0, END)))
    f.close()

def quit_program():
    save_data()
    window.quit()

#-----------------------------------------------------------------------------------------#
# Добавление виджетов
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=add_data_from_file)
filemenu.add_command(label="Сохранить...", command=save_data)
filemenu.add_command(label="Выход", command=quit_program)

mainmenu.add_cascade(label="Файл",
                     menu=filemenu)

box = Listbox(selectmode=EXTENDED, width=55, height=50)
box.pack(side=LEFT)
scroll = Scrollbar(command=box.yview)
scroll.pack(side=LEFT, fill=X)
box.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10, pady=10)
text = Text(f, width=45, height=10, bg="white",
            fg='black')
text.focus()
text.pack(fill=X)
Button(f, text="Добавить задачу", command=add_data, bg = 'orange').pack(fill=X)
Button(f, text="Удалить задачу", command=remove_data, bg = 'red').pack(fill=X)
Button(f, text="Удалить всё", command=clear_data, bg = 'pink').pack(fill=X)

window.mainloop()
