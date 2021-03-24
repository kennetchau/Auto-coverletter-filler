#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#! python3 
# autocoverletter

# obj: ask user for input and return a string of coverletter to clipboard
# note: This script is basically fill in the blanks, thus it is still necessary to check for grammer and spelling mistakes


# In[2]:


import pyperclip #use for copying the coverletter to clipboard
import os
from datetime import date #use for copying date
print(os.getcwd())


# In[36]:


#getting today's date
today = date.today()
todaydate = today.strftime("%B %d, %Y") #Automatic getting date

#Create a dictionary for storing variables
v = {'jobtitle':'','company':'','companystat':'','interest':'','special':'','Whyyoufit':'','foundation':'','Proficient':'','NotsoProf':''}


# In[28]:


Question = input("Do you want to read your inputs from a text files?(y/n) ") #Asking if the users have an input file


# In[53]:


if Question == "y": 
    filename = input("What's the full file directory? ") #ask file name
    f = open(filename,"r") #open file read mode
    text = f.read()
    mylist = text.split("\n") #spliting each inputs by using new line
    for item in mylist: #looping the list
        items = item.split(":") #split it again so now we can have key and inputs 
        if (items[0]) in v: #matching key
            v[items[0]] = items[1] #if keys match input value
    f.close()


# In[41]:





# In[48]:





# In[24]:


#getting the list of inputs
if Question != "y":
    v['jobtitle'] = input("Job title? ") #requesting the job title
    v['company'] = input("company name? ") # requesting the company name
    v['companystatement'] = input("What the statement of the company you're applying to? ")
    v['interest'] = input("Why you're interested in this job? ") #Why you're interested in this job
    v['special'] = input("What is special about this company? ") #Asking what is special about this company
    v['Whyyoufit'] = input("Why you're a great candidate? ") #Asking why you're a good candidate
    v['foundation'] = input("What you focus in University? ") #Asking the field you specialize in University
    v['Proficient'] = input("What are you proficient in? ") #Asking skills "Python, Java..."
    v['NotsoProf'] = input("Some other skills? ") #Asking skills


# In[50]:


# the coverletter
text = """{}
Dear Hiring Manager of {},

I am writing to apply for the {} position in your organization. My interest in {} and the opportunity to put my expertise to use and learn from the professionals in {} have propelled me to apply for this position. I believe I am a great candidate for this role due to my {} specialty. I am knowledgeable in {}. Also, I am proficient in {} and have moderate knowledge of {}. Finally, I am detail-oriented and am a team player with the ability to work independently. I am excited by the opportunity to work on the subject I am interested in and help your company continue to {}.

I am a recent graduate from Western University with a bachelor's degree (Hons) in Economics and a minor in Computer Science. My educational background has equipped me with a solid foundation in {}. Also, I am proficient in different programming languages and analytics tools such as Python, R, Excel. For example, I have written a python script that used the package yfinance to download stock price data and use Panda to turn data into meaningful insights. I believe my finance and computer science expertise would allow me to adapt to your organization quickly and produce results effectively.

Besides my technical skills, I am also a strong team player with excellent communication skills, a creative mindset, and strong time management skills. I have participated in different academic challenges, such as the Bank of Canada Governor Challenge and Hack Western. During these challenges, I used my experience and skills to bring my team together and help my team meet the deadline by organizing workflow and responsibility among team members. Also, my ability to think out of the box provides new ways to solve my team's problems and make our project more efficient. Based on the above factors, I envision myself a fitting candidate for your organization.

I am looking forward to putting my knowledge and skill to use as a productive member of your organization and learn from the industry best. If you have any questions or require any additional information, please do not hesitate to contact me via email (kennetchau@gmail.com) or by phone (+1)519-280-6122. Thank you for your time and consideration.
I look forward to discussing this position with you in detail.

Sincerely, 
Ming Yin Kenneth Chau""".format(todaydate,v['company'], v['jobtitle'], v['interest'],v['special'],v['Whyyoufit'],v['foundation'],v['Proficient'],v['NotsoProf'],v['companystat'],v['foundation'])


# In[51]:


pyperclip.copy(text)
print("Coverletter have been copy to clipboard")


# In[ ]:




