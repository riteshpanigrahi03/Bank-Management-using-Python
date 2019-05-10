
from tkinter import *
import tkinter.messagebox
from numpy import *
import pickle
import re
import mysql.connector


a=1
def doWithdraw(event):
    for widget in windowdetails.winfo_children():
        widget.destroy()
    if a==1:
        para=(acc_new)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d'" % para)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user[6])

    if a==2:
        args=(account,passwd)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d' and password='%s'" % args)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user)
            print(user[2])

        
    l=Label(windowdetails,text=('Your current balance is --Rs{0}'.format(user[6])),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=130)
    l=Label(windowdetails,text=('Withdraw Money:  '),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=160)
    e=Entry(windowdetails,width=20,fg='black',bg='white',font=('Arial',16))
    def display(event):
        l=Label(windowdetails,text=('Your balance after withdraw  is --Rs{0}'.format(user[6]-int(e.get()))),font=('Arial',16),fg='black',bg='lightblue')
        l.place(x=20,y=190)
        l=Label(windowdetails,text=('PRESS SUBMIT TO WITHDRAW.'),font=('Arial',16),fg='red',bg='lightblue')
        l.place(x=35,y=220)
        sub=Button(windowdetails,text='SUBMIT',bg='red',fg='black',width=6,height=2)
        sub.place(x=100,y=250)
        def updateBalance(event):
            cur.execute("update customersdetails set bal ='%d' where account_no = '%d'" % (user[6]-int(e.get()),user[5]))
            db.commit()
        sub.bind("<Button-1>",updateBalance)
    e.place(x=100,y=160)
    e.bind("<Return>",display)       
    
    exitt=Button(windowdetails,text='EXIT',bg='red',fg='black',width=6,height=2,command=quit)
    exitt.place(x=190,y=250)



def doDeposit(event):
    for widget in windowdetails.winfo_children():
        widget.destroy()
    if a==1:
        para=(acc_new)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d'" % para)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user[6])

    if a==2:
        args=(account,passwd)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d' and password='%s'" % args)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user)
            print(user[2])

        
    l=Label(windowdetails,text=('Your current balance is --Rs{0}'.format(user[6])),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=130)
    l=Label(windowdetails,text=('Deposit Money:  '),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=160)
    e=Entry(windowdetails,width=20,fg='black',bg='white',font=('Arial',16))
    def display(event):
        l=Label(windowdetails,text=('Your balance after deposit  is --Rs{0}'.format(user[6]+int(e.get()))),font=('Arial',16),fg='black',bg='lightblue')
        l.place(x=20,y=190)
        l=Label(windowdetails,text=('PRESS SUBMIT TO DEPOSIT.'),font=('Arial',16),fg='red',bg='lightblue')
        l.place(x=35,y=220)
        sub=Button(windowdetails,text='SUBMIT',bg='red',fg='black',width=6,height=2)
        sub.place(x=100,y=250)
        def updateBalance(event):
            cur.execute("update customersdetails set bal ='%d' where account_no = '%d'" % (user[6]+int(e.get()),user[5]))
            db.commit()
        sub.bind("<Button-1>",updateBalance)
    e.place(x=100,y=160)
    e.bind("<Return>",display)       
    
    exitt=Button(windowdetails,text='EXIT',bg='red',fg='black',width=6,height=2,command=quit)
    exitt.place(x=190,y=250)



        




    
def printprofile(event):
    '''global loginname
    global s
    global a
    print(s)'''
    for widget in windowdetails.winfo_children():
        widget.destroy()

    print(a)
    #print(account)
    #print(passwd)
    if a==2:
        args=(account,passwd)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d' and password='%s'" % args)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user)
            print(user[2])

    if a==1:
        para=(acc_new)
        db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
        if db.is_connected():
            print("connected")
            cur=db.cursor()
            cur.execute("SELECT * from customersdetails WHERE account_no='%d'" % para)
            data=cur.fetchall()
            print(data)
            user=data[0]
            print(user)
            print(user[2])

            
        
    l=Label(windowdetails,text=('Name:          '+user[0]),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=30)

    l=Label(windowdetails,text=('Email Id:      '+user[1]),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=70)

    l=Label(windowdetails,text=('Contact:       {0}'.format(user[2])),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=110)

    l=Label(windowdetails,text=('Gender:       '+user[3]),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=150)

    l=Label(windowdetails,text=('Password:    '+user[4]),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=190)

    l=Label(windowdetails,text=('Account No.: {0}'.format(user[5])),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=230)

    l=Label(windowdetails,text=('Balance:      {0}'.format(user[6])),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=270)
    rootmain.mainloop()
    

