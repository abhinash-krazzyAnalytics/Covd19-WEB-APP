# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:22:22 2021

@author: Abhinash
"""
import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'TV':230.1, 'Radio':37.8, 'Newspaper':69.2})

print(r.json())