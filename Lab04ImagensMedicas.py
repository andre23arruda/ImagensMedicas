## ----------------- Aula 4 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens

## 1
amostra = np.array([15,29,5,8,255,40,1,0,10])

# 3 formas de fazer copia de uma matriz ou vetor:
amostraOrdenada = amostra.copy() # fazendo literalmente a copia
amostraOrdenada = amostra + 0 # colocando a matriz em outra variavel e somando zero
amostraOrdenada = np.array(amostra) # usando np.array
amostraOrdenada.sort() # ordenando
mediana = np.median(amostraOrdenada)

## 2
IMRI = im.imread('C:\PythonScripts\ImagensMedicas\Lab04\TransversalMRI_salt-and-pepper.pgm') # lendo imagem pgm
IMRIfiltrada = np.zeros(IMRI.shape) # criando matriz de zeros com o tamanho de IMRI (alocando memória para a nova imagem)

from funcoesImagensMedicas import medianFilter # importando a função de filtro mediana
IMRIfiltrada = medianFilter(IMRI,3) # aplicando filtro mediana de mascara 3x3

plt.figure() # criando figura
plt.subplot(1,3,1) # subplot de 1 linha e 2 colunas
plt.imshow(IMRI,cmap='gray') # exibindo IRI original
plt.title('IMRI') # titulo
plt.axis('off') # desativando eixos

plt.subplot(1,3,2)
plt.imshow(IMRIfiltrada,cmap='gray')
plt.title('IMRI filtrada 3x3')
plt.axis('off')


imFilter = medianFilter(IMRI,5)
plt.subplot(1,3,3)
plt.imshow(imFilter,cmap='gray')
plt.title('IMRI filtrada 5x5')
plt.axis('off')


## 3
from funcoesImagensMedicas import gaussmf
x = np.arange(1,10)
m = 5
s = 1
gx = gaussmf(x,m,s)
plt.figure()
plt.plot(x,gx)
plt.title('Gaussiana')

gxT = gx.copy().transpose()
w_Gauss2D = np.kron(gx,gx).reshape(gx.size,gx.size)
plt.figure()
plt.imshow(w_Gauss2D,cmap = 'gray')
plt.axis('off')
plt.title('Gaussiana 2D')

w_Gauss2D2 = w_Gauss2D *(1/np.sum(w_Gauss2D))
Mamo = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Mamography.pgm') # lendo imagem pgm
from funcoesImagensMedicas import conv2, im2double, fazerMascaraGauss2D
Mamo = im2double(Mamo)
convolucaoMamo = conv2(Mamo,w_Gauss2D2)
plt.figure()
plt.imshow(convolucaoMamo,cmap = 'gray')
plt.axis('off')
plt.title('Convolucao Mamo')

mascara = fazerMascaraGauss2D(8,3)
convolucaoMamo2 = conv2(Mamo,mascara)
plt.figure()
plt.imshow(convolucaoMamo2,cmap = 'gray')
plt.axis('off')
plt.title('Convolucao Mamo 2')

## 4
f = im.imread('C:\PythonScripts\ImagensMedicas\Lab04\TransversalMRI2.pgm')
f = im2double(f)
mascara = fazerMascaraGauss2D(8,3)
f_borrado = conv2(f,mascara)
g = f - f_borrado
f_afiado = f + g

plt.figure()
plt.subplot(1,3,1)
plt.imshow(f,cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(g,cmap='gray')
plt.title('Bordas')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(f_afiado,cmap='gray')
plt.title('Bordas afiadas')
plt.axis('off')


## 5
from funcoesImagensMedicas import xcorr2
Stent = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Stent.pgm') # lendo imagem pgm
wx_priwitt = np.kron(np.ones([3,1],dtype = 'uint8'),np.array([-1,0,1]))
wy_priwitt = wx_priwitt.transpose()
wx_sobel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
wy_sobel = wx_sobel.transpose()

gx_priwitt = xcorr2(Stent,wx_priwitt)
gy_priwitt = xcorr2(Stent,wy_priwitt)
modulo_priwitt = (gx_priwitt**2 + gy_priwitt**2)**0.5

gx_sobel = xcorr2(Stent,wx_sobel)
gy_sobel = xcorr2(Stent,wy_sobel)
modulo_sobel = (gx_sobel**2 + gy_sobel**2)**0.5

plt.figure()
plt.subplot(1,3,1)
plt.imshow(gx_sobel,cmap = 'gray')
plt.title('Gx Priwitt')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gy_sobel,cmap = 'gray')
plt.title('Gy Priwitt')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(modulo_sobel,cmap = 'gray')
plt.title('Modulo Priwitt')
plt.axis('off')

plt.show()