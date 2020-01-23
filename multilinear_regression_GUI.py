import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyttsx3
import speech_recognition as sr
import os
import random
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


window = Tk()
window.geometry('700x500')
window.configure(bg='red')
speak("welcome to ML multilinear regression GUI")

def regressor(r1,r2,r3,r4,r5):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns


#2.loading the dataset
    mydata=pd.read_csv('50_Startups.csv')
    X=mydata.iloc[:,:-1].values
    Y=mydata.iloc[:,4].values

#encoding categorical data
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    ct = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = 'passthrough')
    X = ct.fit_transform(X)
#avoiding dummy variable trap
    X=X[:,1:]

#splitting into training and testing data
    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0) #to have same output in different system

#4.applying multiple linear regression to the training set
    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression()
    regressor.fit(X_train,Y_train)

    return(regressor.predict([[r1,r2,r3,r4,r5]]))

def get_salary():
    r3=entry.get('1.0',tk.END)
    r3=float(r3)
    r4=entry2.get('1.0',tk.END)
    r4=float(r4)
    r5=entry3.get('1.0',tk.END)
    r5=float(r5)
    r6=entry4.get('1.0',tk.END)
    print(r6)
    
    r6=str(r6)
    if 'New York' in r6:
        r1=0.0
        r2=1.0
        print(r1,r2)
    elif 'California' in r6:
        r1=0.0
        r2=0.0
        print(r1,r2)
    elif 'Florida' in r6 :
        r1=1.0
        r2=0.0
        print(r1,r2)
    
    result=regressor(r1,r2,r3,r4,r5)
    print(result)
    speak("predicted profit is")
    speak(result)
    result1 = '\nPredicted profit: {}'.format(result)
    tab1_display.insert(tk.END,result1)

def clear_text():
        entry.delete('1.0',END)
        entry2.delete('1.0',END)
        entry3.delete('1.0',END)
        entry4.delete('1.0',END)
        speak("the text is cleared")
        
def clear_display_result():
        tab1_display.delete('1.0',END)
        speak("the result is cleared")
my_font=Font(family="Times New Roman",weight="bold",slant="italic")
#speak("welcome to ML multi linear regression GUI")
l1 = Label(window,text='Enter details to know profit',padx=5,pady=5,font=my_font)
l1.grid(row=1,column=0)
entry=Text(window,height=1)
entry.grid(row=3,column=0,columnspan=2,pady=5,padx=5)
l2 = Label(window,text='Enter R&D Spend',padx=5,pady=5,font=my_font)
l2.grid(row=2,column=0)
l3 = Label(window,text='Enter Administration',padx=5,pady=5,font=my_font)
l3.grid(row=4,column=0)
entry2=Text(window,height=1)
entry2.grid(row=5,column=0,columnspan=2,pady=5,padx=5)
l4 = Label(window,text='Enter Marketing spend',padx=5,pady=5,font=my_font)
l4.grid(row=6,column=0)
entry3=Text(window,height=1)
entry3.grid(row=7,column=0,columnspan=2,pady=5,padx=5)
l5 = Label(window,text='State',padx=5,pady=5,font=my_font)
l5.grid(row=8,column=0)
entry4=Text(window,height=1)
entry4.grid(row=9,column=0,columnspan=2,pady=5,padx=5)

button1 = Button(window,text='PREDICT',command=get_salary,width=12,bg='#25d366',fg='#fff')
button1.grid(row=10,column=0,pady=10,padx=10 )
button1 = Button(window,text='EXIT',command=window.destroy,width=12,bg='#25d366',fg='#fff')
button1.grid(row=10,column=1,pady=10,padx=10 )
button2 = Button(window,text='Reset',command=clear_text,width=12,bg='#25d366',fg='#fff')
button2.grid(row=11,column=0,pady=10,padx=10 )
button3 = Button(window,text='clean result',command=clear_display_result,width=12,bg='#25d366',fg='#fff')
button3.grid(row=11,column=1,pady=10,padx=10 )

tab1_display=Text(window,height=2)
tab1_display.grid(row=12,column=0,columnspan=3,padx=5,pady=5)  

window.mainloop()
