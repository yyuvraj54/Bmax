import csv
element=[]
data=[]
with open('self\\source\\dname.txt',"r") as f:
    for x in f:
        x=x.split("\n")
        y=x[0]
        data.append(y)
    length=len(data)
    for i in range(1,length,4):
        element.append(data[i])
    #print(data)


def request(n,text):
    c=0
    if n=="":
        pass
    else:
        for a in data:
            
            if a==n:
                ind=data.index(a)
                name=data[ind]
                remedy=data[ind+1]
                med=data[ind+2]
                c=1
                if len(med)==0:
                    med=("ask doctor")
                break
            else:
                c=0
        if c==1:
            text.insert(1.0,"According to Bmax" + "\n" +name + "\n"+"remedy:"+ remedy +"\n"+"medicines:"+med+"\n\n")        
        else:
            text.insert(1.0,"According to Bmax \nNo data found\n\n")
        

        
    
        
    
    
