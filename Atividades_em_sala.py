import numpy as np
# dados=np.random.randint(0,101,size=(1,10))
# print(dados)
# print(dados.dtype)

# matriz=np.random.rand(5,5)
# print(matriz)
# print(np.min(matriz))

# arr=np.random.rand(1,10)
# arr2=arr*10
# print(arr)
# print(arr2)
# print(arr2.astype(int))

# arr=np.random.randint(0,10,size=(3,3))
# arr[1,:]=-1
# print(arr)

import pandas as pd
df=pd.DataFrame([["Banana",7.9,12],["Maca",10.2,3],["Pera",11.8,4]],columns = ['fruta','preco','quantidade'])
print(df)
