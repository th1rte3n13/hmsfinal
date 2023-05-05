from tkinter import *
from subprocess import call
import sys

def guest_name(event):
    import csv
    with open("guest_list.csv","r") as f:
        gs=e1.get()
        gst=csv.reader(f)
        for row in gst:
            if row==[]:
                no_data=Label(root,text="NO DATA PRESENT")
                no_data.place()
                pass
            elif row[4]==gs:
                gst_name=row[0]
                label=Label(root,text="WELCOME:                                    ",font="times 18 bold")
                label.place(x=100,y=150)
                label2=Label(root,text=gst_name,font="times 18 bold")
                label2.place(x=250,y=150)
                enter=Button(root,text="ENTER RESTAURANT",font="times 12 bold",command=call_restaurant)
                enter.place(x=160,y=185)
                break
            else:
                room_not_match=Label(root,text="ROOM NO. DOES NOT EXIST",font="times 18 bold")
                room_not_match.place(x=100,y=150)

    
def call_restaurant():
    call(["python",r"C:\Users\Max Gonsalves\max\hmsfinalproject\restaurant.py"])

    
#def check_room():
 #   import os
  #  import csv
   # with open("guest_list.csv","r") as f:
    #    gs=e1.get()
     #   gst=csv.reader(f)
      #  for row in gst:
       #     if row==[]:
        #        pass
         #   elif row[4]==gs:
          #      call(["python","restaurent.py"])
           #     break
            #else:
             #   mylabel2=Label(root,text="room no. does not exist",font="Courier 15")
              #  mylabel2.pack()
            
from tkinter import *
from subprocess import call

root = Tk()
root.iconbitmap(r"C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico")
root.geometry('550x300')
root.title('CHECKING ROOM NO')
root.configure(bg='#e6e6fa')

mylabelmain = Label(root, text="TO CHECK WHETHER ROOM NO EXIST", font="Helvetica 20 bold", fg='#800080', bg='#e6e6fa')
mylabelmain.place(x=0, y=15)

mylabel = Label(root, text="    ENTER ROOM NO:", font="Helvetica 15", fg='#4b0082', bg='#e6e6fa')
mylabel.place(x=170, y=50)

e1 = Entry(root, width=25, font="Helvetica 12")
e1.place(x=170, y=80)
e1.bind('<Return>', guest_name)

button1 = Button(root, text='Cancel', font="Helvetica 12", fg='#4b0082', bg='#e6e6fa', command=root.destroy)
button1.place(x=240, y=110)

root.mainloop()