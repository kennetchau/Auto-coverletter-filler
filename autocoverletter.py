#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#! python3 
# autocoverletter

# obj: ask user for input and return a string of coverletter to clipboard
# note: This script is basically fill in the blanks, thus it is still necessary to check for grammer and spelling mistakes


# In[1]:


import pyperclip #use for copying the coverletter to clipboard
from tkinter import *
from tkinter import filedialog # for creating giu
from datetime import date #use for copying date


# In[2]:


# A gui to open files, read them and return the text in them
def openfile():
    filepath = filedialog.askopenfilename()
    try:
        file = open(filepath,'r')
        text = file.read()
        file.close()
        return text
    except:
        print("filepath does not exist.")
        exit()
    


# In[3]:


#open template
print("Please select your template")
coverletter = openfile()


# In[4]:


#getting today's date
today = date.today()
todaydate = today.strftime("%B %d, %Y") #Automatic getting date

#Create a dictionary for storing variables
v = {'Name':'','Phone':'','Email':'','Whereyourgrad':'','Degree':'','focus':'','SpecialDesignation':'','Knowledgablein':'','Proficientin':'','ExampleofProficient':'','NotsoProficient':'','Softskills':'','Demostrateexampleofsoftskills':'','howsoftskillsaffectteam':'','Company':'','Companystat':'','Role':'','WhyApply':'','Whatspecabtcomp':'','Whyufit':'','Jobindustry':'','Whatudotoenhance':''}


# In[9]:


Question = input("Do you want to read your inputs from a text files?(y/n) ") #Asking if the users have an input file


# In[13]:


if Question == "y": 
    text = openfile()
    mylist = text.split("\n") #spliting each inputs by using new line
    for item in mylist: #looping the list
        items = item.split(": ") #split it again so now we can have key and inputs 
        if (items[0]) in v: #matching key
            v[items[0]] = items[1] #if keys match input value
    


# In[14]:


#getting the list of inputs
if Question != "y": #using a loop to fill in the dictionary
    for item in v:
        v[item]=input("{}?".format(str(item)))


# In[22]:


# the coverletter
text = coverletter
text = text.format(todaydate,v["Company"],v["Role"],v["WhyApply"],v["Whatspecabtcomp"],v["Whyufit"],v["Knowledgablein"],v["Proficientin"],v["NotsoProficient"],v["Companystat"],v["Whereyourgrad"],v["Degree"],v["SpecialDesignation"],v["focus"],v["Jobindustry"],v["Whatudotoenhance"],v["ExampleofProficient"],v["Softskills"],v["Demostrateexampleofsoftskills"],v["howsoftskillsaffectteam"],v["Email"],v["Phone"],v["Name"])


# In[20]:


pyperclip.copy(text) #copy coverletter to clipboard
print("Coverletter have been copy to clipboard")


# In[ ]:




