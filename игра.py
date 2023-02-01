from tkinter import *
import random
score, max_score = 0, 5
size_x, size_y = 500, 500 
def put():
    global b
    b=Button(root, text='Нажми', activebackground='red', command=click)
    b.place(x=random.randint(0, size_x-10), y=random.randint(2, size_y-10))
def click():
    global score
    b.destroy()
    if score < max_score-1:
        score+=1
        put()
    else:
        Label(root, text='Поздравляем\n Вы виграли', borderwidth=5, relief='solid').place(relx=0.5, rely=0.5,anchor=CENTER)
root = Tk()
root.title('Игра')
root.geometry(f'{size_x}x{size_y}')
root.resizable(False, False)
put()
root.mainloop()