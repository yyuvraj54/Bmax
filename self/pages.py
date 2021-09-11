from tkinter import *
bg="#2b2b2b"

class set1():
    def page2(page):
        def off():
            page.destroy()

        global dev,nextaf
        dev=PhotoImage(file="img_load\\dpage.png")
        devlab=Label(page,image=dev,bd=0)
        devlab.pack()
        nextaf=PhotoImage(file="img_load\\nextaf.png")
        exitbut=Button(page,image=nextaf,command=off,bg="#353535",activebackground="#353535",bd=0)
        exitbut.place(relx=0.75,rely=0.87)
    def page1():
        def nextpage():
            aboutlabel.place_forget()
            set1.page2(page)
            nextbut.place_forget()
        def next_enter(e):
            nextaf=PhotoImage(file="img_load\\nextaf.png")
            nextbut["image"]=nextaf
            nextbut.image=nextaf
        def next_leave(e):
            nextbut["image"]=next_
            nextbut.image=next_         
        page=Tk()
        page.title("Bmax")
        page.geometry("800x540+390+100")
        page.maxsize(800,540)
        page.minsize(800,540)
        page.config(bg=bg)
        page.call('wm', 'iconphoto', page._w, PhotoImage(file='img_load\\smalllogo.png'))


        about=PhotoImage(file="img_load\\about.png")
        aboutlabel=Label(page,image=about,bd=0)
        aboutlabel.place(relx=0,rely=0)
        

        next_=PhotoImage(file="img_load\\next.png")
        nextbut=Button(page,image=next_,bg="#10554e",bd=0,command=nextpage,relief=FLAT,highlightthickness=0,activebackground="#10554e")
        nextbut.place(relx=0.5,rely=0.87)
        nextbut.bind("<Enter>",next_enter)
        nextbut.bind("<Leave>",next_leave)

        page.mainloop()








if __name__=="__main__":
    set1.page1()
