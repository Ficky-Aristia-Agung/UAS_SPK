# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:19:25 2021

@author: Ficky Aristia Agung
"""

from nltk.stem import PorterStemmer
ps = PorterStemmer()
kata = ["program","programs","programer","programing","programers"]
for k in kata:
    print(k, " : " , ps.stem(k))
    
    
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
stm = ["giving","given","given","gave"]
for word in stm:
    print(word, ":", lst.stem(word))