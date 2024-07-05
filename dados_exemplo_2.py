import pandas as pd
import numpy as np
import random

tamanho=500
tamanho2=1000
variavel_teste='branch'

individuos = {'ids':np.arange(1,tamanho+1,1),
             'Q1':np.random.randint(1, 6, tamanho),
             'Q2':np.random.randint(1, 6, tamanho),
             'Q3':np.random.randint(1, 6, tamanho),
             'Q4':np.random.randint(1, 6, tamanho),
             'Q5':np.random.randint(1, 6, tamanho),
             'Q6':np.random.randint(1, 6, tamanho),
             'Q7':np.random.randint(1, 6, tamanho),
             'Q8':np.random.randint(1, 6, tamanho),
             'Q9':np.random.randint(1, 6, tamanho),
             'fpd30':np.random.binomial(n=1, p=0.25, size=tamanho)}

df = pd.DataFrame(individuos)
df['ids']='n'+df.ids.astype(str)
