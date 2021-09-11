import tkinter.messagebox as tmsg
import os
try:import mysql.connector
except:
    tmsg.showwarning("Software-plot"," 'mysql.connector' module not found please install to continue")
    modd=tmsg.askquestion("Software-plot", "Do you want to install 'mysql.connector'(module) through bmax?")
    if modd=="yes":
        os.system('python -m pip install mysql.connector')
        tmsg.showinfo("Software-plot","module downloaded successfully")
        import mysql.connector
    else:pass
    
d_name="bmax"    



def db_create(buser,hostvalues,myuservalue,passvalue):   #DATABASE CREATE (FIRST TIME)
    mydb=mysql.connector.connect(host=hostvalues,user=myuservalue,passwd=passvalue)
    mycur=mydb.cursor()
    mycur.execute(f'create database IF NOT EXISTS {d_name}')

def db_table_in(buser,hostvalues,myuservalue,passvalue):  #CREATE TABLE
    mydb=mysql.connector.connect(host=hostvalues,user=myuservalue,passwd=passvalue,database=f'{d_name}')
    mycur=mydb.cursor()
    mycur.execute('create table IF NOT EXISTS soft_run(name varchar(20) primary key,logged int(10))')


    
def db_insert_or_update(buser,hostvalues,myuservalue,passvalue,main):  #INSERT RECORD (FIRST TIME) UPDATE MULTIPLE TIMES
    try:
        mydb=mysql.connector.connect(host=hostvalues,user=myuservalue,passwd=passvalue,database=f'{d_name}')
        mycur=mydb.cursor()
        query=('insert into soft_run (name,logged)values(%s,%s)')
        values=(buser,1)
        mycur.execute(query,values)
        mydb.commit()
        main.destroy()
    except mysql.connector.errors.IntegrityError:
        mydb=mysql.connector.connect(host=hostvalues,user=myuservalue,passwd=passvalue,database=f'{d_name}')
        mycur=mydb.cursor()
        mycur.execute(f"SELECT logged from soft_run WHERE name='{buser}'")
        rec=mycur.fetchall()
        temp=1
        for i in rec:
            temp=temp+i[0]
        call="UPDATE soft_run SET logged=%s WHERE name =%s"
        val=(temp,buser)
        mycur.execute(call,val)
            
        #mycur.execute(f'UPDATE soft_run SET logged = logged+1 WHERE name = {buser}')
        #sql='Update soft_run set logged = logged+1 WHERE name = %s'
        #val =(buser)
        #mycur.execute(sql,val)
        mydb.commit()
        main.destroy()
    
    
def db_in_database(buser,hostvalues,myuservalue,passvalue):    # CHECK IF DATABASE ALREDY CREATED AND RETURN (True/False)
    mydb=mysql.connector.connect(host=hostvalues,user=myuservalue,passwd=passvalue)
    mycur=mydb.cursor()
    mycur.execute('show databases')
    for x in mycur.fetchall():
        if x[0] ==d_name:
            f=1
            break
        else:
            f=0
           
            pass
    if f==1:
        
        return True
    else:
        
        return False



        
        
    
    
