from tkinter import *
import tkinter.messagebox


root=Tk()
root.iconbitmap('C:\\Users\\LOHITH\\OneDrive\\Desktop\\tic\\tictactoe.ico')

root.title("TIC TAC TOE 😎")
root.resizable(width=False,height=False)

click=True

count=0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xphoto = PhotoImage(file='C:\\Users\\LOHITH\\OneDrive\\Desktop\\tic\\xnew.png')
ophoto = PhotoImage(file='C:\\Users\\LOHITH\\OneDrive\\Desktop\\tic\\onew.png')


def play():
    button1 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#668cff',textvariable=btn1,command=lambda:press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#668cff',textvariable=btn2,command=lambda:press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#668cff',textvariable=btn3,command=lambda:press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#809fff',textvariable=btn4,command=lambda:press(4,1,0))
    button4.grid(row=1,column=0)

    button5 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#809fff',textvariable=btn5,command=lambda:press(5,1,1))
    button5.grid(row=1,column=1)

    button6 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#809fff',textvariable=btn6,command=lambda:press(6,1,2))
    button6.grid(row=1,column=2)

    button7 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#99b3ff',textvariable=btn7,command=lambda:press(7,2,0))
    button7.grid(row=2,column=0)

    button8 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#99b3ff',textvariable=btn8,command=lambda:press(8,2,1))
    button8.grid(row=2,column=1)

    button9 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#99b3ff',textvariable=btn9,command=lambda:press(9,2,2))
    button9.grid(row=2,column=2)

def press(num,r,c):
   global count,click

   if click == True:
    lablephoto = Label(root,image=xphoto)
    lablephoto .grid(row=r,column=c)
    if num == 1:
        btn1.set('X')
    elif num == 2:
        btn2.set('X')
    elif num == 3:
        btn3.set('X')
    elif num == 4:
        btn4.set('X')
    elif num == 5:
        btn5.set('X')
    elif num == 6:
        btn6.set('X')
    elif num == 7:
        btn7.set('X')
    elif num == 8:
        btn8.set('X')
    else:
        btn9.set('X')
    
    count+=1

    click=False
    checkwin()
   else:
    lablephoto = Label(root,image=ophoto)
    lablephoto .grid(row=r,column=c)
    if num == 1:
        btn1.set('O')
    elif num == 2:
        btn2.set('O')
    elif num == 3:
        btn3.set('O')
    elif num == 4:
        btn4.set('O')
    elif num == 5:
        btn5.set('O')
    elif num == 6:
        btn6.set('O')
    elif num == 7:
        btn7.set('O')
    elif num == 8:
        btn8.set('O')
    else:
        btn9.set('O')
    
    count+=1
    click=True
    checkwin()

def checkwin():
    global count,click
    if(btn1.get()=='X' and btn2.get() == 'X' and btn3.get()== 'X'  or
      btn4.get()=='X' and btn5.get() == 'X' and btn6.get()== 'X'  or
      btn7.get()=='X' and btn8.get() == 'X' and btn9.get()== 'X'  or
      btn1.get()=='X' and btn4.get() == 'X' and btn7.get()== 'X'  or
      btn2.get()=='X' and btn5.get() == 'X' and btn8.get()== 'X'  or
      btn3.get()=='X' and btn6.get() == 'X' and btn9.get()== 'X'  or
      btn1.get()=='X' and btn5.get() == 'X' and btn9.get()== 'X'  or
      btn3.get()=='X' and btn5.get() == 'X' and btn7.get()== 'X'  ):
         
          tkinter.messagebox.showinfo("TIC TAC TOE",'PLAYER X WINS 😘')
          click = True
          count =0
          clear()
          play()

    elif (btn1.get()=='O' and btn2.get() == 'O' and btn3.get()== 'O'  or
      btn4.get()=='O' and btn5.get() == 'O' and btn6.get()== 'O'  or
      btn7.get()=='O' and btn8.get() == 'O' and btn9.get()== 'O'  or
      btn1.get()=='O' and btn4.get() == 'O' and btn7.get()== 'O'  or
      btn2.get()=='O' and btn5.get() == 'O' and btn8.get()== 'O'  or
      btn3.get()=='O' and btn6.get() == 'O' and btn9.get()== 'O'  or
      btn1.get()=='O' and btn5.get() == 'O' and btn9.get()== 'O'  or
      btn3.get()=='O' and btn5.get() == 'O' and btn7.get()== 'O'  ):
       tkinter.messagebox.showinfo("TIC TAC TOE",'PLAYER O WINS😍')
       count=0
       clear()
       play()
       
    elif(count==9):
        tkinter.messagebox.showinfo("TIC TAC TOE",'TIE GAME 🥰')
        click=True
        count=0
        clear()
        play()

        
def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    
play()
root.mainloop()