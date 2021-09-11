def mode(m,user,age):
    f=open("self\\source\\openmode.txt","a")
    f.write(user)
    f.write('\n')
    f.write(str(m))
    f.write('\n')
    f.write(str(age))
    f.write('\n')
    f.close()
def readmode_mode(user):
    l1=[]
    f=open("self\\source\\openmode.txt","r")
    d=f.readlines()
    for x in d:
        x=x.split("\n")
        x=x[0]
        l1.append(x)
    for y in l1:
        if user == y:
            index=l1.index(y)
            return (l1[index+1])
def readmode_age(user):
    l1=[]
    f=open("self\\source\\openmode.txt","r")
    d=f.readlines()
    for x in d:
        x=x.split("\n")
        x=x[0]
        l1.append(x)
    for y in l1:
        if user == y:
            index=l1.index(y)
            return (l1[index+2])

    f.close()
def update_m(user,m_new):
    l1=[]
    f=open("self\\source\\openmode.txt","r+")
    d=f.readlines()
    for x in d:
        x=x.split("\n")
        x=x[0]
        l1.append(x)
   
    for y in l1:
        if user == y:
            index=l1.index(y)
            index=index+1
            l1[index]=m_new
            
        f.truncate(0)
        f.seek(0)
        for l in l1:
            l=str(l)
            f.write(l)
            f.write("\n")
    f.close()
def update_age(user,new_age):
    l1=[]
    f=open("self\\source\\openmode.txt","r+")
    d=f.readlines()
    for x in d:
        x=x.split("\n")
        x=x[0]
        l1.append(x)
   
    for y in l1:
        if user == y:
            index=l1.index(y)
            index=index+2
            l1[index]=new_age
            
        f.truncate(0)
        f.seek(0)
        for l in l1:
            l=str(l)
            f.write(l)
            f.write("\n")
    f.close()

def search(user):
    if readmode_mode(user)==None:
        return False
    else:
        return  True


