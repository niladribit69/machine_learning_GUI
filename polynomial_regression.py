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
window.configure(bg='light blue')

def salary_predictor(raw_text):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    dataset=pd.read_csv('Position_Salaries.csv')
    X=dataset.iloc[:,1:2].values
    Y=dataset.iloc[:,2].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    from sklearn.linear_model import LinearRegression
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree = 4)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, Y)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, Y)
    sample_output=lin_reg.predict([[raw_text]])
    sample_output2=lin_reg_2.predict(poly_reg.fit_transform([[raw_text]]))
    return(sample_output,sample_output2)

def get_salary():
    raw_text=entry.get('1.0',tk.END)
    raw_text=float(raw_text)
    a,b=salary_predictor(raw_text)
    print(a,b)
    result = '\nPredicted salary with linear regression : {}'.format(a)
    result2 = '\nPredicted salary with polynomial regression : {}'.format(b)
    tab1_display.insert(tk.END,result)
    tab2_display.insert(tk.END,result2)
def clear_text():
        entry.delete('1.0',END)
        speak("the text is cleared")
                
def clear_display_result():
        tab1_display.delete('1.0',END)
        tab2_display.delete('1.0',END)
        speak("the result is cleared")
my_font=Font(family="Times New Roman",weight="bold",slant="italic")
speak("welcome to ML polynomial regression GUI")
l1 = Label(window,text='Enter position level to predict salary',padx=5,pady=5,font=my_font)
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

l2 = Label(window,text='salary with linear regression',padx=5,pady=5,font=my_font)
l2.grid(row=7,column=0)
tab1_display=Text(window,height=2)
tab1_display.grid(row=8,column=0,columnspan=3,padx=5,pady=5)  
l3 = Label(window,text='salary with polynomial regression',padx=5,pady=5,font=my_font)
l3.grid(row=9,column=0)
tab2_display=Text(window,height=2)
tab2_display.grid(row=10,column=0,columnspan=3,padx=5,pady=5)  
window.mainloop()
