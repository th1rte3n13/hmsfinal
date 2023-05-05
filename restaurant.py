from tkinter import *
from subprocess import call
def total_bill():
    tea=e1.get()
    breakfast=e2.get()
    lunch=e3.get()
    dinner=e4.get()
    total=((int(tea)*50)+(int(breakfast)*300)+(int(lunch)*400)+(int(dinner)*500))
    #print(total)
    label20=Label(text="YOUR TOTAL BILL IS Rs:",font="times 30 bold")
    label20.place(x=100,y=350)
    labelmain=Label(root,text=total,font="times 30 bold")
    labelmain.place(x=600,y=350)


from tkinter import *

root=Tk()
root.geometry("900x500")
root.title("Restaurant")
root.configure(bg="white")
root.iconbitmap(r"C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico")

# Restaurant name label
labelmain=Label(root, text='ITALINOIC RESTAURANT', font=("Comic Sans MS", 40, "bold"), fg='#FFA500',bg="white")
labelmain.place(x=450, y=40, anchor="center")

# Menu card label
label1=Label(root, text="MENU", font=("Georgia", 35, "bold"), fg='#483D8B',bg="white")
label1.place(x=600, y=120)

# Menu items labels
label2=Label(root, text="               Tea            | RS=50", font=("Arial", 22, "bold"), fg='#006400',bg="white")
label2.place(x=500, y=190)

label3=Label(root, text="               Coffee       | RS=50", font=("Arial", 22, "bold"), fg='#006400',bg="white")
label3.place(x=500, y=220)

label4=Label(root, text="               Breakfast  | RS=300", font=("Arial", 22, "bold"), fg='#006400',bg="white")
label4.place(x=500, y=250)

label5=Label(root, text="               Lunch       | RS=400", font=("Arial", 22, "bold"), fg='#006400',bg="white")
label5.place(x=500, y=280)

label6=Label(root, text="               Dinner       | RS=500", font=("Arial", 22, "bold"), fg='#006400',bg="white")
label6.place(x=500, y=310)

# Billing system labels and entries
label7=Label(root, text="Enter the number of items", font=("Verdana", 20, "bold"), fg='#800000',bg="white")

label7.place(x=70, y=80)

label8=Label(root, text="Tea/Coffee:", font=("Verdana", 20, "bold"), fg='#800000',bg="white")
label8.place(x=20, y=140)

e1=Entry(root, font=("Verdana", 18, "bold"))
e1.place(x=20, y=180)

label9=Label(root, text="Breakfast:", font=("Verdana", 20, "bold"), fg='#800000',bg="white")
label9.place(x=250, y=140)

e2=Entry(root, font=("Verdana", 18, "bold"))
e2.place(x=250, y=180)

label10=Label(root, text="Lunch:", font=("Verdana", 20, "bold"), fg='#800000',bg="white")
label10.place(x=20, y=220)

e3=Entry(root, font=("Verdana", 18, "bold"))
e3.place(x=20, y=260)

label11=Label(root, text="Dinner:", font=("Verdana", 20, "bold"), fg='#800000',bg="white")
label11.place(x=250, y=220)

e4=Entry(root, font=("Verdana", 18, "bold"))
e4.place(x=250, y=260)

# Total Bill button
bill=Button(text="Total Bill", font=("Verdana", 25, "bold"), bg='#FFA500', fg='#483D8B', command=total_bill)
bill.place(x=120, y=330)

root.mainloop()