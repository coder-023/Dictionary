from tkinter import *
import json
import time
import difflib
root = Tk()
root.geometry("400x400");

def dict():
    meaning.config(text="");
    doyoumeaning.config(text="")
    
    user_txt=word.get()
    user_txt=str(user_txt)
    f=open('076 data.json') #opening the json file
    data=json.load(f)       #loading all the contents
    data1=data              #data1 is dictionary.We have to lower the keys of the dictionary
    data1 = {k.lower(): v for k, v in data1.items()} #Here,we set the keys of dictionary to lower case
    user_txt=user_txt.lower()
    if(user_txt not in data1.keys()):
        try:
         a=difflib.get_close_matches(user_txt,data1,1) #compare the input string with the dictionary and only return 1 
         doyoumeaning.config(text='Do you mean '+a[0]+' ?');
         meaning.config(text=data1[a[0]][0])
        except:
         doyoumeaning.config(text='Not Found.....')
         
         quit()     
    else:
        
        meaning.config(text=data1[user_txt][0])
    #Label(root,text="Dictionary",font=("ComicSansMS 10 bold"),fg="Blue").pack(pady=10);




Label(root,text="*******Dictionary*******",font=("ComicSansMS 20 bold"),fg="Green").pack(pady=10);
frame = Frame(root)

Label(frame, text="Type Word:", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

frame0= Frame(root)
Label(frame0, text="", font=("Helvetica 10 bold")).pack(side=LEFT)
doyoumeaning = Label(frame0, text="", font=("Helvetica 10"))
doyoumeaning.pack()
frame0.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)


Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()










root.mainloop();