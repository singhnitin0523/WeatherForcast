from tkinter import *
import sense 
import backend
import numpy as np
s=np.zeros(3)

def search():
    s[0],s[1],s[2]=sense.senseread()
    e1.delete(0,END)
    e1.insert(END,str(s[0]))
    e2.delete(0,END)
    e2.insert(END,str(s[1]))
    e3.delete(0,END)
    e3.insert(END,str(s[2]))
    return s[0],s[1],s[2]
def pret():
    b,h,u=search()
    z=backend.preg(b,h,u)
    if z==1:
        T.insert(END, 'There Is A High Possibility Of Rain Today') 
    else:
        T.insert(END, 'There Is No Possibility Of Rain Today') 
        
window=Tk()

window.wm_title("Weather Predictor")

l1=Label(window,text="Weather Predictor",width=22,height=1,font=("Constantia", 44),bg='white')
l1.grid(row=0,column=0,rowspan=3,columnspan=4)

l2=Label(window,text="Temperature",font=("Calibri Light",20))
l2.grid(row=3,column=0)
l3=Label(window,text="Humidity",font=("Calibri Light",20))
l3.grid(row=4,column=0)
l4=Label(window,text="Pressure",font=("Calibri Light",20))
l4.grid(row=5,column=0)


title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=3,column=1)

title2_text=StringVar()
e2=Entry(window,textvariable=title2_text)
e2.grid(row=4,column=1)

title3_text=StringVar()
e3=Entry(window,textvariable=title3_text)
e3.grid(row=5,column=1)


l5=Label(window,text="°C",font=("Calibri Light",20))
l5.grid(row=3,column=2,padx=0)
l6=Label(window,text="%",font=("Calibri Light",20))
l6.grid(row=4,column=2,padx=0)
l7=Label(window,text="mbar",font=("Calibri Light",20))
l7.grid(row=5,column=2,padx=0)

b1=Button(window,text="Get Data From Sensor",font=("Calibri Light",20),command=search)
b1.grid(row=4,column=3,columnspan=3)

b2=Button(window,text="Predict Weather",font=("Calibri Light",20),command=pret)
b2.grid(row=7,column=3)

 
T = Text(window, height=2, width=30,bg='lightgreen') 
T.grid(row=7,column=0,columnspan=2) 


l8=Label(window,text="Note:This Model is 88% accurate ",height=2)
l8.grid(row=8,column=0,rowspan=2,columnspan=2)
l8.config(bd=10)
#l8.grid_columnconfigure(0, weight=1,pad=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=11,column=0,columnspan=4,pady=6)



window.mainloop()

