#all modules needed imported 
from tkinter import *
from subprocess import call

#all the functions to call program based on choice 
def check_in_call():
    call(["python",r"C:\Users\Max Gonsalves\max\hmsfinalproject\check_in.py"])
def check_out_call():
    call(["python",r"C:\Users\Max Gonsalves\max\hmsfinalproject\check_out.py"])
def restaurent_call():
    call(["python",r"C:\Users\Max Gonsalves\max\hmsfinalproject\restaurant.py"])
def guest_list():
    call(["python",r"C:\Users\Max Gonsalves\max\hmsfinalproject\show_guest_list.py"])

#basic defination of tkinter window
root = Tk()
root.title("Hotel Mangement System")
root.iconbitmap(r"C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico")
root.geometry("650x650")
root.configure(bg='#8b5d9e')

# Topmost label
myLabel= Label(root, text="WELCOME TO HOTEL MANGEMENT SYSTEM !!!", font="Courier 20 bold", bg='#8b5d9e')
myLabel.pack()

# Check in button
mybutton = Button(root, text="1. CHECK INN", padx=91, pady=30, bg='#644e99', fg='white', font="Courier 20 bold", command=check_in_call)
mybutton.pack()

# Show all the guest list button
mybutton2 = Button(root, text="2. SHOW GUEST LIST", padx=43, pady=30, bg='#523e84', fg='white', font="Courier 20 bold", command=guest_list)
mybutton2.pack()

# Function call to check out the guest
mybutton3 = Button(root, text="3. CHECK OUT", padx=91, pady=30, bg='#523e84', fg='white', font="Courier 20 bold", command=check_out_call)
mybutton3.pack()

# Restaurent button
mybutton5 = Button(root, text="5 . RESTAURENT", padx=75, pady=30, bg='#3e2c6f', fg='white', font="Courier 20 bold", command=restaurent_call)
mybutton5.pack()

# Exit button
mybutton6 = Button(root, text="5. EXIT", padx=130, pady=30, bg='#3e2c6f', fg='white', font="Courier 20 bold", command=root.destroy)
mybutton6.pack()

# Infinite loop for GUI to work
root.mainloop()
