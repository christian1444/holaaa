# %%
import numpy as np
import pandas as pd 
# %%
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)
lista,nplista,pdlista

#print(lista * 4)
#print(nplista * 2)
#print(pdlista  * 2)

df = pd.read_csv("insurance.csv")
print (df.describe())

# %%
