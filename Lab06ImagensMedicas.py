## ----------------- Aula 6 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens
from funcoesImagensMedicas import *

## 1
H_ideal = filter(np.zeros([400,400]),0.2)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(H_ideal,cmap = 'gray')
plt.axis('off')
plt.title('H_ideal')

H_gauss = maskGauss2D(400,0.2)
plt.subplot(1,3,2)
plt.imshow(H_gauss,cmap = 'gray')
plt.axis('off')
plt.title('H_gauss')

H_butter = maskButter2D(444,0.2,2)
plt.subplot(1,3,3)
plt.imshow(H_butter,cmap = 'gray')
plt.axis('off')
plt.title('H_butter')

Mamo = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Mamography.pgm') # lendo imagem pgm
#Mamo = np.resize(Mamo,(400,400))
H_butter2 = np.zeros(Mamo.shape)
diferenca = [int(0.5*(Mamo.shape[0] - 444)),int(0.5*(Mamo.shape[1] - 444))]
H_butter2[diferenca[0]:-diferenca[0],diferenca[1]:-diferenca[1]] = H_butter
ImFrequencia = np.fft.fft2(Mamo)
ImFrequencia = np.fft.fftshift(ImFrequencia)
ImFiltrada = ImFrequencia*H_butter2

mamoVoltando = np.fft.ifftshift(ImFiltrada)
mamoVoltando = np.fft.ifft2(mamoVoltando)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(Mamo,cmap='gray')
plt.title('Mamo')
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(np.abs(mamoVoltando),cmap='gray')
plt.title('Mamo Filtrada Baixa')
plt.axis('off')

#plt.figure()
#plt.imshow(H_butter2,cmap='gray')

ImFrequencia = np.fft.fft2(Mamo)
ImFrequencia = np.fft.fftshift(ImFrequencia)
ImFiltrada = ImFrequencia*(1-H_butter2)

mamoVoltando = np.fft.ifftshift(ImFiltrada)
mamoVoltando = np.fft.ifft2(mamoVoltando)
plt.subplot(1,3,3)
plt.imshow(np.abs(mamoVoltando),cmap='gray')
plt.title('Mamo Filtrada Alta')
plt.axis('off')

plt.show()