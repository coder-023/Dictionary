from tkinter import *
from functools import partial

import json
import time
import difflib
root = Tk()
root.geometry("600x600");
frame = Frame(root)
#from dictionary1 import main
username_list=['mukul','devashish','omkar']
password_list=['mukul123','devashish123','omkar123']
def loginvalidationreturn(username, password):
    if(username in username_list and password in password_list):
        return True
    else:
        return False    
def check_wrd(word):
    user_txt=word
    print(user_txt)
    f=open('076 data.json') #opening the json file
    data=json.load(f)    
      #loading all the contents
    data1=data              #data1 is dictionary.We have to lower the keys of the dictionary
    data1 = {k.lower(): v for k, v in data1.items()} #Here,we set the keys of dictionary to lower case
    user_txt=user_txt.lower()
    if(user_txt not in data1.keys()):
        try:
         a=difflib.get_close_matches(user_txt,data1,1) #compare the input string with the dictionary and only return 1 
         
         return True
        except:
            
            return False
            time.sleep(2)
            quit()     
    else:
        
        
        return True
def validateLogin(username, password):
    result=loginvalidationreturn(username.get(), password.get())
    if(result==True):
        openNewWindow()
            
    else:
        nw=Toplevel(root)
        Label(nw,text="Invalid username and/or password entered",font=("ComicSansMS 20 bold"),fg="Green").pack(pady=10);
        #root.destroy()
        return False 
	
def openNewWindow():
    newWindow=Toplevel(root)
    newWindow.title("Meaning Section")
    Label(newWindow,text="*******Dictionary*******",font=("ComicSansMS 20 bold"),fg="Green").pack(pady=10);
    frame = Frame(newWindow)
    Label(frame, text="Type Word:", font=("Helvetica 15 bold")).pack(side=LEFT)
    word = Entry(frame, font=("Helvetica 15 bold"))
    word.pack()
    frame.pack(pady=10)
    
    Button(newWindow, text="Submit", font=("Helvetica 15 bold"), command=partial(dict,word)).pack()

# def dict(word):
    
    
def dict(word):
    print(str(word))
    newWindow=Toplevel(root)
    newWindow.title("Meaning Section")
    frame0= Frame(newWindow)
    Label(frame0, text="", font=("Helvetica 10 bold")).pack(side=LEFT)
    doyoumeaning = Label(frame0, text="", font=("Helvetica 10"))
    doyoumeaning.pack()
    frame0.pack(pady=10)
    
    frame1 = Frame(newWindow)
    Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
    meaning = Label(frame1, text="", font=("Helvetica 10"))
    meaning.pack()
    frame1.pack(pady=10)
    meaning.config(text="");
    doyoumeaning.config(text="")
    
    user_txt=word.get()
    user_txt=str(user_txt)
    f=open('076 data.json') #opening the json file
    data=json.load(f)    
      #loading all the contents
    data1=data              #data1 is dictionary.We have to lower the keys of the dictionary
    data1 = {k.lower(): v for k, v in data1.items()} #Here,we set the keys of dictionary to lower case
    user_txt=user_txt.lower()
    if(user_txt not in data1.keys()):
        try:
         a=difflib.get_close_matches(user_txt,data1,1) #compare the input string with the dictionary and only return 1 
         doyoumeaning.config(text='Do you mean '+a[0]+' ?');
         meaning.config(text=data1[a[0]][0])
         return True
        except:
            doyoumeaning.config(text='Not Found.....')
            return False
            time.sleep(2)
            quit()     
    else:
        
        meaning.config(text=data1[user_txt][0])
        return True
    #Label(root,text="Dictionary",font=("ComicSansMS 10 bold"),fg="Blue").pack(pady=10);

#window
 
root.title('Login Form')
title=Label(root,text='Welcome to A-Z Dictionary.',font=("ComicSansMS 20 bold")).grid(row=1, column=8)
#username label and text entry box
usernameLabel = Label(root, text="User Name",font=("ComicSansMS 20 bold")).grid(row=5, column=6)
username = StringVar()
usernameEntry = Entry(root, textvariable=username, font=("Helvetica 15 bold")).grid(row=5, column=8)  

#password label and password entry box
passwordLabel = Label(root,text="Password",font=("ComicSansMS 20 bold")).grid(row=6, column=6)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*', font=("Helvetica 15 bold")).grid(row=6, column=8)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(root, text="Login", font=("ComicSansMS 20 bold"),command=validateLogin).grid(row=7, column=8)  

root.mainloop()