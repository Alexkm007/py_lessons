# -*- coding: utf-8 -*- 
from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Войти в систему")

def regestration():
    text = Label(text = "для входа в систему зарегистрируйтесь!!!")
    text_log  = Label(text = "Введите вашг логин")
    reg_login = Entry()
    text_pass = Label(text = "Введите вашг пароль")
    reg_pass1  = Entry()
    text_pass2 = Label(text = "Подтвердите пароль")
    reg_pass2  = Entry(show = "*")
    butt_reg   = Button(text = "Зарегистрироваться", command = lambda:save())
    text.pack()
    text_log.pack()
    reg_login.pack()
    text_pass.pack()
    reg_pass1.pack()
    text_pass2.pack()
    reg_pass2.pack()
    butt_reg.pack()
        
    def save():
        login_pass_save = {}
        login_pass_save[reg_login.get()] = reg_pass1.get()
        f = open("login.txt","wb")
        pickle.dump(login_pass_save,f)
        f.close()
        login()
        
def login():
    text_log     = Label(text = "Поздравлаем теперь вы можете войти в систему")
    text_en_log  = Label(text = "Введите ваш логин")
    en_login     = Entry()
    text_en_pass = Label(text = "Введите пароль")
    en_pass      = Entry(show = "*")
    button_enter = Button(text= "Войти", command =lambda:log_pass())
    text_log.pack()
    text_en_log.pack()
    en_login.pack()
    text_en_pass.pack()
    en_pass.pack()
    button_enter.pack()
    def log_pass():
         f = open("login.txt","rb")
         a = pickle.load(f)
         f.close()
         if en_login.get() in a:
             if en_pass.get() == a[en_login.get()]:
                messagebox.showinfo("Ок, коллега","Привет! У тебя 5 новых сообщений")
             else:
                messagebox.showerror("Ошибка", "что то пошло не так")
         else:                        
             messagebox.showerror("Ошибка", "Я вас без грима не узнаю")
         
#login()   
regestration()


root.mainloop()