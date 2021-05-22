#import all the required libraries
import requests
from tkinter import *
import tkinter.messagebox

#API key from Alpha Vantage API Service
api_key = 'TF7EODX3H4PHJYIE'

#this function scraps the realtime currency
#conversion rate from x-rates.com
def exchange_using_api(a,f,t):
    base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
    main_url = base_url + '&from_currency=' + f + '&to_currency=' + t+ '&apikey=' + api_key
    response = requests.get(main_url)
    result = response.json()
    key = result['Realtime Currency Exchange Rate']
    rate = key['5. Exchange Rate']
    new_amt=float(rate)*a
    return new_amt


#Create a GUI window
root=Tk()
#Title of GUI window
root.title("Currency Converter")
#Configuration of GUI window
root.geometry("500x500")


#Create global variables
input1=StringVar(root)
input2=StringVar(root)

#Initialise global variables
input1.set("Select")
input2.set("Select")

#Function to call exchange_using_bs()
#function using values enterred by user
def RealTimeConversion():
    variable1=input1.get().split()
    variable2=input2.get().split()
    fromm=variable1[0]
    to=variable2[0]

    if (value.get()==""):
        tkinter.messagebox.showerror("Error","Amount not enterred\n")

    elif(fromm=="Select" or to=="Select"):
         tkinter.messagebox.showerror("Error","Amount not enterred\n")
         
    else:
        amount=float(value.get())
        new_amount=exchange_using_api(amount,fromm,to)
        output.insert(0,str(new_amount)) #insert method inserts new_amount in output field

        
#Function for clearing entry field      
def clear():
    value.delete(0,END)
    output.delete(0,END)
    input1.set("Select")
    input2.set("Select")

#Configure background colur of GUI Window
root.configure(background = 'black')

#Creates headlabel giving heading to GUI Window
#place method is used for placing widgets
headlabel = Label(root,font=('Helvetica',15,'bold'), text = 'Welcome to Real Time Currency Convertor',
                  fg = 'white', bg = "blue")  
headlabel.place(x=40,y=1)

#Create label named Amount
label1 = Label(root,font=('Helvetica',15,'bold'), text = "Amount :",fg = 'black')
label1.place(x=20,y=50)

#Create label named From
label2 = Label(root,font=('Helvetica',15,'bold'), text = "From :",fg = 'black')
label2.place(x=20,y=120)

#Create label named To
label3 = Label(root,font=('Helvetica',15,'bold'), text = "To :",fg = 'black')
label3.place(x=20,y=170)

#Create label named Converted Amount
label4 = Label(root,font=('Helvetica',15,'bold'), text = "Converted Amount :",fg = 'black')
label4.place(x=20,y=300)

CurrencyCode_list=['AUD - Australian Dollar', 'CAD - Canadian Dollar', 'CHF - Swiss Franc',
                   'CNY - Chinese Yuan Renminbi', 'DKK - Danish Krone', 'EUR - Euro', 'GBP - British Pound',
                   'HKD - Hong Kong Dollar', 'HUF - Hungarian Forint', 'INR - Indian Rupee',
                   'JPY - Japanese Yen', 'MXN - Mexican Peso', 'MYR - Malaysian Ringgit',
                   'NOK - Norwegian Krone', 'NZD - New Zealand Dollar', 'PHP - Philippine Peso',
                   'RUB - Russian Ruble', 'SEK - Swedish Krona', 'SGD - Singapore Dollar',
                   'THB - Thai Baht', 'TRY - Turkish Lira', 'USD - US Dollar', 'ZAR - South African Rand']

#Creates drop-down menu based on currency list given
#'*' is usede to unpack the list
FromCurrency_option=OptionMenu(root,input1,*CurrencyCode_list)
ToCurrency_option=OptionMenu(root,input2,*CurrencyCode_list)

FromCurrency_option.place(x=100,y=120)
ToCurrency_option.place(x=100,y=170)

#Creates text-entry box
value=Entry(root)
value.place(x=150,y=57)

output=Entry(root)
output.place(x=250,y=305)

#Creates button attached with RealTimeConversion function
convert = Button(root,font=('arial',15,'bold'), text = "Convert", bg = "blue", fg = "white",
                 command = RealTimeConversion) 
convert.place(x=200,y=220)

#Creates button attached with clear function
clear1 = Button(root,font=('arial',15,'bold'), text = "Clear", bg = "blue",fg = "white", command = clear) 
clear1.place(x=208,y=400)

#Start GUI Window
root.mainloop()
