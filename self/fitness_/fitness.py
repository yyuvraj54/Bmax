from tkinter import *
from self import animations

def openfile(rec):
    
    global fitbar_,al,dp,ap,fp,pla1,pla2,pla3,pla4
    fit=Toplevel()
    #fit.call('wm', 'iconphoto', fit._w, PhotoImage(file='self\\smalllogo.png'))
    fit.geometry("1200x670+100+10")
    fit.maxsize(1200,670)
    fit.minsize(1200,670)
    fit.title("Bmax")
    fit.config(bg="#7accc8")
    fitbar_=PhotoImage(file="self\\fitness_\\bar_fit.png")
    fitbar=Label(fit,image=fitbar_,bd=0,bg="white")
    fitbar.pack()
    al=animations.AnimatedGIF(fit,"self\\fitness_\\run.gif")
    al.config(bd=0)
    al.place(relx=0,rely=0.05)

    def ex_pg():
        fitbar.pack_forget()
        al.place_forget()
        pl1.place_forget()
        pl2.place_forget()
        pl3.place_forget()
        pl4.place_forget()
        fit.config(bg="#f7f7f7")
        #fit.minsize(400,600)
        #fit.geometry("400x600")

    def _pl1():
        ex_pg()
        fit.minsize(800,470)
        fit.maxsize(800,470)
        fit.geometry("800x470+300+100")
        try:
            dp.destroy()
        except:pass
        dp=animations.AnimatedGIF(fit,"self\\fitness_\\daily.gif")
        dp.config(bd=0)
        dp.pack()

    def _pl2():
        ex_pg()
        fit.minsize(890,470)
        fit.maxsize(890,470)
        fit.geometry("800x470+280+100")
        try:
            fp.destroy()
        except:pass
        fp=animations.AnimatedGIF(fit,"self\\fitness_\\fat.gif")
        fp.config(bd=0)
        fp.pack()

    def _pl3():
        ex_pg()
        fit.minsize(790,370)
        fit.maxsize(790,370)
        fit.geometry("800x470+300+100")
        try:
            ap.destroy()
        except:pass
        ap=animations.AnimatedGIF(fit,"self\\fitness_\\dumble.gif")
        ap.config(bd=0)
        ap.pack()
    def _pl4():
        
        if int(rec)==1:
            _pl1()
        elif int(rec)==2:
            _pl2()
        elif int(rec)==3:
            _pl3()
        
        
    pla1=PhotoImage(file="self\\fitness_\\dp.png")
    pla2=PhotoImage(file="self\\fitness_\\fp.png")
    pla3=PhotoImage(file="self\\fitness_\\ap.png")
    pla4=PhotoImage(file="self\\fitness_\\rp.png")

   # disclab=Label(fit,text="Animation handling by: YUVRAJ SINGH YADAV \nData processing by:SHREYAS OM \nPOWERED BY PYTHON3"
    #              ,bg='white',fg='grey').place(relx=0.02,rely=0.7)
    

    bc="#f7941d"
    pl1=Button(fit,image=pla1,bd=0,bg=bc,command=_pl1)
    pl1.place(relx=0.5,rely=0.2)
    pl2=Button(fit,image=pla2,bd=0,bg=bc,command=_pl2)
    pl2.place(relx=0.7,rely=0.2)
    pl3=Button(fit,image=pla3,bd=0,bg=bc,command=_pl3)
    pl3.place(relx=0.5,rely=0.5)
    pl4=Button(fit,image=pla4,bd=0,bg=bc,command=_pl4)
    pl4.place(relx=0.7,rely=0.5)
    fit.mainloop()

