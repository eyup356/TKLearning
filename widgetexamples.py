from tkinter import *

window = Tk()
window.title("python tkinter")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20)

#label
label = Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.pack()
label.config(padx=20,pady=20)

def button_clicked():
    print(text.get("1.0", END))

button= Button(text="Button", command=button_clicked)
button.config(padx=20,pady=20)
button.pack()

entry = Entry(width=20)
entry.pack()

text = Text(width=30)
text.pack()
text.focus()

#scale
def scale_selected(value):
    print(value)
    print(my_scale.get())
my_scale = Scale(from_=0,to=50, command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())
check_state=IntVar()
my_checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()
window.mainloop()