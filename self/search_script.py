from tkinter import *
try:
    from self import wikipedia
except ModuleNotFoundError:
    print("Module not found wikipedia")



def search(q,text,main):
    c=0
    
    try:
        lan['state']=NORMAL
    except:
        pass
    text.delete('1.0', END)
    if q=="":
        pass
    elif "Enter Your Problem"==q:
        pass 
    else:
        loading=Toplevel()
        photo = PhotoImage(file ="self\\smalllogo1.png")
        loading.iconphoto(False, photo)
        loading.geometry("1250x670+50+5")
        loading.title("Bmax")
        
        loading.attributes("-alpha",0.8)
        loading.config(bg="#464646")
        
        anima= PhotoImage(file="self\\smalllogo1.png")
        load=Label(loading,image=anima,bd=0,relief=FLAT)
        load.pack()
        c=0
        main.update()
        #wat on ent
#----language english-------
        try:
            global lang1
            wikipedia.set_lang("en")
            lang1=wikipedia.summary(q)
            c=1
        except wikipedia.exceptions.DisambiguationError as er:
            
            reff=str(er)
            
            text.insert(1.0,"According to Wikipedia \n|Similar Search Found|" + "\n" + "Can't Find Your Search, Available Page Refer Below (just copy and past the word you want to search)" + "\n" +"\n"+reff)
        
        except wikipedia.requests.exceptions.ConnectionError as er:
            
           
            text.insert(1.0,"According to Wikipedia \n|Connection Error|"+"\n"+"Check your internet connection")
            
        except wikipedia.exceptions.PageError as er:
            
            
            text.insert(1.0,"According to Wikipedia \n|Page Not Found Error|"+"\n"+"The page you looking for is not available")
            
        except:
            
            
            text.insert(1.0,"According to Wikipedia \n|Search Error|"+"\n"+"Something went wrong")

        if c==1:
            text.insert(1.0,"According to Wikipedia \n|Summary|"+"\n"+lang1)
        else:
            pass
        try:
            loading.destroy()
        except:
            pass



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

