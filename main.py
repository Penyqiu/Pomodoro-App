import time
from tkinter import *



def start_count():
    decrease_time(5)


def decrease_time(count):
    print(count)
    canvas.itemconfig(timer, text=count)
    if count > 0:
        root.after(1000, decrease_time,count -1)


root = Tk()


root.title("Working with twoj stary timer")
root.config(padx=100,pady=50, background="black")


canvas = Canvas(width=200,height=224, background="black", highlightthickness=0)


hasbulla = PhotoImage(file="hasbulla.png")
canvas.create_image(100,200,image=hasbulla)
start_button = Button(text="Jazda",command=start_count)
start_button.grid(column=0, row=2)
timer = canvas.create_text(103,130,text="00:00", fill="white", font=("Arial",40,"bold"))
canvas.pack()






# Execute tkinter
root.mainloop()