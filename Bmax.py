from self import start_up
from self import pages
start_up.boot_up()
pages.set1.page1()
import os
from tkinter import *
from self import food_and_diet
from self import animations
from self import startmode
from self import placeholder
from self import variable
import tkinter as tk
from self import search_script
import datetime
from self import problem
import tkinter.messagebox as tmsg

try:
    import mysql.connector
    from self import mysql_connections
except:tmsg.showwarning("Software-Plot","Bmax:mysql_connections module faild to import")



try:
    from covid_india import states
except ModuleNotFoundError:
    print("covid_india module Not Found-installing for you plz wait..")
    os.system('python -m pip install covid_india')
    print("Installation DONE")
    from covid_india import states
try:
    import wikipedia
except ModuleNotFoundError:
    print("wikipedia module Not Found-installing for you plz wait..")
    os.system('python -m pip install wikipedia')
    print("Installation DONE")
    import wikipedia
try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    print("Pillow module Not Found-installing for you plz wait..")
    os.system('python -m pip install Pillow')
    print("Installation DONE")
    
    
    


bg="#2b2b2b"



def connectdb():
    global hostvalues,myuservalues,passvalues
    hostvalues=hostvalue.get()
    myuservalues=myuservalue.get()
    passvalues=passvalue.get()
    try:
        mydb=mysql.connector.connect(host=hostvalues,user=myuservalues,passwd=passvalues)
        mycursor=mydb.cursor()
#=====(CHECKING CONNECTION STATUS)
        if (mydb):
            #global mysqlframe
            #mysqlframe=animations.AnimatedGIF(mysql_login,"self//butgif.gif").place(relx=0.694,rely=0.755)
            print("ALL OK , CONNECTION MADE SUCESS..")
    except :
        print("mysql rejected your login input " + "check your default host and user or make sure passaword is correct,(Not connected)")
        tmsg.showinfo("ERROR","Wrong credentials,please try to check password and username")   # WARING MEASSAGE BOX WILL OPEN SHOWING ERROR

      
    try:
        if mysql_connections.db_in_database(username1,hostvalues,myuservalues,passvalues)==False:
            mysql_connections.db_create(username1,hostvalues,myuservalues,passvalues)
            mysql_connections.db_table_in(username1,hostvalues,myuservalues,passvalues)
        else:mysql_connections.db_insert_or_update(username1,hostvalues,myuservalues,passvalues,mysql_login)
    except:tmsg.showwarning("Warning","Mysql is not connected with Bmax so it will not increase your userprofile!")   # WARING MEASSAGE BOX WILL OPEN SHOWING ERROR

            
                

    

            
            

    

    
class data():
    def sinuptxt(uvalue,pvalue,gender,sl,h,w):
        dln=[]
        found=0
        
        rnow=open("self\\source\\sinup.txt","r")
        xa=rnow.readlines()
        for io in xa:
            iio=io.split("\n")
            viio=iio[0]
            dln.append(viio)
        length=len(dln)
        dln1=[]
        for y in range(0,length,7):
            valadd=(dln[y])
            dln1.append(valadd)
        rnow.close()
        for A in dln1:
            if A==uvalue:
                found=1
            else: pass
            
       

        if found==1:
            return sl.config(text="This Username Alredy Exist",fg="green")
        else:
            try:
                
                now= datetime.datetime.now()
                tod=(now.strftime("%Y-%m-%d"))
                tot=(now.strftime("%H:%M:%S"))
            except:
                tod="--------"
                tot="--------"
                
            sinfile=open("self\\source\\sinup.txt","a")
            sinfile.write(uvalue)
            sinfile.write("\n")
            sinfile.write(pvalue)
            sinfile.write("\n")
            sinfile.write(gender)
            sinfile.write("\n")
            sinfile.write(str(h))
            sinfile.write("\n")
            sinfile.write(str(w))
            sinfile.write("\n")
            sinfile.write(str(tod))
            sinfile.write("\n")
            sinfile.write(str(tot))
            sinfile.write("\n")
            sinfile.close()
            return sl.config(text="Sucessfully Created!",fg="green")
    def log_txt(user,passw,labelstatus):
        dln=[]
        want=0
        rnow=open("self\\source\\sinup.txt","r")
        xa=rnow.readlines()
        for io in xa:
            iio=io.split("\n")
            viio=iio[0]
            dln.append(viio)
        length=len(dln)
        dln1=[]
        done=0
        for y in range(0,length,7):
            valadd=(dln[y])
            if valadd==user:
                done=1
                if dln[y+1]==passw:
                    done=2
        rnow.close()
        if done==0:
            labelstatus.config(text="Username is not created",fg="#68d87d")
        if done==2:
            labelstatus.config(text="      LOGIN SUCESS",fg="#68d87d")
        elif done==1:
            labelstatus.config(text="    Incorrect Passsword",fg="#ec5959")
        
            
            



