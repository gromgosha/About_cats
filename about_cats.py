import pandas as pd
import numpy as np
import scipy
from scipy import spatial
import re

data_list = list(open('sentences.txt'))
list_sentence = []

# Построчное чтение исходного файла, перевод всех букв в нижний регистр, токенизация (выделение отдельных слов) и добавление в их в список
for line in data_list: 
    a =  line.strip()
    a = a.lower()
    tokens = re.sub('[^a-z]', ' ', a).split()
    list_sentence.append(tokens)
    
# Создание словаря всех уникальных слов из исходного текста и присвоение каждому слову индекса
n = 0
dict_words = {}
for item in list_sentence:
    for word in item:
        if word not in dict_words.keys():
            dict_words[word] = n
            n += 1

# Создание нулевой матрицы размером (количество предложений исходного файла х количество уникальных слов)
matr = np.zeros([len(list_sentence), len(dict_words)])

# Заполнение матрицы matr. Элементу матрицы прибавляется 1 в случае употребления слова в предложении
for k in range(len(list_sentence)):
    sent = list_sentence[k]
    for word in sent:
        if word in dict_words.keys():
            j = dict_words[word]
            matr[k, j] += 1

# Вычисление косинусного расстояния между векторами матрицы matr
for v in range(len(list_sentence)):
    
    cos_distance = scipy.spatial.distance.cosine(matr[0], matr[v])
    
    print ('The cosine distance between 0 sentence and %s sentene: %s' %(v, cos_distance))