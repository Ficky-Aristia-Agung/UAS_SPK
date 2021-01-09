# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:20:25 2021

@author: Ficky Aristia Agung
"""

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print ("car :", lemmatizer.lemmatize("cars"))
print ("foot :", lemmatizer.lemmatize("feet"))
print ("people :", lemmatizer.lemmatize("people"))
print ("fantasize :", lemmatizer.lemmatize("fantasized"))