class interface():
    def mysqlpage():
        global mysql_login

        mysql_login=Tk()
        

        mysql_login.geometry("463x480+400+120")
        mysql_login.maxsize(463,480)
        mysql_login.minsize(463,480)
        try:
            mysql_login.call('wm', 'iconphoto', mysql_login._w, PhotoImage(file='img_load//smalllogo.png'))
        except:pass
        mysql_login.title("Bmax")
        
        mymenu=Menu(mysql_login)
        m2=Menu(mymenu,tearoff=False)
        m4=Menu(mymenu,tearoff=False)

        

        mymenu.add_cascade(label="Options",menu=m2)
        m2.add_command(label="Check For Mysql_Connection_Module")
        m2.add_command(label="Mysql Install-status")


        mymenu.add_cascade(label="Help",menu=m4)
        m4.add_command(label="Screen Info")

        mysql_login.config(menu=mymenu)
     
        #TITLEBAR MENU ENDS--

       
        global mysqlframe
        mysql_login.config(bg="#ffffff")
        mysqlframe=animations.AnimatedGIF(mysql_login,"img_load//data.gif")
        mysqlframe.pack()
        mysqlframe.config(bd=0)

        sqlabel=Label(mysql_login,text="MYSQL LOGIN",font='20',fg="black",bg="#64aacf").pack()
        passpara=Label(mysql_login,text="FILL ALL DETAILS TO PASS MYSQL PARAMETERS",bg="#ffffff",fg="green4").pack(side=TOP)
        notify_l=Label(mysql_login,text="Enter Your Password",font="10",bg="#ffffff",fg="#47d3a3").pack(side=BOTTOM,anchor="ne",padx=150)

        #FRAMES AND LABELS
        mysql_entry_frame=Frame(mysql_login,bg="#ffffff")
        mysql_entry_frame.pack(side=LEFT)
        hostlabel=Label(mysql_entry_frame , text="HOSTNAME :",font="20",bg="#ffffff",fg="SpringGreen2").grid(row=0,column=0)
        userlabel=Label(mysql_entry_frame , text="USERNAME :" ,font="20",bg="#ffffff",fg="SpringGreen2").grid(row=1,column=0)
        passwdlabel=Label(mysql_entry_frame , text="PASSWORD :"  ,font="20",bg="#ffffff",fg="red").grid(row=2,column=0)            

        #ENTRY FIELD VALUE CLASS
        
        from self import entrydefault       #default values
        global hostvalue,myuservalue,passvalue
        hostvalue=entrydefault.StringVar2()
        myuservalue=entrydefault.StringVar1()
        passvalue=StringVar()

        #ENTRY FIELD 
        hostentry=Entry(mysql_entry_frame , textvariable=hostvalue,bg="light cyan1").grid(row=0,column=1)
        userentry=Entry(mysql_entry_frame , textvariable=myuservalue,bg="light cyan1").grid(row=1,column=1)
        passwdentry=Entry(mysql_entry_frame , show="*",textvariable=passvalue,bg="coral2").grid(row=2,column=1)
        
        
        
        
        butframe=Frame(mysql_login,bg="#ffffff")
        butframe.pack(side=RIGHT,fill="y")
        button_image=PhotoImage(file="img_load//butimg.png")
        connect_button=Button(butframe,image=button_image,relief=FLAT,borderwidth=2,highlightthickness=0,highlightbackground="#ffffff",command=connectdb)
        connect_button.pack(side=RIGHT,padx=10)

        connect_button.config(bd=0)

        mysql_login.mainloop()
        
    def logs():
        global log
        log=0

        
        login=Tk()
        login.config(bg=bg)
        login.title("Bmax")
        login.call('wm', 'iconphoto', login._w, PhotoImage(file='img_load\\smalllogo.png'))
        login.geometry("400x500+450+100")
        login.maxsize(400,500)
        login.minsize(400,500)
        userimg=PhotoImage(file="img_load\\user.png")
        user_=Label(login,image=userimg,bg=bg)
        user_.pack()
        global username,user
        user=StringVar()
        username=placeholder.Entry1(login,"        Username","#58c3c3",textvariable=user,font=10,width=17,relief=FLAT,fg="#58c3c3",bg="#404040")
        username.place(relx=0.33,rely=0.424)

        passwd=StringVar()
        passval=placeholder.Entry1(login,"","#58c3c3",show="*",textvariable=passwd,font=10,width=17,relief=FLAT,fg="#58c3c3",bg="#404040")
        passval.place(relx=0.33,rely=0.543)


        hl2=Label(login,text="Password",fg="#58c3c3",bg="#404040",font=10,relief=FLAT,width=10)
        hl2.place(relx=0.39,rely=0.54)

        def hide(e):
            hl2.config(text="",bd=0,borderwidth=0)
            passval.focus()
        hl2.bind("<Button-1>",hide)
        def ac(e):
            hl2.config(text="",bd=0,borderwidth=0)
            hl2.place_forget()

        def bc(e):
            if len(passwd.get())==0:
                hl2.place(relx=0.39,rely=0.545)
                hl2.config(text="Password")    
            else:
                pass
            
               

        passval.bind("<FocusIn>",ac)
        passval.bind("<FocusOut>",bc)

        sinup_page=Label(login,text="reopen and sign up ",bg=bg,fg="red",relief=FLAT,height=1,activebackground=bg,bd=0)
        sinup_page.place(relx=0.5,rely=0.844)
        

        def login_():       
           logu=0
           logp=0
           
           if user.get()=="":
               labelstatus.config(text="     Invalid Username",fg="#ec5959")
           elif user.get()=="        Username":
               labelstatus.config(text="     Invalid Username",fg="#ec5959")
           else:
               loginuser=user.get()
               logu=1
           if logu==1:
               if passwd.get()=="":
                   labelstatus.config(text="     Invalid Password",fg="#ec5959")
               elif passwd.get()=="                     Password":
                   labelstatus.config(text="     Invalid Password",fg="#ec5959")
               else:
                   loginpass=passwd.get()
                   logp=1
               if logp==1:
                   data.log_txt(loginuser,loginpass,labelstatus)
                   if labelstatus['text']=="      LOGIN SUCESS":
                       
                       global log,username1,password1
                       log=100
                       username1=loginuser
                       password1=loginpass
                       login.after(500, lambda:login.destroy()) 
                       

        proimg=PhotoImage(file="img_load\\submit.png")
        pro=Button(login,image=proimg,bd=0,command=login_,bg=bg,activebackground=bg)
        pro.place(rely=0.65,relx=0.37)

        def ent(e):
            pro2=PhotoImage(file="img_load\\submitaf.png")
            pro["image"]=pro2
            pro.image=pro2
        def exi(e):
            pro["image"]=proimg
            pro.image=proimg
        pro.bind("<Enter>",ent)
        pro.bind("<Leave>",exi)

        labelstatus=Label(login,bd=0,bg=bg,fg="#ec5959")
        labelstatus.place(relx=0.37,rely=0.97)



        

        login.mainloop()
    
    def sign():                                  # SIGNUP PAGE INTERFACE 
        
        sin=Tk()
        sin.config(bg=bg)
        sin.title("Bmax")
        sin.call('wm', 'iconphoto', sin._w, PhotoImage(file='img_load\\smalllogo.png'))
        sin.geometry("400x530+450+100")
        sin.maxsize(400,530)
        sin.minsize(400,530)
        
        
        sinupimg=PhotoImage(file="img_load\\sinup.png")
        sinup=Label(sin,image=sinupimg)
        sinup.pack()

        
        
        
    
        username=StringVar()
        password=StringVar()
        height=variable.IntVar_for_height_and_weight()
        weight=variable.IntVar_for_height_and_weight()
        newname=placeholder.Entry1(sin,"         Username","#58c3c3",textvariable=username,font=10,width=17,relief=FLAT,fg="#58c3c3",bg="#404040")
        newpass=placeholder.Entry1(sin,"","#58c3c3",show="*",textvariable=password,font=10,width=17,relief=FLAT,fg="#58c3c3",bg="#404040")


        hl=Label(sin,text="Password",fg="#58c3c3",bg="#404040",font=10,relief=FLAT,width=17)
        hl.place(relx=0.337,rely=0.382)

        def hide(e):
            hl.config(text="",bd=0,borderwidth=0)
            newpass.focus()
        hl.bind("<Button-1>",hide)
        def ac(e):
            hl.config(text="",bd=0,borderwidth=0)
            hl.place_forget()

        def bc(e):
            if len(password.get())==0:
                hl.place(relx=0.33,rely=0.382)
                hl.config(text="Password")    
            else:
                pass
            
               

        newpass.bind("<FocusIn>",ac)
        newpass.bind("<FocusOut>",bc)       

        
         
        gendervalue=IntVar()
        def clicked():
            global gender  
            if gendervalue.get()==1:
                gender="Male"
            elif gendervalue.get()==2:
                gender="Female"
            else:
                pass
        r1=Radiobutton(sin,variable=gendervalue,value=1,height=1,relief=FLAT,activebackground="#404040",activeforeground=bg,command=clicked,selectcolor=bg,bg="#404040",fg="white").place(relx=0.26,rely=0.472)
        r2=Radiobutton(sin,variable=gendervalue,value=2,height=1,relief=FLAT,activebackground="#404040",activeforeground=bg,command=clicked,selectcolor=bg,bg="#404040",fg="white").place(relx=0.58,rely=0.472)

       
        weight1=placeholder.Entry1(sin,"Weight","#58c3c3",font="3",textvariable=weight,relief=FLAT,width=7,bg="#404040")
        height1=placeholder.Entry1(sin,"Height","#58c3c3",font="3",textvariable=height,relief=FLAT,width=7,bg="#404040")

        
        def hide():
            if hidevalue.get()==1:
               height1['state']='disabled'
               height1['disabledbackground']="black"
               weight1['state']='disabled'
               weight1['disabledbackground']="black"
            else:
               weight1['state']='normal'
               height1['state']='normal'
               
        hidevalue=IntVar()
        c0=Checkbutton(sin,font=2,variable=hidevalue,width=1,relief=FLAT,activebackground="#404040",command=hide,selectcolor=bg,fg="#58c3c3",bg="#404040").place(relx=0.668,rely=0.595)

        weight1.place(relx=0.305,rely=0.56)
        height1.place(relx=0.305,rely=0.64)
        newname.place(relx=0.34,rely=0.2945)
        newpass.place(relx=0.34,rely=0.382)

        def inbut(e):
            sinlogo2=PhotoImage(file="img_load\\sinlogoaf.png")
            sinbut["image"]=sinlogo2
            sinbut.image=sinlogo2
        def outbut(e):
            sinbut["image"]=sinlogo
            sinbut.image=sinlogo

        

        def confir_start():
            next1=0
            c="#ec5959"

            no_password_entered=0                    #Default variable value of Password entery if leaved blank
            no_user_name_entered=0                   #Default variable value of Username entery if leaved blank 

            if username.get()=="         Username":
                no_user_name_entered=1
                sl.config(text="Invalid Username",fg=c)                    #Label change when user name is invalid
            elif username.get()=="":
                no_user_name_entered=1
                sl.config(text="Invalid Username",fg=c)                    #Label change when user name is invalid
            else:
                uvalue=username.get()                                                         #Username is assined by uvalue
                next1=1


            if next1==1:                                                                       #if Username entry is satisfied
                if password.get()=="         Password":                        
                    no_password_entered=1
                    sl.config(text="Invalid Password")                         #if Password is not entered
                elif password.get()=="":                                                      #if Password is not entered
                    no_password_entered=1
                    sl.config(text="Invalid Password",fg=c)

                else:
                    pvalue=password.get()                                                     #Password is assined by pvalue
                    pass

                if no_user_name_entered==1:                      
                    pass
                elif no_password_entered==1:                                                    #No need
                    pass                                                                        #------
                else:                                                                           #------
                    g=0                                                                         #default gender not satisfied
                    try: 
                        if gender =="Male":                                                     #if gender = Male that g=1(gender is satisfied)
                            g=1
                            pass
                        elif gender=="Female":        
                            g=1                                                                 #if gender = Female that g=1(gender is satisfied)
                            pass
                    except NameError :
                        sl.config(text="Select Your Gender",fg=c)              #Label will change if gender not selected
                
                    if g==0:                                                                    #if gender value is not satisfied
                        sl.config(text="Select Your Gender",fg=c)              #Label will change if gender not selected
                       
                       
                    elif g==1:                                                  #if gender value is satisfied
                        all_done=0                                              #first stage of condition satisfied
                        h=1                                                     #default height value if not given
                        w=1                                                     #default weight value if not given
                        if hidevalue.get()==0:
                            try:
                                h=int(height.get())                                                #if height enter is 0
                                if h==0:
                                    sl.config(text="Height can not be 0",fg=c)
                                elif h=="":                                                        #if height is null          
                                    sl.config(text="Helight column is empty",fg=c)
                                else:
                                    all_done=1
                                   
                            except ValueError:                                                        #if height condition is not satisfied                     
                                sl.config(text="Invalid Height",fg=c)
                            except:
                                sl.config(text="Invalid Height",fg=c)              #             =======
                               
                            if all_done==1:                                                           #if height condition is satisfied
                                try:
                                    w=int(weight.get())
                                    if w==0:                                                          #check for weight=0
                                        sl.config(text="Weight can not be 0",fg=c)
                                    elif w=="":                                                       #check for weight=null
                                        sl.config(text="Weight column is empty",fg=c)
                                    else:
                                        all_done=2
                                       
                                       
                                except ValueError:
                                    sl.config(text="Invalid Weight",fg=c)          #if weight entry not satisfied
                                except:                                                               #if weight entry not satisfied
                                    sl.config(text="Invalid Weight",fg=c)
                        elif hidevalue.get()==1:                                                      #all condition satisfied
                            all_done=2
                        if all_done==2:
                            data.sinuptxt(uvalue,pvalue,gender,sl,h,w)


        sinlogo=PhotoImage(file="img_load\\sinlogo.png")
        sinbut=Button(sin,image=sinlogo,bg=bg,bd=0,relief=FLAT,command=confir_start,activebackground="#2b2b2b")
        sinbut.place(relx=0.37,rely=0.73)

        sinbut.bind("<Enter>",inbut)
        sinbut.bind("<Leave>",outbut)

        gotolog=Button(sin,text="Log in here",bg=bg,relief=FLAT,fg="red",activebackground=bg,bd=0,command=sin.destroy)
        gotolog.place(relx=0.67,rely=0.919)


        def enter_key(e):
            confir_start()
        sin.bind('<Return>',enter_key)

        sl=Label(sin,bg=bg)
        sl.place(relx=0.39,rely=0.964)

        sin.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def values(username):
    file=open("self\\source\\sinup.txt","r")
    f=file.readlines()
    l1=[]
    l2=[]
    for x in f:
        x=x.split("\n")
        l1.append(x)

    for y in l1:
        for t in y:
            if t=="":
                pass
            else:
                l2.append(t)
    length=len(l2)
    for y in range(0,length,7):
        valadd=(l2[y])
        if valadd==username:
            global gender1,height1,weight1,tod,tot
            gender1=(l2[y+2])
            height1=(l2[y+3])
            weight1=(l2[y+4])
            tod=(l2[y+5])
            tot=(l2[y+6])
 
    file.close()
