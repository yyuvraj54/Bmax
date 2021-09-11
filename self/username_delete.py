def deletion(e1):
    
    x=str(e1)
    x=x+'\n'
    f=open('self//source//sinup.txt','r')
    d=f.readlines()
    f.close()
    df=[]
    for i in range(len(d)//7):
        t=d[(i*7):(i+1)*7]
        df.append(t)
    for i in df:
        if i[0]==x:
            ind=df.index(i)
            df[ind]=[]
    w=''
    for i in df:
        for j in i:
            w=w+j
    f=open('self//source//sinup.txt','w')
    f.write(w)
    f.close()
