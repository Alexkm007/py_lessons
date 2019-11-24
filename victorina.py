# -*- coding: utf-8 -*- 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry('250x160')

def que_one():
    question = Label(root, text = "Висит груша нельзя скушать?")
    answer   = Entry()
    btn = Button(root,text = "Ответить",command = lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()
    
    def game1(que):
        if answer.get().lower() == "лампочка":
            que()
        else:    
           messagebox.showerror("Ошибка", "Попробуй еще раз")
            
            
def que_two():
    question2 = Label(root, text = "Зимой и летом одним цветом")
    answer2   = Entry()
    btn2 = Button(root,text = "Ответить",command = lambda: game2())
    question2.grid()
    answer2.grid()
    btn2.grid()
    
    def game2():
        if answer2.get().lower() == "елка":
            messagebox.showinfo("Победа", "Ты молодец")
        else:    
           messagebox.showerror("Ошибка", "Попробуй еще раз")
    
    
que_one()


root.mainloop()