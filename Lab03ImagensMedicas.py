## ----------------- Aula 3 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens

# 1
w = np.array([1,2,3,2,8]) # criando vetor mascara (kernel)
f = np.array([0,0,0,1,0,0,0,0]) # criando vetor sinal

Lw = w.shape[0] # tamanho da mascara
Lo = f.shape[0] # tamanho do sinal

L = Lo + 2*(Lw-1) # calculando o tamanho do sinal com preenchimento de zeros
fpadding = np.zeros(L,dtype = 'uint8') # criando vetor de zeros com o tamanho calculado
fpadding[Lw-1:-(Lw-1)] = f # colocando o vetor sinal dentro do vetor de zeros

# 2 - 3
c = np.zeros(Lo+Lw-1) # criando vetor de zeros que vai receber o resultado da correlacao entre w e f
for i in range(Lo+Lw-1):  # fazendo correlacao
    c[i] = np.sum(w*fpadding[i:i+5]) 
    
# 4
padding = int((Lw-1)/2) # encontrando o tamanho do preenchimento de zeros
c = c[padding:-padding] # ceifando os zeros de preenchimento

# 5
f = np.zeros([5,5],dtype = 'uint8') # criando matriz de zeros 5x5
f[2,2] =1 # colocando no centro da matriz o valor 1
c = np.zeros([5,5],dtype = 'uint8') # criando a matriz de correlacao com zeros 5x5
w = np.array([[1,2,3],[4,5,6],[7,8,9]]) # criando matriz mascara (kernel)
M,N = f.shape # numero de linhas e colunas de f

# 6
for i in range(1,4): # fazendo a correlação da matriz com a mascara
    for j in range(1,4):
        c[i,j] = np.sum(f[i-1:i+2,j-1:j+2]*w) # correlacao

# 9
from funcoesImagensMedicas import im2double, xcorr2
f = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Mamography.pgm') # lendo imagem pgm
#f = im2double(f) # para dar certo não pode transformar a imagem para double
plt.figure()
plt.subplot(1,2,1)
plt.imshow(f,cmap='gray')
plt.title('Mamograph')
plt.axis('off')

w = np.ones([11,11])
w = w/np.sum(w)
c = xcorr2(f,w)

plt.subplot(1,2,2)
plt.imshow(c,cmap='gray')
plt.title('Mamograph Correlation')
plt.axis('off')


plt.show()






