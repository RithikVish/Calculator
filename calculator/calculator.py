from tkinter import *

def click(event):
    global ScreenValue
    global screenEntry
    text = event.widget.cget("text")
    print(text)
    if text== "=":
        if ScreenValue.get().isdigit():
            value = int(ScreenValue.get())
        else:
            value = eval(screenEntry.get())
        ScreenValue.set(value)
        screenEntry.update()

    elif text== "c":
        ScreenValue.set("")
        screenEntry.update()
    else:
        ScreenValue.set(ScreenValue.get() + text)
        screenEntry.update()

root = Tk()
root.geometry("360x420")
root.resizable(False,False)
root.wm_iconbitmap("Wineass-Ios7-Redesign-Calculator.ico")
root.title("Calculator")
root.config(bg="grey")

ScreenValue = StringVar()
ScreenValue.set("")
screenEntry = Entry(root, textvar=ScreenValue, font="Lucida 35 bold",justify="right")
screenEntry.focus()
screenEntry.pack()
frame1 = Frame(root)
frame1.pack(side=TOP,anchor="w")

frame1 = Frame(root)
frame1.pack(anchor="w")

frame2 = Frame(root)
frame2.pack(anchor="w")

frame3 = Frame(root)
frame3.pack(anchor="w")

frame4 = Frame(root)
frame4.pack(anchor="w")

b1 = Button(frame1, text = "7",font="Lucida 30", borderwidth=8,width=3)
b1.bind("<Button-1>",click)
b1.pack(side="left")


b2 = Button(frame1, text = "8",font="Lucida 30", borderwidth=8,width=3)
b2.bind("<Button-1>",click)
b2.pack(side="left")

b3 = Button(frame1, text = "9",font="Lucida 30", borderwidth=8,width=3)
b3.bind("<Button-1>",click)
b3.pack(side="left")

b4 = Button(frame1, text = "+",font="Lucida 30", borderwidth=8,width=3)
b4.bind("<Button-1>",click)
b4.pack(side="left")

b5 = Button(frame2, text = "4",font="Lucida 30", borderwidth=8,width=3)
b5.bind("<Button-1>",click)
b5.pack(side="left")

b6 = Button(frame2, text = "5",font="Lucida 30", borderwidth=8,width=3)
b6.bind("<Button-1>",click)
b6.pack(side="left")

b7 = Button(frame2, text = "6",font="Lucida 30", borderwidth=8,width=3)
b7.bind("<Button-1>",click)
b7.pack(side="left")

b8 = Button(frame2, text = "-",font="Lucida 30", borderwidth=8,width=3)
b8.bind("<Button-1>",click)
b8.pack(side="left")

b9 = Button(frame3, text = "1",font="Lucida 30", borderwidth=8,width=3)
b9.bind("<Button-1>",click)
b9.pack(side="left")

b10 = Button(frame3, text = "2",font="Lucida 30", borderwidth=8,width=3)
b10.bind("<Button-1>",click)
b10.pack(side="left")

b11 = Button(frame3, text = "3",font="Lucida 30", borderwidth=8,width=3)
b11.bind("<Button-1>",click)
b11.pack(side="left")

b12 = Button(frame3, text = "*",font="Lucida 30", borderwidth=8,width=3)
b12.bind("<Button-1>",click)
b12.pack(side="left")

b13 = Button(frame4, text = "c",font="Lucida 30", borderwidth=8,width=3)
b13.bind("<Button-1>",click)
b13.pack(side="left")

b14 = Button(frame4, text = "0",font="Lucida 30", borderwidth=8,width=3)
b14.bind("<Button-1>",click)
b14.pack(side="left")

b15 = Button(frame4, text = "=",font="Lucida 30", borderwidth=8,width=3)
b15.bind("<Button-1>",click)
b15.pack(side="left")

b16 = Button(frame4, text = "/",font="Lucida 30", borderwidth=8,width=3)
b16.bind("<Button-1>",click)
b16.pack(side="left")





root.mainloop()