def mainpage():

    global a
    if a==1:
        windowsignup.destroy()
        rootsignup.destroy()
    if a==2:
        windowlogin.destroy()
        rootlogin.destroy()

    global rootmain
    global windowmain
    global windowdetails
    global accno
    
   
    rootmain=Tk()
    windowmain=Frame(rootmain,width=400,height=50,bg='lightblue')
    rootmain.title("Account")
    windowmain.grid(row=0,column=4)
    
    profilebutton=Button(windowmain,text='Profile',width=10,height=1,bg='red',fg='white')
    profilebutton.place(x=20,y=20)
    profilebutton.bind("<Button-1>",printprofile)
    
    depositbutton=Button(windowmain,text='Deposit',width=10,height=1,bg='red',fg='white')
    depositbutton.place(x=150,y=20)
    depositbutton.bind("<Button-1>",doDeposit)

    withdrawbutton=Button(windowmain,text='Withdraw',width=10,height=1,bg='red',fg='white')
    withdrawbutton.place(x=280,y=20)
    withdrawbutton.bind("<Button-1>",doWithdraw)


    windowdetails=Frame(rootmain,width=400,height=400,bg='lightblue')
    windowdetails.grid(row=1,column=4)
    
    rootmain.mainloop()


def checkuser(event):
    global account
    global passwd
    account=int(accentry.get())
    passwd=passentry.get()
    db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
    if db.is_connected():
        print("connected")
        
    cur=db.cursor()
    
    args=(account,passentry.get())
    #print(bool(cur.execute("SELECT * from customersdetails WHERE account_no='%d' and password='%s'" % args)))
    
    '''if(not bool(cur.execute("SELECT * from customersdetails WHERE account_no='%d' and password='%s'" % args))):
            
        data = cur.fetchall()
        print(data)
        tkinter.messagebox.showinfo("Logged In","successful")
        print("yessss")
    else:
        tkinter.messagebox.showerror("Error","invalid credentials")'''
            
    
        
    
    #below is the alternate code for searching    
    cur.execute("select password,account_no from customersdetails")
    data=cur.fetchall()
    print(data)
    global flag
    flag=0
    
    for i in data:
        if((passentry.get()==i[0]) and (account==i[1]) and flag==0):
            flag=1
            print("hello")
            print(i)
            tkinter.messagebox.showinfo("Logged In","successful")
            mainpage()
            break
    if flag==0:
        tkinter.messagebox.showerror("Error","invalid credentials")
        
def loginfunc(event):
    global a
    global loginname 
    
    a=2
    windows.destroy()
    root1.destroy()
    global rootlogin
    global windowlogin
    global accentry
    global passentry

    rootlogin=Tk()
    windowlogin=Frame(rootlogin,width=400,height=300,bg="lightblue")
    rootlogin.title("Login")
    windowlogin.pack()

    acclabel=Label(windowlogin,text='Account:-\nNumber',bg='lightblue')
    acclabel.place(x=30,y=35)
    
    accentry=Entry(windowlogin,width=20,fg='black',bg='white',font=('Arial',16))
    accentry.place(x=110,y=30)
    
    passlabel=Label(windowlogin,text='Password:-',bg='lightblue')
    passlabel.place(x=30,y=70)
    
    passentry=Entry(windowlogin,width=20,fg='black',bg='white',font=('Arial',16),show='*')
    passentry.place(x=110,y=65)
    login=Button(windowlogin,text='Login',width=5,height=2,bg='red',fg='white')
    login.place(x=140,y=110)
    login.bind("<Button-1>",checkuser)
                
    rootlogin.mainloop()        
        
     
    
def generateAccountNumber(event):
    db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")

    global s
    global accno
    
    name=namee1.get()
    email=emaile2.get()
    gender=var.get()
    cno=int(phoe3.get())
    password=passe4.get()
    if gender==1:
        sex='M'
    else:
        sex="F"

    if(bool(re.search(r'\d', name))) or (name ==""):
        tkinter.messagebox.showinfo("INVALID","Your name is invalid please enter a valid name")

    if (re.search("[@.]",email) is None) or (email ==""):
        tkinter.messagebox.showinfo("INVALID","Your e-mail id is invalid please enter a valid e-mail id with ''@.''")

    
        
    if len(password) < 8:
        flag=-1
    elif re.search('[0-9]',password) is None:
        flag=-1
    elif re.search('[A-Z]',password) is None:
        flag=-1
        print("Make sure your password has a capital letter in it")
    else:
        flag=1
    if flag == -1:
        tkinter.messagebox.showinfo("INVALID","Your password is invalid ")


    else:
        global acc_new
        accno=int(random.rand()*100000)
        acc_new=accno
        accno=str(accno)
        s=accno
        tkinter.messagebox.showinfo("Account Created","Your account number is:"+accno)

        cur = db.cursor()
        #str="insert into customersdetails(name,email,contact,gender,password,account_no) values('%s','%s','%d','%s','%s','%d')"
        cur.execute("insert into customersdetails(name,email,contact,gender,password,account_no,bal) values('%s','%s',%d,'%s','%s',%d,%d)"%(name,email,cno,sex,password,acc_new,1000))
        db.commit()
        cur.close()
        db.close()


    
