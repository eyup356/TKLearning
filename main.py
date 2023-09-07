import tkinter
#window
window = tkinter.Tk()
window.title("python tkinter")
window.minsize(width=500,height=300)
#label
my_label = tkinter.Label(text="LABEL XD")
my_label.config(bg="black",fg="white")
#my_label.pack(side="bottom")
#my_label.place(x=50,y=150)
#my_label.update()
#print(my_label.winfo_height())
my_label.grid(row=2,column=1)
def click_button():
    user_input=my_entry.get()
    print(user_input)
#button
my_button = tkinter.Button(text="BUTTON XD", command=click_button)
my_button.grid(row=1,column=2)
#entry
my_entry = tkinter.Entry(width="15",)
my_entry.grid(row=0,column=2)
#my_entry.pack()
window.mainloop()