import tkinter 
from tkinter import * 
from tkinter import messagebox 

import json
import difflib
def hello():
    
	user_txt=entry_1.get()
	user_txt=str(user_txt)            #String converted form of Entered Text

	f=open('076 data.json') #opening the json file
	data=json.load(f)       #loading all the contents
	data1=data              #data1 is dictionary.We have to lower the keys of the dictionary
	data1 = {k.lower(): v for k, v in data1.items()} #Here,we set the keys of dictionary to lower case
	user_txt=user_txt.lower()

	try:
	 a=difflib.get_close_matches(user_txt,data1,1) #compare the input string with the dictionary and only return 1 
	 label_mean=Label(root,text='Do you mean '+a[0]+' ?')
	 label_mean.grid(row=5,column=10)	
	 
	except:
		label_warn=Label(root,text='Wrong details entered!')
		label_warn.grid(row=4,column=10)
		quit()
	
	j=0
	label_list=list()
	ans=list()
	for i in data1[a[0]]:            #Some words have more than one meanings.For that,we create many labels as required 
                                  #and store their information in list,which would be benificial for us to delete them once the user presses the reset button
		label_ans=Label(root,text=i)
		label_ans.grid(row=j+6,column=10) #arranging each meaning Displaying down by down
		label_list.append(label_ans)
		j=j+1
	
	 	
	
	button_reset=Button(root,text="Reset",command=lambda:reset(label_ans,label_mean,label_list))  #Reset button to clear out the previous stuff!
	button_reset.grid(row=4,column=10)

	def reset(label_ans,label_mean,label_list):
		
		for label in label_list:     #we have to clear all the contents of the labels which has meanings of previous output
			label.destroy()             
		
			
			

		label_mean.after(100 , lambda: label_mean.destroy()) #after 100 milisecs,perform the action
		entry_1.delete(first=0,last=100)                                                           
		button_reset.destroy()  

root=Tk()
root.geometry("400x400")
label_1=Label(root,text='Welcome to my Window',bg='red',font='70').pack(pady=10);
entry_1=Entry(root)
label_2=Label(root,text='Dictionary A to Z',bg='red',font='70')
button_1=Button(root,text='Enter',command=hello)


# #label_1.grid(row=0,column=10)
# label_2.grid(row=1,column=10)
# entry_1.grid(row=2,column=10)
# button_1.grid(row=3,column=10)
root.mainloop()