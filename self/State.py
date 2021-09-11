from tkinter import *
info=Tk()
info.geometry("300x100+400+300")
info.title("Information")


value=StringVar()
l1=Label(info,text="Enter Your State:").pack()

def done():
    d=0
    val=value.get()
    lst=[]
    f=open("source\\state.txt",'r')
    for x in f:
        s=x.split('\n')
        a=s[0]
        lst.append(a)
    f.close()

    for i in lst:
        
        if i.lower()==val:
            d=1
            val_need=i
        else:
            pass
    if d==1:
        f=open("source\\state_app.txt",'w')
        f.write(val_need)
        f.close()
        print("Done and Applied")
    else:print("State Not Found")

    
    
e1=Entry(info,textvariable=value).pack(pady=5)
b1=Button(info,text="Done",bd=0,bg="blue",command=done).pack()
info.mainloop()

