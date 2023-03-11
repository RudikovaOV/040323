from tkinter import *
from tkmacosx import Button

arg1 = 0
arg2 = 0
znak = ''

def onclick_plus():
    global arg1
    global znak
    arg1 = int(rezultat['text'])
    znak = '+'
    rezultat.configure(text='')

def onclick_minus():
    global arg1
    global znak
    arg1 = int(rezultat['text'])
    znak = '-'
    rezultat.configure(text='')

def onclick_umnozhit():
    global arg1
    global znak
    arg1 = int(rezultat['text'])
    znak = '*'
    rezultat.configure(text='')

def onclick_delenie():
    global arg1
    global znak
    arg1 = int(rezultat['text'])
    znak = '/'
    rezultat.configure(text='')

def onclick_znak():
    if int(rezultat['text']) < 0:
        rezultat.configure(text=rezultat['text'])



def onclick_ravno():
    global arg2
    global znak
    arg2 = int(rezultat['text'])
    if znak == "+":
        finrezult = arg1 + arg2
    elif znak == "-":
        finrezult = arg1 - arg2
    elif znak == "*":
        finrezult = arg1 * arg2
    elif znak == "/":
        finrezult = arg1/arg2

    rezultat.configure(text=str(finrezult))

def onclick_1():
    rezultat.configure(text=rezultat['text']+'1')
def onclick_2():
    rezultat.configure(text=rezultat['text']+'2')
def onclick_3():
    rezultat.configure(text=rezultat['text']+'3')
def onclick_4():
    rezultat.configure(text=rezultat['text']+'4')
def onclick_5():
    rezultat.configure(text=rezultat['text']+'5')
def onclick_6():
    rezultat.configure(text=rezultat['text']+'6')
def onclick_7():
    rezultat.configure(text=rezultat['text']+'7')
def onclick_8():
    rezultat.configure(text=rezultat['text']+'8')
def onclick_9():
    rezultat.configure(text=rezultat['text']+'9')
def onclick_0():
    rezultat.configure(text=rezultat['text']+'0')
def onclick_clear():
    rezultat.configure(text=rezultat['text'][:-1])
def onclick_clearall():
    rezultat.configure(text='')


def onclick():
    pass

main_window = Tk()
main_window.title("Калькулятор")
main_window.geometry("600x600")
#элементы интерфейса: кнопки, поле ввода, надпись, выпадающий список, checkbox
#radiobutton, всплывающие сообщения

rezultat = Label(main_window)
rezultat.grid(column=0, row=0)
btn_1 = Button(main_window, text="1", command=onclick_1)
btn_1.grid(column=0, row=1)
btn_2 = Button(main_window, text="2", command=onclick_2)
btn_2.grid(column=2, row=1)
btn_3 = Button(main_window, text="3", command=onclick_3)
btn_3.grid(column=3, row=1)

btn_4 = Button(main_window, text="4", command=onclick_4)
btn_4.grid(column=0, row=2)
btn_5 = Button(main_window, text="5", command=onclick_5)
btn_5.grid(column=2, row=2)
btn_6 = Button(main_window, text="6", command=onclick_6)
btn_6.grid(column=3, row=2)

btn_7 = Button(main_window, text="7", command=onclick_7)
btn_7.grid(column=0, row=3)
btn_8 = Button(main_window, text="8", command=onclick_8)
btn_8.grid(column=2, row=3)
btn_9 = Button(main_window, text="9", command=onclick_9)
btn_9.grid(column=3, row=3)

btn_znak = Button(main_window, text="+/-", command=onclick_znak)
btn_znak.grid(column=0, row=4)
btn_0 = Button(main_window, text="0", command=onclick_0)
btn_0.grid(column=2, row=4)
btn_point = Button(main_window, text=".", command=onclick)
btn_point.grid(column=3, row=4)

btn_plus = Button(main_window, text="+", command=onclick_plus)
btn_plus.grid(column=4, row=1)
btn_minus = Button(main_window, text="-", command=onclick_minus)
btn_minus.grid(column=4, row=2)
btn_umnozhit = Button(main_window, text="*", command=onclick_umnozhit)
btn_umnozhit.grid(column=4, row=3)
btn_delenie = Button(main_window, text="/", command=onclick_delenie)
btn_delenie.grid(column=4, row=4)
btn_ravno = Button(main_window, text="=", command=onclick_ravno)
btn_ravno.grid(column=5, row=3)
btn_clear = Button(main_window, text="clear", command=onclick_clear)
btn_clear.grid(column=5, row=1)
btn_clearall = Button(main_window, text="clearall", command=onclick_clearall)
btn_clearall.grid(column=5, row=2)

main_window.mainloop() #ставим в самый конец