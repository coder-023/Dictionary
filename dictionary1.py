from tkinter import *
from functools import partial
import json
import time
import difflib
root = Tk()
root.geometry("400x400");
# root1=Tk()
# root1.geometry("400x400");

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

def dict(word):
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
    print(type(word))
    #user_txt=word.get()
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




Label(root,text="*******Dictionary*******",font=("ComicSansMS 20 bold"),fg="Green").pack(pady=10);
frame = Frame(root)

Label(frame, text="Type Word:", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
#check(word.get())
word.pack()
frame.pack(pady=10)




Button(root, text="Submit", font=("Helvetica 15 bold"), command=partial(dict,str(word))).pack()










root.mainloop();