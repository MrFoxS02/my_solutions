from tkinter import messagebox as mb
from tkinter import *

TASK_LIST = {} # Хранение индексированной задачи
frames = {} # Хранение адреса text
TASKS = {} # Список задач
N = 1 # Индекс задачи

# Параметры окна
window = Tk()
window.title('ToDo')
window.geometry('510x470')
window.configure(bg='green')

# Добавление задачи
def add_task():
    global N, TASK_LIST

    var = IntVar()
    var.set(N)
    # Удаление задачи
    def pop_item():
        global N, TASK_LIST
        TASK_LIST[var.get()].pack_forget()
        TASK_LIST.pop(var.get())
        main()

    # Сохранение текстовой задачи
    TASKS[N] = frames[0].get(1.0, END)
    frames[0].delete(1.0, END)
    if len(TASK_LIST) < 9:
        f = Frame(bg='yellow')
        text = Text(f, width=45, height=3, bg="white", fg='black')
        text.grid(column=0, row = 0)
        frames[N] = text

        c1 = Checkbutton(f,text = 'Снять задачу', onvalue=N, offvalue=0,
                 command=pop_item).grid(column=1, row = 0)

        TASK_LIST[N] = f

        N += 1
        main()
    else:
        mb.showinfo('', 'Превышен лимит задач')

f = Frame(bg='black')
text = Text(f, width=45, height=3, bg="white",
            fg='black')
text.grid(column=0, row = 0)
button = Button(f, text="Добавить задачу", command=add_task, bg = 'orange',\
                width=20, height=3).grid(column=1, row = 0)
TASK_LIST[0] = f
f.pack(fill=X)
frames[0] = text

#main
def main():
    window.quit()
    for i in TASK_LIST.keys():
        TASK_LIST[i].pack(fill=X)
        frames[i].delete(1.0, END) # Удаление дубликатов
        if i > 0:
            frames[i].insert(1.0, TASKS[i])

    window.mainloop()

main()