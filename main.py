# all modules needed to import
from tkinter import *
from subprocess import call
from datetime import datetime
from datetime import date

# for display of current date and time
today = date.today()
d1 = today.strftime("%d/%m/%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# to check the password and username
def command1(event):
    if entry1.get() == 'admin' and entry2.get() == '123456' or entry1.get() == 'max' and entry2.get() == '123456':
        call(["python", r"C:\Users\Max Gonsalves\max\hmsfinalproject\Hotel_management_system.py"])
    root.destroy()

# defining root base of tkinter program
root = Tk()
root.iconbitmap(r'C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico')
root.geometry('500x500')
root.title('LOGIN SCREEN')
root.configure(bg='#D6D1E6') # set background color

hotel_image = PhotoImage(file=r"C:\Users\Max Gonsalves\max\hmsfinalproject\HOTEL.gif")
photo = Label(root, image=hotel_image, bg='#D6D1E6')
photo.pack()

# main screen
mylabelmain = Label(root, text="LOGIN YOUR ACCOUNT", font=("Helvetica", 20, "bold"), fg='#484C7F', bg='#D6D1E6') # change font and colors
mylabelmain.pack()

# entering username
mylabel = Label(root, text="Username:", font=("Helvetica", 15), fg='#484C7F', bg='#D6D1E6') # change font and colors
mylabel.pack()

entry1 = Entry(root, width=25, font=("Helvetica", 12), bg='#E3E1F3', fg='#484C7F') # change font and colors
entry1.pack()

# entering password
label2 = Label(root, text="Password:", font=("Helvetica", 15), fg='#484C7F', bg='#D6D1E6') # change font and colors
label2.pack()

entry2 = Entry(root, show='*', width=25, font=("Helvetica", 12), bg='#E3E1F3', fg='#484C7F') # change font and colors
entry2.pack()

# bind buttontype entry for enter on keyboard
entry2.bind('<Return>', command1)

# exit the program
button1 = Button(root, text='Cancel', font=("Helvetica", 12), bg='#D6D1E6', fg='#484C7F', command=root.destroy) # change font and colors
button1.pack()

# display of date and time in tkinter
date = Label(root, text=d1, fg='#484C7F', bg='#D6D1E6', font=("Helvetica", 15)) # change font and colors
date.place(x=380, y=450)

time = Label(root, text=current_time, fg='#484C7F', bg='#D6D1E6', font=("Helvetica", 15)) # change font and colors
time.place(x=380, y=420)

# infinitely looping the GUI to work
root.mainloop()