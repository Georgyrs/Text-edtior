from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def open_file():
    file_name = filedialog.askopenfilename(initialdir='/',
                                     title='Open file',
                                     filetypes=(('Text document', '*.txt'),
                                                ('All files', '*.*')))
    if file_name:
       f = open(file_name, 'r')
       text_open = f.read()
    #   if text_open != NONE:
       text.delete(1.0, END)
       text.insert(END, text_open)
def clear():
    message1 = messagebox.askokcancel("Внимание!", "Вы точно хотите очистить поле ввода?")
    if message1 == True:
        text.delete(1.0, END)
    else:
        messagebox.showinfo("Инфо", "Строка не очищена")


window = Tk()
window.geometry("400x300")
window.title("Текстовый редактор")
def show_info():
    regwin = Toplevel(window)
    regwin.title("Информация")
    regwin.geometry("400x300")
    labb = Label(regwin, text="Добро пожаловать в текстовый редактор!")
    labb.pack()

    close = Button(regwin, text="Закрыть", command=regwin.destroy)
    close.pack()

def save_as():
    che2ck = text.get(1.0, END)
    try:
        if len(che2ck) > 1:
            file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
            ("ALL files", "*.*")), defaultextension='')
            file = open(file_name, 'w')
            s =text.get(1.0, END)
            file.write(s)
            file.close()
        else:
            messagebox.showwarning("Внимание!", "Файл пустой")
    except:
        messagebox.showerror("Ошибка!", "Данные не сохранены")
def close():
    try:
      checking()
      window.destroy()
    except:
      messagebox.showerror("Ошибка!", "Данные не сохранены.")
def checking():
     check = text.get(1.0, END)
     if len(check) > 0:
        message=messagebox.askokcancel("Внимание!", "Вы хотите сохранить данные?")
        if message == True:
            file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                                ("ALL files", "*.*")), defaultextension='')
            file = open(file_name, 'w')
            s = text.get(1.0, END)
            file.write(s)
            file.close()
def create_new():
    check3 = text.get(1.0, END)
    if len(check3) > 0:
        msg = messagebox.askokcancel("Внимание!", "Вы хотите сохранить предыдущий файл?")
        if msg == True:
            file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                                ("ALL files", "*.*")), defaultextension='')
            file = open(file_name, 'w')
            s = text.get(1.0, END)
            file.write(s)
            file.close()
        else:
            text.delete(1.0, END)
menubar = Menu(window)

window.config(menu=menubar)

save = Menu(menubar)
save.add_command(label="Открыть", command=open_file)
save.add_command(label="Создать новый", command=create_new)
save.add_command(label="Сохранить как", command=save_as)
save.add_command(label="Закрыть", command=close)
menubar.add_cascade(label="Файл", menu=save)

cl = Menu(menubar)
cl.add_command(label="Очистить", command=clear)
cl.add_command(label="Инфо", command=show_info)
menubar.add_cascade(label="Другое", menu=cl)


text = Text(window)
text.pack(expand=YES, fill=BOTH)
window.mainloop()