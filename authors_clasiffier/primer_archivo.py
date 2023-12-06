# -*- coding: utf-8 -*-
"""Prueba1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bL-AEf_J0a0CjxRI_MSYOfK6oEIXK7GB

# Naive Bayes Classifier

## LIbrerias
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.model_selection import train_test_split

"""## Funciones

"""

def letra_separada(oracion):
    lyrics = [word for word in oracion]
    lyrics2 = [oracion.count(word) for word in oracion]
    dictionary = {}
    for palabra in lyrics:
        for rep in lyrics2:
            dictionary[palabra]= rep
            lyrics2.remove(rep)
            break
    return dictionary

def Lyrics_count(song):
    canc = open(song)
    lyrics = []
    letrac = []
    for elemento in canc:
        try:
            lyrics.append((elemento.strip()).split())
        except StopIteration:
            break
    for oracion in lyrics:
        for palabra in oracion:
            letrac.append(palabra)

    diccionario = letra_separada(letrac)
    return diccionario

cancion = "AlejandroSanz.txt"
letra = Lyrics_count(cancion)
letra

nltk.download('punkt')
nltk.download('stopwords')

msg = open(cancion)

is_body = False
lines = []

for elemento in msg:
    lines.append((elemento.strip()))

lines
art_body = '\n'.join(lines)
print(art_body)

art_body

palabras = word_tokenize(art_body.lower())
palabras

palabrasnt = set(stopwords.words('spanish'))
palabrasnt

filtradas = []
for word in palabras:
    if word not in palabrasnt and word.isalpha() == True:
        filtradas.append(word)

print(filtradas)

stemmer = SnowballStemmer('spanish')
Stem = []

for word in filtradas:
    stemmed_word = stemmer.stem(word)
    Stem.append(stemmed_word)

print(Stem)
len(Stem)