def signupfunc(event):
    
    global a
    a=1
    windows.destroy()
    root1.destroy()
    global rootsignup
    global windowsignup
    
    rootsignup=Tk()
    windowsignup=Frame(rootsignup,width=400,height=300,bg="lightblue")
    windowsignup.pack()
    rootsignup.title("Signup")
    namelabel=Label(windowsignup,text='NAME:-',bg='lightblue')
    namelabel.place(x=30,y=35)

    global namee1
    global emaile2
    global phoe3
    global g1
    global g2
    global passe4
    global accno

    
    namee1=Entry(windowsignup,width=20,fg='black',bg='white',font=('Arial',16))
    namee1.place(x=110,y=30)
    
    emaillabel=Label(windowsignup,text='Email Id:-',bg='lightblue')
    emaillabel.place(x=30,y=75)
    
    emaile2=Entry(windowsignup,width=20,fg='black',bg='white',font=('Arial',16))
    emaile2.place(x=110,y=70)

    pholabel=Label(windowsignup,text='CONTACT:-',bg='lightblue')
    pholabel.place(x=30,y=115)

    phoe3=Entry(windowsignup,width=20,fg='black',bg='white',font=('Arial',16))
    phoe3.place(x=110,y=110)
    
    genderlabel=Label(windowsignup,text='GENDER:-',bg='lightblue')
    genderlabel.place(x=30,y=145)
    global var
    var=IntVar()
    g1=Radiobutton(windowsignup,text='MALE',variable=var,value=1,bg='lightblue')
    g1.place(x=110,y=145)
    g2=Radiobutton(windowsignup,text='FEMALE',variable=var,value=2,bg='lightblue')
    g2.place(x=175,y=145)
    

    passlabel=Label(windowsignup,text='PASSWORD:-',bg='lightblue')
    passlabel.place(x=30,y=180)
    
    passe4=Entry(windowsignup,width=20,fg='black',bg='white',font=('Arial',16),show='*')
    passe4.place(x=110,y=175)

    passAlert=Label(windowsignup,text='* Your password should be alphanumeric,there should be a capital letter and\n the length should be of atleast 8 characters.',bg='lightblue',fg="red")
    passAlert.place(x=15,y=210)
    

    done=Button(windowsignup,text='DONE',width=5,height=2,bg='red',fg='white')
    done.place(x=100,y=250)
    done.bind("<Button-1>",generateAccountNumber)
    

    
    submit=Button(windowsignup,text='SUBMIT',width=5,height=2,bg='red',fg='white',command=mainpage)
    submit.place(x=180,y=250)
    #submit.bind("<Button-1>",mainpage)  
    rootsignup.mainloop()

def userclick(event):
    window.destroy()
    root.destroy()
    global root1
    global windows
    
    root1=Tk()
    
    windows=Frame(root1,width=400,height=300,bg="lightblue")
    root1.title("HSBC")

    logo1=PhotoImage(file="front.png")
    logo1label=Label(windows,image=logo1)
    logo1label.place(x=20,y=20)

    
    login=Button(windows,text='LOG IN',width=20,bg="blue",fg="white")
    login.bind("<Button-1>",loginfunc)
    login.place(x=10,y=250)

    signup=Button(windows,text="NEW USER",width=20,bg="blue",fg="white")
    signup.bind("<Button-1>",signupfunc)
    signup.place(x=205,y=250)
   
    windows.pack()
    root1.mainloop()


