import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.messagebox

def x_rate(a, f, t):
    url='https://www.x-rates.com/calculator/?from='+f+'&to='+t+'&amount='+str(a)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rate_tag= soup.find('span',{'class':'ccOutputRslt'})
    rate = rate_tag.text.replace(t, ' ')
    return rate
    
    


root=Tk()
root.title("Currency Converter")
root.geometry("500x500")

ip1=StringVar(root)
ip2=StringVar(root)

ip1.set("Select")
ip2.set("Select")

def RealTimeConversion():
    fr=ip1.get()
    to=ip2.get()

    if (value.get()==""):
        tkinter.messagebox.showerror("Error","Amount not enterred\n")

    elif(fr=="Select" or to=="Select"):
         tkinter.messagebox.showerror("Error","Amount not enterred\n")
         
    else:
        amt=float(value.get())
        new_amt=x_rate(amt,fr,to)

        output.insert(0,str(new_amt))

        
def clear():
    value.delete(0,END)
    output.delete(0,END)
    ip1.set("Select")
    ip2.set("Select")



label1 = Label(root,font=('Helvetica',15,'bold'), text = "Amount :",fg = 'black')
label1.place(x=20,y=50)

label2 = Label(root,font=('Helvetica',15,'bold'), text = "From :",fg = 'black')
label2.place(x=20,y=120)

label3 = Label(root,font=('Helvetica',15,'bold'), text = "To :",fg = 'black')
label3.place(x=20,y=170)

label4 = Label(root,font=('Helvetica',15,'bold'), text = "Converted Amount :",fg = 'black')
label4.place(x=20,y=300)

Currency_list=['USD','INR','GBP']

FromCurrency_option=OptionMenu(root,ip1,*Currency_list)
ToCurrency_option=OptionMenu(root,ip2,*Currency_list)

FromCurrency_option.place(x=100,y=120)
ToCurrency_option.place(x=100,y=170)

value=Entry(root)
value.place(x=150,y=57)

output=Entry(root)
output.place(x=250,y=305)

convert = Button(root, text = "Convert", bg = "white", fg = "black", command = RealTimeConversion) 
convert.place(x=200,y=220)

clear1 = Button(root,text = "Clear", bg = "white",fg = "black", command = clear) 
clear1.place(x=208,y=400)

root.mainloop()
