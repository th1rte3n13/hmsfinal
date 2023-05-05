#all the modiules imported 
from tkinter import *
from subprocess import call
import os

#function to check that room no occupied or not 
def checking_out():
    import os
    import csv
    gst=[]
    f1=open("guest_list.csv","r")
    f2=open("guest_list2.csv","a")
    gs=e1.get()
    gst=csv.reader(f1)
  
    for row in gst:
        if row==[]:
            pass
        elif row[4]!= gs:
            wr=csv.writer(f2)
            wr.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]])
            mylabel4=Label(root,text="-------------------------------------------------",font="times 20 bold")
            mylabel4.place(x=400,y=200)
            mylabel10=Label(root,text="RECORD DELETED ",font="times 20 bold")
            mylabel10.place(x=450,y=230)
            mylabel3=Label(root,text="-------------------------------------------------",font="times 20 bold")
            mylabel3.place(x=400,y=260)
            
         
    f1.close()
    f2.close()
    os.remove('guest_list.csv')
    os.rename('guest_list2.csv','guest_list.csv')
    
    check_out_label=Label(root,text=" Checked  Out.",font="times 25 bold")
    check_out_label.place(x=420,y=290)

    thank_you=Label(root,text="THANK YOU !!!",font="times 25 bold")
    thank_you.place(x=550,y=330)

    
#if room occupied checked then to diplay all the data of the guest staying in the room 
def display_record():
    import os
    import csv
    gst=[]
    f1=open("guest_list.csv","r")
    gs=e1.get()
    gst=csv.reader(f1)

    for row in gst:
        if row==[]:
            pass
        elif row[4]==gs:
            name=row[0]
            address=row[1]
            phone_no=row[2]
            email_id=row[3]
            room_no=row[4]
            room_type=row[5]
            cost_of_stay=row[7]
            check_in_date=row[8]
            check_in_time=row[9]
            divider=Label(root,text="-------------------------------------------------------------------------------------------------------------------------------------",font="times 15 bold")
            divider.place(x=0,y=160)
            label2=Label(root,text="Guest name :",font="times 15 bold")
            label2.place(x=50,y=200)
            label3=Label(root,text=name,font="times 15 bold")
            label3.place(x=200,y=200)
            label4=Label(root,text="Guest Address :",font="times 15 bold")
            label4.place(x=50,y=230)
            label5=Label(root,text=address,font="times 15 bold")
            label5.place(x=200,y=230)
            label6=Label(root,text="Guest phone no :",font="times 15 bold")
            label6.place(x=50,y=260)
            label7=Label(root,text=phone_no,font="times 15 bold")
            label7.place(x=200,y=260)
            label8=Label(root,text="Guest Email_ID:",font="times 15 bold")
            label8.place(x=50,y=290)
            label9=Label(root,text=email_id,font="times 15 bold")
            label9.place(x=200,y=290)
            label10=Label(root,text="Guest room no :",font="times 15 bold")
            label10.place(x=50,y=320)
            label11=Label(root,text=room_no,font="times 15 bold")
            label11.place(x=200,y=320)
            label12=Label(root,text="Room Type :",font="times 15 bold")
            label12.place(x=50,y=350)
            label13=Label(root,text=room_type,font="times 15 bold")
            label13.place(x=200,y=350)              
            label14=Label(root,text="Check in Date/Time: :",font="times 15 bold")
            label14.place(x=50,y=380)
            label15=Label(root,text=check_in_date,font="times 15 bold")
            label15.place(x=230,y=380)
            label16=Label(root,text=check_in_time,font="times 15 bold")
            label16.place(x=330,y=380)
            label17=Label(root,text="Cost of stay:",font="times 15 bold")
            label17.place(x=50,y=410)
            label18=Label(root,text=cost_of_stay,font="times 15 bold")
            label18.place(x=230,y=410)

            check_out=Button(root,text="Check Out",font="times 20 bold",command=checking_out)
            check_out.place(x=100,y=440)

    f1.close()
    
    
#base for the tkiter window                         
root = Tk()
root.iconbitmap(r'C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico')
root.geometry('900x600')
root.configure(bg='#e6e6fa')
root.title('CHECKING OUT')

label1=Label(root,text=" YOU CHOICE WAS: CHECK OUT",font="Helvetica 30 bold", fg="#663399",bg='#e6e6fa')
label1.place(x=100,y=30)

label2=Label(root,text="-------------------------------------------------------------------------------------------------------------",font="Helvetica 25 bold", fg="#9370DB",bg='#e6e6fa')
label2.place(x=0,y=75)

# entering room no to be checked out
label3=Label(text="ENTER THE ROOM NO.:",font="Verdana 18 bold", fg="#8B008B",bg='#e6e6fa')
label3.place(x=30,y=120)

e1=Entry(root,width=30,font="Verdana 18",fg='#e6e6fa')
e1.place(x=350,y=125)

# button to display all data of the room no entered
button1=Button(root,text="OK",font="Verdana 15 bold", bg="#9370DB", fg="black", command=display_record)
button1.place(x=800,y=120)

root.mainloop()