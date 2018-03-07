#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:53:08 2018

@author: victor
"""

import pandas as pd 
from sklearn.preprocessing import LabelEncoder

encoderProvisors = LabelEncoder()
data = pd.read_csv('census.csv')

provisors = data.iloc[:, 0:14].values
classes = data.iloc[:, 14].values

#fit_transform transforma os valores distintos de string para int (sexo M,F vira 0,1)
provisors[:, 1] = encoderProvisors.fit_transform(provisors[:, 1])
provisors[:, 3] = encoderProvisors.fit_transform(provisors[:, 3])
provisors[:, 5] = encoderProvisors.fit_transform(provisors[:, 5])
provisors[:, 6] = encoderProvisors.fit_transform(provisors[:, 6])
provisors[:, 7] = encoderProvisors.fit_transform(provisors[:, 7])
provisors[:, 8] = encoderProvisors.fit_transform(provisors[:, 8])
provisors[:, 9] = encoderProvisors.fit_transform(provisors[:, 9])
provisors[:, 13] = encoderProvisors.fit_transform(provisors[:, 13])