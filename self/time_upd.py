from datetime import datetime
from tkinter import *
def routine(l1):
    now=datetime.now().time()
    n=int((str(now))[0:2])
    if n==6:
        x='Its morning time, you should start of \n by doing exercise.'
    elif n==7:
        x='Nothing is more refreshing than a warm cup \n of tea. Hence make yourself a nice cup of tea.'
    elif n==8:
        x='It is time for breakfast. Have something with\nhigh carbohydrate content like cereal with milk\nor sandwitches to set you up for the day'
    elif n==11:
        x='Quite a time went by since breakfast, have a\nfruit and make your gut happy'
    elif n==13:
        x='Its lunch time now, have something with high\nprotien content like daals'
    elif n==17:
        x='Its been a while since lunch, have something\nwith high energy content snack\nlike dark cholate :D.'
    elif n==20:
        x='Its dinner time, have something low fat like a\nsoup with some vegetables.'
    elif n==21:
        x='Make yorself a ginger tea by boiling some\ncrushed ginger,cloves and tulsi (indian\nbasil) in water. It will enhance\nyour bodies metabolism.'
    else:
        x='Nothing for now. Keep following social\n distancing and also keep washing your\n hands regularly.'
    l1.config(text=x)

