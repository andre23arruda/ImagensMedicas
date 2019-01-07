## ----------------- Aula 7 - 8 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens
import cv2
from funcoesImagensMedicas import *

## 1
I = im2double(im.imread('C:\PythonScripts\ImagensMedicas\Lab07\hue.pgm')) # lendo imagem pgm
#plt.figure()
#plt.imshow(I)
#plt.axis('off')
#plt.title('Ultrassom Bebê')

regiao = cv2.selectROI(I) # selecionando regiao
cv2.destroyAllWindows() # fechando a imagem

Colunamin = int(regiao[0])             # Valor da coluna minima da regiao 
Colunamax = int(regiao[0] + regiao[2]+1) # Valor da coluna maxima da regiao 
Linhamin = int(regiao[1])              # Valor da linha minima da regiao 
Linhamax = int(regiao[1] + regiao[3]+1)  # Valor da linha maxima da regiao

media = np.mean(I[Linhamin:Linhamax,Colunamin:Colunamax])
desvio = np.std(I[Linhamin:Linhamax,Colunamin:Colunamax])

## 2
imFilter = np.zeros(I.shape)
inicio = int((7+1)/2)
for i in range(inicio,(I.shape[0])-inicio):
    for j in range(inicio,(I.shape[1])-inicio):
        janela = I[i-inicio:i+inicio+1,j-inicio:j+inicio+1]
        mediaLocal = np.mean(janela)
        desvioLocal = np.std(janela)
        k = (1 - (desvio/(desvioLocal+0.000001)))
        if k < 0:
            k = 0
        imFilter[i,j] = mediaLocal+k*(I[i,j] - mediaLocal)
        
        
plt.figure()
plt.subplot(1,2,1)
plt.imshow(I,cmap='gray')
plt.axis('off')
plt.title('Original')

plt.subplot(1,2,2)
plt.imshow(imFilter,cmap='gray')
plt.axis('off')
plt.title('I Lee')


plt.show()