def bmii(weight,height,bmilab_,bmicon):
    weight3=int(height)
    height3=int(weight)
    global bmi
    bmi = height3/((weight3/100)**2)
    bmi=int(bmi)
    bmilab_.config(text=(str(bmi)))
    if ( bmi < 16):
       bmicon.config(text="severely underweight")
    elif ( bmi >= 16 and bmi < 18.5):
       bmicon.config(text="    underweight",fg="#39b33f")  
    elif ( bmi >= 18.5 and bmi < 25):
       bmicon.config(text="        Healthy",fg="#7dd556")    
    elif ( bmi >= 25 and bmi < 30):
       bmicon.config(text="    overweight",fg="#da355c")  
    elif ( bmi >=30):
       bmicon.config(text="severely overweight",fg="red")
    elif bmi=="invalid Bmi":
        bmicon.config(text="change your detail")



def history(listbox):
    
    f2=open(f"self\\source\\{username1}_catch.txt","r")
    frn=f2.readlines()
    l1=[]
    change=0
    leng=len(frn)
    for o in frn:
        if change<leng:
            ind=frn[change]
            ind=ind.split("\n")
            l1.append(ind[0])
        change +=3
    index=0
    for p in l1:
        listbox.insert(index,p)
        index +=1
        
def add_temp(q,listbox):
    listbox.insert(END,q)



