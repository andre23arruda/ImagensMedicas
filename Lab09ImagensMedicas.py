## ----------------- Aula 9 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens
import pydicom
from funcoesImagensMedicas import *




dcmInfo = pydicom.dcmread('C:\PythonScripts\ImagensMedicas\Lab09\IOCT-TD.dcm') # lendo imagem pgm

informations,imagem = getInformations(dcmInfo)

## 2
# Numero de frames, numero de linhas e numero de colunas

## 6
plt.figure()
plt.imshow(imagem[19,:,:], cmap='hot')
plt.axis('off')
plt.title('IOCT 20 slice')


## 7
imagemCortada = imagem[:,0:525,84:615]
plt.figure()
plt.imshow(imagemCortada[19,:,:], cmap='hot')
plt.axis('off')
plt.title('IOCT 20 slice cortado')







plt.show()









