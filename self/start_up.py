from tkinter import *
def boot_up():
    boot=Tk()
    boot.title("BMAX")
    boot.attributes("-fullscreen", 0.5)
    boot.attributes("-transparentcolor","#f0f0f0")
    img=PhotoImage(file="img_load\\boot_.png")
    label=Label(boot,image=img)
    label.pack(pady=120)
    boot.after(7000, lambda:boot.destroy()) 
    boot.mainloop()
if __name__=="__main__":
    boot_up()
