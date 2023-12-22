# -*- coding: utf-8 -*-
"""Selamat Datang di Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

DIANNOVA DIVA ALZAHRAH ARYANTI-1217030009- TUGAS 3

Program dan hasil tugas 3 kolom 1
"""

import pandas as pd

last_names = ['Connor', 'Connor', 'Reese']
first_names = ['Sarah', 'John', 'Kyle']
df = pd.DataFrame({
  'first_name': first_names,
  'last_name': last_names,
})

url = "https://raw.githubusercontent.com/FillahAlamsyah/Machine-Learning-Prediksi-Posisi-Pada-Gerak-Parabola/main/DatabaseGerakParabola.txt"
database = pd.read_csv (url, sep=',')
'''pd.read_csv('data.csv')'''
print(database.columns)
print(database.describe())
print(database.head())
print(database.tail())

"""program dan hasil tugas 3 kolom 2 "sudah divariasikan"
"""

import numpy as np
x = [i for i in range(5,12)]
y1 = np.tan(x)
y2 = np.cos(x)
y3 = np.sin(x)

print(x,y1,y2,y3)

"""program dan hasil tugas 3 kolom 3 "sudah divariasikan"
"""

dataframe = pd.DataFrame({
    'x': x,
    'y1': y1,
    'y2': y2,
    'y3': y3
                             })
dataframe['z1'] = np.tan(x)
dataframe['z2'] = np.cos(x)
dataframe['z3'] = np.sin(x)


dataframe