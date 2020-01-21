import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import time
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


window = Tk()
window.geometry('700x500')
window.configure(bg='red')

def salary_predictor(raw_text):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    dataset=pd.read_csv('Salary_Data.csv')
    X=dataset.iloc[:,0:1].values
    Y=dataset.iloc[:,1].values
    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression()
    regressor.fit(X_train,y_train)
    sample_output=regressor.predict([[raw_text]])
    speak("predicted salary is")
    speak(sample_output)
    return(sample_output)

    

def get_salary():
    raw_text=entry.get('1.0',tk.END)
    raw_text=float(raw_text)
    final_text=salary_predictor(raw_text)
    print(final_text)
    result = '\nPredicted salary: {}'.format(final_text)
    tab1_display.insert(tk.END,result)
    
def clear_text():
        entry.delete('1.0',END)
        speak("the text is cleared")
                
def clear_display_result():
        tab1_display.delete('1.0',END)
        speak("the result is cleared")

my_font=Font(family="Times New Roman",weight="bold",slant="italic")
speak("welcome to ML linear regression GUI")
l1 = Label(window,text='Enter year to predict salary',padx=5,pady=5,font=my_font)
l1.grid(row=1,column=0)
entry=Text(window,height=2)
entry.grid(row=2,column=0,columnspan=2,pady=5,padx=5)

button1 = Button(window,text='PREDICT',command=get_salary,width=12,bg='#25d366',fg='#fff')
button1.grid(row=4,column=0,pady=10,padx=10 )
button1 = Button(window,text='EXIT',command=window.destroy,width=12,bg='#25d366',fg='#fff')
button1.grid(row=4,column=1,pady=10,padx=10 )
button2 = Button(window,text='Reset',command=clear_text,width=12,bg='#25d366',fg='#fff')
button2.grid(row=5,column=0,pady=10,padx=10 )
button3 = Button(window,text='clean result',command=clear_display_result,width=12,bg='#25d366',fg='#fff')
button3.grid(row=5,column=1,pady=10,padx=10 )

tab1_display=Text(window,height=2)
tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)  
window.mainloop()
