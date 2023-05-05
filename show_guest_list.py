from tkinter import *
from tkinter import ttk
import csv


def guest_staying():
    with open("guest_list.csv", "r") as f:
        gst = csv.reader(f)
        # v = Scrollbar(root)
        # v.pack(side = RIGHT, fill = Y)
        # gst.config(command=t.yview)
        for row in gst:
            if row == []:
                pass
            else:
                name = row[0]
                address = row[1]
                phone_no = row[2]
                room_no = row[3]
                room_type = row[4]
                label2 = Label(second_frame, text="Guest name:", font="times 12 bold")
                label2.pack()
                label3 = Label(second_frame, text=name, font="times 12 bold")
                label3.pack()
                label4 = Label(second_frame, text="Guest address:", font="times 12 bold")
                label4.pack()
                label5 = Label(second_frame, text=address, font="times 12 bold")
                label5.pack()
                label6 = Label(second_frame, text="Guest phone no:", font="times 12 bold")
                label6.pack()
                label7 = Label(second_frame, text=phone_no, font="times 12 bold")
                label7.pack()
                label8 = Label(second_frame, text="Guest room no", font="times 12 bold")
                label8.pack()
                label9 = Label(second_frame, text=room_no, font="times 12 bold")
                label9.pack()
                label10 = Label(second_frame, text="Room Type :", font="times 12 bold")
                label10.pack()
                label11 = Label(second_frame, text=room_type, font="times 12 bold")
                label11.pack()
                label12 = Label(second_frame,
                                text="-------------------------------------------------------------------------",
                                font="times 15 bold")
                label12.pack()


root = Tk()
root.title("GUEST_LIST")
root.iconbitmap(r"C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico")
root.geometry('650x800')
root.configure(bg="#E6E6FA")  # set background color to lavender

# Create a main frame
main_frame = Frame(root, bg="#E6E6FA")  # set background color to lavender
main_frame.pack(fill=BOTH, expand=1)

# create a Canvas
my_canvas = Canvas(main_frame, bg="#E6E6FA", highlightthickness=0)  # set background color to lavender
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add a scrolllbar to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
# crete another frame inside the canvas
second_frame = Frame(my_canvas, bg="#E6E6FA")  # set background color to lavender
# add that new frame to a windoe in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

label1 = Label(second_frame, text="                     DISPLAY ALL GUEST LIST                      ", font="Times 20 bold", bg="#E6E6FA", fg="#4B0082")  # set background color to lavender and foreground color to indigo
label1.pack()

button1 = Button(second_frame, text="DISPLAY ALL", font="Courier 20 bold", bg="#9370DB", fg="#800080", command=guest_staying)  # set background color to medium purple and foreground color to white
button1.pack()


root.mainloop()