def catch_data(username1,q):
    try:
        now= datetime.datetime.now()
        tod=(now.strftime("%Y-%m-%d"))
        tot=(now.strftime("%H:%M:%S"))
    except:
        tod="----"
        tot="----"
    path=(f"self\\source\\{username1}_catch.txt")
    filed_=open(path,"a+")
    if q=="":
        pass
    else:
        filed_.write(q)
        filed_.write("\n")
        filed_.write(tod)
        filed_.write("\n")
        filed_.write(tot)
        filed_.write("\n")
        filed_.close()
        

        
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()




class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       
       global genderimg,bg_,editpro1,bglabel
       
       editpro1=PhotoImage(file="img_load\\edit.png")
       
       pink="#ea517c"
       u=username1.capitalize()
       p="*"*len(password1)
       bg2_=PhotoImage(file="img_load\\bg2.png")
       bglabel=Label(self,image=bg2_,bg=bg)
       bglabel.place(relx=0,rely=0)
       
       if gender1=="Male":
           genderimg=PhotoImage(file="img_load\\user_m.png")
       elif gender1=="Female":
           genderimg=PhotoImage(file="img_load\\user_f.png")
       

       photo=Label(self,image=genderimg,bg="#333333")
       photo.place(relx=0.06,rely=0.25)

       lname=Label(self,text=f"{u}",bg="#333333",fg=pink,font=("Helvetica", 25))
       lname.place(relx=0.18,rely=0.38)

       
       passwd=Label(self,text=f"{p}",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
       passwd.place(relx=0.19,rely=0.56)

       gendern=Label(self,text=f"{gender1}",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
       gendern.place(relx=0.19,rely=0.64)

       weightn=Label(self,text=f"{weight1} KG",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
       weightn.place(relx=0.19,rely=0.72)

       heightn=Label(self,text=f"{height1} CM",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
       heightn.place(relx=0.18,rely=0.8)


       def editit():

           def destroy():
               from self import username_delete
               username_delete.deletion(user.get())
               
               
    
               print(tmsg.showinfo("Software-plot","Account Deleted"))
               edpro.destroy()
               root.destroy()
               
                   
                   
                   
                   
           edpro=Toplevel()
           edpro.title("Edit")
           edpro.geometry("455x446")
           edpro.minsize(455,446)
           edpro.maxsize(455,446)
           global imagebg, e

           e=PhotoImage(file="img_load\\edprosa.png")
           imagebg=PhotoImage(file="img_load\\editit.png")
           labelimg=Label(edpro,image=imagebg,bd=0)
           labelimg.pack()
           
           passwd=Label(edpro,text=f"{p}",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
           passwd.place(relx=0.45,rely=0.48)

           gendern=Label(edpro,text=f"{gender1}",bg="#3b3b3b",fg=pink,font=("Helvetica", 18))
           gendern.place(relx=0.45,rely=0.59)

           l=Label(edpro,bg="#333333")
           l.place(relx=0.2,rely=0.06)

           
           weightn=Label(edpro,text=f"{weight1}",bg="#3b3b3b",fg="red",font=("Helvetica", 10),relief=FLAT)
           weightn.place(relx=0.42,rely=0.71)
           
           heightn=Label(edpro,text=f"{height1}",bg="#3b3b3b",fg="red",font=("Helvetica", 10),relief=FLAT)
           heightn.place(relx=0.42,rely=0.8)

           editprosav=Button(edpro,image=e,bg="#333333",bd=0,relief=FLAT,activebackground="#333333",command=destroy)
           editprosav.place(relx=0.78,rely=0.603)  

               
       editprofile=Button(self,image=editpro1,bg="#333333",bd=0,relief=FLAT,activebackground="#333333",command=editit)
       editprofile.place(relx=0.315,rely=0.66)

       
           
       global hislabel
      
       def hislabel():

            try:
                global listbox,bg_,item,datelab,timelab
                f2=open(f"self\\source\\{username1}_catch.txt","r")
                bg_=PhotoImage(file="img_load\\bg1.png")
                bglabel["image"]=bg_

                hisframe=Frame(self,bd=0)
                hisframe.place(relx=0.48,rely=0.33)

                framep=Frame(hisframe,bd=0,height=260,width=200)
                framep.pack(fill="both")
                framep.pack_propagate(0)
                #listscroll=Scrollbar(framep)              #scrollbar
                anys=StringVar()
                listbox=Listbox(framep,height=25,listvariable=anys,fg="white",bg="#333333",relief=FLAT,bd=0)
                
                item=Label(self,bg="#3b3b3b",text="Select from listbox")
                item.place(relx=0.76,rely=0.4)
                datelab=Label(self,text="----",bg="#3b3b3b")
                datelab.place(relx=0.8,rely=0.51)
                timelab=Label(self,text="----",bg="#3b3b3b")
                timelab.place(relx=0.8,rely=0.63)
           
                #listscroll.config(command=listbox.yview)      #scrollbar config
                #listscroll.pack(fill="y",side="right")
                listbox.pack(fill="both",side="top")

                l2=[]
                l3=[]
                def CurSelet(evt):
                    f2=open(f"self\\source\\{username1}_catch.txt","r")
                    frn=f2.readlines()
                    for new in frn:
                        ad=new.split("\n")
                        l2.append(ad)
                    for r in l2:
                        ze=r[0]
                        l3.append(ze)
                    global values
                    value=str((listbox.get(listbox.curselection())))
                    inded=l3.index(listbox.get(listbox.curselection()))
                    item.config(text=value,font=("Helvetica", 18))
                    datelab.config(text=l3[inded+1],font=("Helvetica", 18))
                    timelab.config(text=l3[inded+2],font=("Helvetica", 18))


                history(listbox)
                listbox.bind('<<ListboxSelect>>',CurSelet)

            except FileNotFoundError:
                global bg2
                bg2=PhotoImage(file="img_load\\bg2.png")
                bglabel["image"]=bg2
               
        
               
       hislabel()

       acd=Label(self,text="Account created on (Date) "+tod,bg=bg,font=("Helvetica", 10),fg="grey")
       acd.place(relx=0.73,rely=0.86)
       act=Label(self,text="Account created on (Time) "+tot,bg=bg,font=("Helvetica", 10),fg="grey")
       act.place(relx=0.73,rely=0.9)
        
       
       
       
       
    
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       global sbg,frame_,sugframe,slabel

       sbg=PhotoImage(file="img_load\\sugg.png")
       slabel=Label(self,image=sbg,bg=bg)
       slabel.place(relx=0,rely=0)

       sugframe=Frame(self,bd=0,bg=bg)
       sugframe.place(relx=0.8,rely=0.2)

       global toptxt

       toptxt=Label(self,bg=bg,font=("Helvetica", 20),fg="grey")
       toptxt.place(relx=0.01,rely=0.08)

       frame_=Frame(self,bd=0,bg="grey",height=400,width=1200)
       

       frame5=Frame(frame_,height=400,width=1200,bg="grey")
       frame5.pack()
       frame5.pack_propagate(0)

       
       global text1,sbar
       #sbar=Scrollbar(frame5)
       #sbar.pack(side=RIGHT,fill=Y)
       
       fg2="#34658e"
       text1=Text(frame5,width=1200,height=400,wrap=WORD,bg=bg,fg='white',padx=10,pady=5,font="TimesNewRoman",relief=FLAT)
       text1.pack(side=LEFT)


       

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global hbg,helth_img

       hbg=PhotoImage(file="img_load\\health.png")
       hlabel=Label(self,image=hbg,bg=bg)
       hlabel.place(relx=0,rely=0)

       weightn2=Label(self,text=f"{weight1} KG",bg="#333333",font=("Helvetica", 28),fg="#2a92b4")
       weightn2.place(relx=0.13,rely=0.54)

       heightn2=Label(self,text=f"{height1} CM",bg="#333333",font=("Helvetica", 28),fg="#2a92b4")
       heightn2.place(relx=0.12,rely=0.3)

       
       bmilab=Label(self,bg="#333333",font=("Helvetica", 29),fg="#2a92b4")
       bmilab.place(relx=0.38,rely=0.397)

       bmicon=Label(self,bg="#616059",font=("Helvetica", 20),fg="#2a92b4")
       bmicon.place(relx=0.23,rely=0.765)

       bmii(weight1,height1,bmilab,bmicon)


       cl=Label(self,bg="#212121",font=("Helvetica", 14),fg="grey")
       cl.place(relx=0.61,rely=0.45)

       def doctype():
           os.system('self\\doctor_pre.py')


       helth_img=PhotoImage(file="img_load\\health_img.png")
       helth_lab=Label(self,image=helth_img,bd=0,relief=FLAT,bg=bg)
       helth_lab.place(relx=0.61,rely=0.8)
           
       health=Button(self,text="Don't Know Which Doctor to visit!? \nclick here to know more",bg=bg,fg="grey",font=("Helvetica", 10),bd=0,relief=FLAT,activebackground
                     =bg,command=doctype)
       health.place(relx=0.68,rely=0.83)

       #doc_type=Label(self,text="which doctor to visit in different conditions?").place(relx=0.1,rely=0.7)

       #al=Label(self,bg="#212121",font=("Helvetica", 14),fg="grey")
       #al.place(relx=0.78,rely=0.46)

       #dl=Label(self,bg="#212121",font=("Helvetica", 14),fg="grey")
       #dl.place(relx=0.78,rely=0.55)

       #rl=Label(self,bg="#212121",font=("Helvetica", 14),fg="grey")
       #rl.place(relx=0.78,rely=0.63)

       #covid_update.update(cl,al,dl,rl)
       from self import time_upd
       time_upd.routine(cl)
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global fudo,exer_bu

       fudo=PhotoImage(file="img_load\\fudo.png")
       f_b=Label(self,image=fudo,bd=0).pack()

       text_d=Text(self, height=20, width=70,wrap=WORD,font="ArialRoundedMT...  15",relief=FLAT,bg=bg,fg="white")
       text_d.insert(END,food_and_diet.reqcalories(int(height1),int(weight1),int(startmode.readmode_age(username1)),gender1,int(startmode.readmode_mode(username1)))+"\n\n\nNote: Your diet plan and fitness plan is based on your given data,so please make sure it’s right.")
       text_d.configure(state='disabled')
       text_d.place(relx=0.01,rely=0.27)

       exer_bu=PhotoImage(file="img_load\\exer_but.png")
       reco=startmode.readmode_mode(username1)
       

       def fitgo():

           import sys
           sys.path.append("self\\fitness_")
           import fitness
           fitness.openfile(reco)
           
        
    
       but_exer=Button(self,image=exer_bu,bd=0,bg=bg,command=fitgo,activebackground=bg,relief=FLAT)
       but_exer.place(relx=0.68,rely=0.6)
       exer=animations.AnimatedGIF(self, "img_load\\exer.gif")
       exer.config(bd=0,bg=bg)
       exer.place(relx=0.85,rely=0.52)
       
       
       

       


    
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global p1,p2,p3
        p1 = Page1(self,bg=bg)
        p2 = Page2(self,bg=bg)
        p3 = Page3(self,bg=bg)
        p4 = Page4(self,bg=bg)


        
        container = tk.Frame(self,bd=0,highlightthickness=0,bg=bg)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=2, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=2, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=2, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=2, relwidth=1, relheight=1)
        

        

# MAIN FRAME OF ALL PAGES

        global bar,search,buts,pro,home,sp,barmen,menubar,markerimg,covid_img,covid_d

#------------COVID INFORMATION-----------------
        
        covid_img=PhotoImage(file="img_load\\covid_but.png")
        covid_d=PhotoImage(file="img_load\\covid _dis.png")
        def data_rec():
            global total,active,cured,death,state_
            f=open("self\\source\\state_app.txt",'r')
            state_=str(f.read())
            f.close()
           
            
            co_data=states.getdata(state_)
            
            active=co_data['Active']
            cured=co_data['Cured']
            death=co_data['Death']
            total=active+cured+death
        data_rec()
            

        def curin(e):
            
            covid_disp.place(relx=0.66,rely=0.19)
            c_state.place(relx=0.74,rely=0.21)
            c_total.place(relx=0.73,rely=0.276)
            c_active.place(relx=0.73,rely=0.327)
            c_cured.place(relx=0.73,rely=0.376)
            c_death.place(relx=0.73,rely=0.427)
            
            c_state.config(text=state_)
            c_total.config(text=total)
            c_active.config(text=cured)
            c_cured.config(text=active)
            c_death.config(text=death)
            

            
        def curout(e):
            covid_disp.place_forget()
            c_state.place_forget()
            c_total.place_forget()
            c_active.place_forget()
            c_cured.place_forget()
            c_death.place_forget()
            
        covid_disp=Label(root,image=covid_d,bd=0)

        covid_lab=Button(root,image=covid_img,bd=0,bg="#2b2b2b",activebackground="#2b2b2b",relief=FLAT,command=data_rec)
        covid_lab.place(relx=0.9,rely=0.17)

        
        bbl='#232323'

        c_state=Label(root,text="------------------",bg="#484848",fg="#eff120",font='10')
        c_total=Label(root,text="------------------",bg=bbl,fg="white",font='10')
        c_active=Label(root,text="------------------",bg=bbl,fg="white",font='10')
        c_cured=Label(root,text="------------------",bg=bbl,fg="white",font='10')
        c_death=Label(root,text="------------------",bg=bbl,fg="white",font='10')
        

        covid_lab.bind("<Enter>",curin)
        covid_lab.bind("<Leave>",curout)
#---------------COVID INFO ENDS---------------------      
        
        def pone():
            p1.show()
            
        def ptwo():
            p2.show()
            
        def pthree():
            p3.show()
        def pfour():
            p4.show()
            
       
        

        barframe=Frame(root,bd=0)
        barframe.pack()

        bar=PhotoImage(file="img_load\\bar.png")
        barlabel=Label(barframe,image=bar,bg=bg)
        barlabel.pack()

        buts=PhotoImage(file="img_load\\buts.png")
        #search=PhotoImage(file="img_load\\search.png")

        #search_box=Label(root,image=search,bg="#3f3f3f")
        #search_box.place(relx=0.15,rely=0.01)

        

#--------------------- SEARCH
        def searchit():
            
            global q
            q=searched.get()
            p2.show()
            search_script.search(q,text1,root)
            catch_data(username1,q)
            try:
                item.place_forget()
                datelab.place_forget()
                timelab.place_forget()
            except NameError:
                pass
            hislabel()
            problem.request(q,text1)
            slabel.place_forget()
            frame_.place(relx=0.02,rely=0.28)
            toptxt.config(text="Search Results for: "+q)
            
            
            
            

        sbut=Button(barframe,image=buts,bg="#3f3f3f",relief=FLAT,bd=0,activebackground="#424040",command=searchit)
        sbut.place(relx=0.855,rely=0.27)
        def searchit1(e):
            searchit()
        searched=StringVar()
        enter=placeholder.Entry1(barframe,"Enter your problem","White",width=47,font="90",bg="#424040",relief=FLAT,textvariable=searched,fg="white")
        enter.place(relx=0.49,rely=0.37)
        enter.bind("<Return>",searchit1)
#----------------------        

        

        framebar=Frame(root,bd=0,bg="#24252a")
        framebar.place(relx=0.08,rely=0.04)

        home=PhotoImage(file="img_load\\home.png")
        homebut=tk.Button(framebar,image=home,bg="#24252a",relief=FLAT,command=ptwo,activebackground="#24252a",bd=0)
        homebut.pack(padx=5,side=LEFT)

        
        pro=PhotoImage(file="img_load\\pro.png")
        probutton=tk.Button(framebar,image=pro,bg="#24252a",relief=FLAT,command=pone,activebackground="#24252a",bd=0)
        probutton.pack(padx=20,side=LEFT)

        

        
        sp=PhotoImage(file="img_load\\sp.png")
        spbut=tk.Button(framebar,image=sp,bg="#24252a",relief=FLAT,command=pthree,activebackground="#24252a",bd=0)
        spbut.pack(padx=5,side=LEFT)

        well=PhotoImage(file="img_load\\well-being.png")
        wellbeing=tk.Button(framebar,image=well,bg="#24252a",relief=FLAT,command=pfour,activebackground="#24252a",bd=0)
        wellbeing.pack(padx=23,side=LEFT)

        
        
        
        def profile(e):
            global proaf
            proaf=PhotoImage(file="img_load\\proaf.png")
            probutton["image"]=proaf
            probutton.image=proaf
        def profileforget(e):
            probutton["image"]=pro
            probutton.image=pro
            
        probutton.bind("<Enter>",profile)
        probutton.bind("<Leave>",profileforget)

        def homeent(e):
            global homeaf
            homeaf=PhotoImage(file="img_load\\homeaf.png")
            homebut["image"]=homeaf
            homebut.image=homeaf
            
        def homeforget(e):
            homebut["image"]=home
            homebut.image=home
            
        homebut.bind("<Enter>",homeent)
        homebut.bind("<Leave>",homeforget)

        def spent(e):
            global spaf
            spaf=PhotoImage(file="img_load\\spaf.png")
            spbut["image"]=spaf
            spbut.image=spaf
        def spforget(e):
            spbut["image"]=sp
            spbut.image=sp
            

        spbut.bind("<Enter>",spent)
        spbut.bind("<Leave>",spforget)

        def welin(e):
            global wellaf
            wellaf=PhotoImage(file="img_load\\well-beingaf.png")
            wellbeing['image']=wellaf
        def welout(e):
            wellbeing['image']=well
        wellbeing.bind("<Enter>",welin)
        wellbeing.bind("<Leave>",welout)

        p2.show()  

        

        

        
if __name__=="__main__":

    
    
    interface.sign()
    interface.logs()
    try:
        if (username1):
            interface.mysqlpage()
        else:pass
    except NameError:pass
    try:

        if startmode.search(username1)==False:
            mode=Tk()
            mode.geometry("300x200+500+200")
            mode.overrideredirect(1)
            mode.config(bg="white")
            mode.title("Bmax")
            mode.call('wm', 'iconphoto', mode._w, PhotoImage(file='self\\smalllogo.png'))
            what=Label(mode,text="Adjust your work type",bg="white")
            what.pack(pady=10)
            mm=IntVar()
            mm.set(2)
            def livechange(e):
                mode_val=mm.get()
                if mode_val==1:
                    info_mode.config(text="Low",fg="red")
                elif mode_val==2:
                    info_mode.config(text="Avg",fg="blue")
                elif mode_val==3:
                    info_mode.config(text="Intensive",fg="Green")
            def did_it():
                global mode_value_,age_val
                age_val=age_.get()
                mode_value_=mm.get()
                startmode.mode(mode_value_,username1,age_val)
                mode.destroy()
        
        
                
                
            mode_st=Scale(mode,bd=2,variable=mm,from_=1,to=3,orient=HORIZONTAL,relief=FLAT,command=livechange,bg="white")
            mode_st.pack()
            info_mode=Label(mode,text="Avg",fg="blue",bg="white")
            info_mode.pack(pady=10)
            age_lab=Label(mode,text="Age(more than 0 less than 80):",fg="black",bg="white").pack()

            age_=IntVar()
            age_.set(18)
            age_entry=Entry(mode,textvariable=age_,bd=0,bg='#1ea5b5')
            age_entry.pack()
            Done_but=Button(mode,text="Done",relief=FLAT,command=did_it)
            Done_but.pack()

            can_be=Label(mode,text="Don't Worry! Can be edited in future",bg="white").pack(pady=5)
            mode.mainloop()
        
    except NameError :
        print("Thanks for Choosing Bmax")
        
        
    if log==100:
        values(username1)
        root = tk.Tk()
        main = MainView(root)
        root.call('wm', 'iconphoto', root._w, PhotoImage(file='img_load\\smalllogo.png'))
        root.config(bg="#2b2b2b")
        root.title("BMAX")
        root.wm_geometry("1250x670+50+5")
        root.maxsize(800,500)
        root.minsize(1250,670)
        main.pack(side="top", fill="both", expand=True)

       # mymenu=Menu(root)
       # m1=Menu(mymenu,tearoff=False)
        

       # mymenu.add_cascade(label="File",menu=m1)
       # m1.add_command(label="Close")
       # m1.add_command(label="Exit")
       # root.config(menu=mymenu)
       
        root.mainloop()