def staffclick(event):
   global root10
   window.destroy()
   root.destroy()

   rootstaff=Tk()
   rootstaff.title("STAFF")
   windstaff=Frame(rootstaff,width=600,height=500,bg="lightblue")
   windstaff.pack(side=TOP)

   photo=PhotoImage(file="staff.png")
   label=Label(windstaff,image=photo)
   label.place(x=100,y=130)

   menu=Menu(rootstaff)
   rootstaff.config(menu=menu)

   def customerlist():
    
       windo1=Frame(rootstaff,width=600,height=500,bg="lightblue")
       windo1.place(x=0,y=0)
       db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
       t=t=Text(windo1,width=400,height=200,font=("Verdana",8,'bold'),fg="BLACK",bg="lightgreen",wrap=WORD)
       if db.is_connected():
           
           cur=db.cursor()
           cur.execute("select * from customersdetails")
           rows=cur.fetchall()
           data=[tuple(str(x) for x in xs) for xs in rows]
           print(data)
           s=''
           for i in data:
               s+='       '.join(i)
               s+="\n"
           print(s)
           t.insert(END,s)
                
   submenu=Menu(menu)
   menu.add_cascade(label="Customer List",menu=submenu)
   submenu.add_command(label="VIEW",command=customerlist)
   submenu.add_command(label="EXIT",command=quit)


   def terms():
          
          windo2=Frame(rootstaff,width=600,height=500,bg="lightblue")
          windo2.place(x=0,y=0)
          t=Text(windo2,width=400,height=200,font=("Verdana",8,'bold'),fg="BLACK",bg="lightgreen",wrap=WORD)
          t.insert(END,'''
Courses Eligible:

 a. Studies in India:
• Graduation, Post-graduation including regular technical
and professional Degree/Diploma courses conducted by
colleges/universities approved by UGC/ AICTE/IMC/Govt.
etc
• Regular Degree/ Diploma Courses conducted by
autonomous institutions like IIT, IIM etc
• Teacher training/ Nursing courses approved by Central
government or the State Government
• Regular Degree/Diploma Courses like Aeronautical, pilot
training, shipping etc. approved by Director General of
Civil Aviation/Shipping
• Vocational Training and skill development study courses
will not be covered under the Education Loan Scheme, as
the scheme is framed to provide bank loans for higher
studies.
\n b. Studies abroad:
• Graduation/ Post-graduation for job oriented
professional/ technical courses offered by reputed
universities 



Student Eligibility:
\n• Should be an Indian National
• Secured admission to Professional/Technical courses
through Entrance Test/Selection process.
• Secured admission to foreign university/Institutions.
• No minimum qualifying marks stipulated in the last
qualifying examination ''')
          t.place(x=0,y=0)

   submenu=Menu(menu)
   menu.add_cascade(label="Terms and Conditions on offers for HSBC Bank Personal Loans ",menu=submenu)
   submenu.add_command(label="VIEW",command=terms)
   submenu.add_command(label="EXIT",command=quit)
   
   def change():

       global windo3
       windo3=Frame(rootstaff,width=600,height=500,bg="lightblue")
       windo3.place(x=0,y=0)
       
       

       previous=Label(windo3,text="Previous Password",bg='yellow',font=('Arial',16))
       entry1=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16),show="*")
       new=Label(windo3,text="New Password",bg='yellow',font=('Arial',16))
       entry2=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16),show="*")                                                      
       account=Label(windo3,text="Account Number",bg='yellow',font=('Arial',16))
       entryacc=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16))

       previous.place(x=80,y=140)
       entry1.place(x=280,y=140)
       new.place(x=80,y=190)
       entry2.place(x=280,y=190)
       account.place(x=80,y=100)
       entryacc.place(x=280,y=100)              

       prev=entry1.get()
       new=entry2.get()
       def update():
           db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1", db = "bankdetails")
           if db.is_connected():
               print('connected')
               cur=db.cursor()
               cur.execute("update customersdetails set password = '%s' where account_no ='%d'" % (entry2.get(),int(entryacc.get())))
               db.commit()

       ok=Button(windo3,text='OK',width=5,height=2,bg='red',fg='white',command=update)
       ok.place(x=250,y=300)

       exitb=Button(windo3,text='Exit',width=5,height=2,bg='red',fg='white',command=quit)
       exitb.place(x=310,y=300)

       


   submenu=Menu(menu)
   menu.add_cascade(label="ChangePassword ",menu=submenu)
   submenu.add_command(label="VIEW",command=change)
   submenu.add_command(label="EXIT",command=quit)


   rootstaff.mainloop()

    
root=Tk()

window=Frame(root,width=600,height=500,bg="lightblue")
root.title("HSBC")

logo=PhotoImage(file="front.png")
logolabel=Label(window,image=logo)
logolabel.place(x=120,y=0)

t=Text(window,width=400,height=3,font=("Verdana",8,'bold'),fg="red",bg="yellow",wrap=WORD)
t.insert(END,"     HSBC never asks for confidential information such as PIN and OTP from customer.\n\t     Any such call can be made only by a fraudster.Please do not share personal info.")
t.place(x=0,y=100)

userimage=PhotoImage(file="ub.png")
userlabel=Label(window,image=userimage)
userlabel.place(x=50,y=180)


staffimage=PhotoImage(file="staff.png")
stafflabel=Label(window,image=staffimage)
stafflabel.place(x=330,y=180)

userbutton=Button(window,text="USERS",width=20,bg="blue",fg="white")
userbutton.bind("<Button-1>",userclick)
userbutton.place(x=70,y=430)

staffbutton=Button(window,text="STAFF",width=20,bg="blue",fg="white")
staffbutton.bind("<Button-1>",staffclick)
staffbutton.place(x=350,y=430)

window.pack()
root.mainloop()
