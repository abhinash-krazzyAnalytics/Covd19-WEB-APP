# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:15:24 2021

@author: Abhinash
"""

import pickle
#modelling deployment on gui
#step 1 library for ml and gui
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from tkinter import*
from tkinter import messagebox
import pyttsx3

data=pd.DataFrame({"bodytemp":[98,102,101,98,102,100,100,103,101,
                              100,103,104,104,101,103,101,100,100,
                              102,98,98,102,99,98,100,103,102,98,104,103],
                  "age":[36,88,71,80,6,88,56,47,61,89,49,71,
                         10,70,30,49,94,24,51,49,45,92,76,37,
                         38,43,49,22,21,38],
                "breath_problem":[0,1,1,0,0,0,0,1,1,0,1,
                                  1,1,0,1,0,0,1,1,0,0,1,
                                  0,0,0,1,1,0,1,0],
                "running_nose":[0,1,1,1,1,0,0,1,1,0,1,1,
                                1,1,1,0,0,0,1,0,0,1,1,0,
                                1,0,1,0,1,1],
                  "body_pain":[0,1,1,1,1,0,0,1,0,1,1,1,1,
                               0,1,1,1,1,1,0,0,1,0,0,1,0,
                               1,0,1,1],
                   "Corona_infection":["no","yes","yes","yes",'yes','no','no',
                                        'yes','yes','no','yes','yes','yes','no',
                                        'yes','no','no','no','yes','no',
                                       'no','yes','no','no','no','no','yes',
                                       'no','yes','yes']})
le=LabelEncoder()
data["Corona_infection"]=le.fit_transform(data["Corona_infection"])
y=data["Corona_infection"]
x=data.drop(["Corona_infection"],axis=1)
     #form model
model=LogisticRegression()
model.fit(x,y)
     
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
