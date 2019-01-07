## ----------------- Aula 5 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens
from funcoesImagensMedicas import *

## 1
f1,f2,f3 = 1,3,5 # variaveis de frequencias
n = int((1+0.01)/0.01) # numero de elementos do vetor tempo
t = np.linspace(0,1,n,endpoint = True) # vetor tempo de 0 a 1 com n elementos
s1 = np.sin(2*np.pi*f1*t) # sinal 1
s2 = np.sin(2*np.pi*f2*t) # sinal 2
s3 = np.sin(2*np.pi*f3*t) # sinal 3
sinal = s1+s2+s3 # soma dos sinais

# Plotando todos os sinais
plt.figure()
plt.subplot(4,1,1)
plt.plot(t,s1)
plt.title('s1')
plt.xlim([min(t),max(t)])
plt.subplot(4,1,2)
plt.plot(t,s2)
plt.title('s2')
plt.xlim([min(t),max(t)])
plt.subplot(4,1,3)
plt.plot(t,s3)
plt.title('s3')
plt.xlim([min(t),max(t)])
plt.subplot(4,1,4)
plt.plot(t,sinal)
plt.title('sinal')
plt.xlim([min(t),max(t)])

#
Xf = np.fft.fft(sinal) # Fast Fourier Transform (FFT) de sinal
Xf = np.abs(Xf) # modulo da FFT de sinal, pois é complexo
Xf = Xf[0:int((Xf.shape[0])/2)] # pegando só a metade de FFT, porque FFT é espelhado
plt.figure()
plt.stem(Xf) # plotando o módulo de FFT


## 2
pulsoQuadrado = im.imread('C:\PythonScripts\ImagensMedicas\Lab05\PulsoQuadrado.pgm') # lendo imagem pgm

## 3
pulsoQuadradoFFT = np.fft.fft2(pulsoQuadrado) # FFT em 2D

FFTshift = np.fft.fftshift(pulsoQuadradoFFT) # colocando as frequencias no centro da matriz 

LogFFTshift = np.log(1+FFTshift) # log para facilitar a visualização

# Plotando tudo
plt.figure()
plt.subplot(2,2,1)
plt.imshow(pulsoQuadrado,cmap='gray')
plt.title('Pulso Quadrado')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(np.abs(pulsoQuadradoFFT),cmap='gray')
plt.title('Pulso Quadrado FFT')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(np.abs(FFTshift),cmap='gray')
plt.title('FFT Shift')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(np.abs(LogFFTshift),cmap='gray')
plt.title('Log FFT Shift')
plt.axis('off')


Mamo = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Mamography.pgm') # lendo imagem pgm
filtro = filter(Mamo,0.2) # filtro de elipse
#plt.figure() # se quiser plotar o filtro é só descomentar
#plt.imshow(filtro,cmap='gray')
#plt.title('Filtro')
#plt.axis('off')
mamoFFT = np.fft.fftshift(np.fft.fft2(Mamo)) # FFT em 2D da mamografia
mamoFiltrado = mamoFFT*filtro # filtrando mamografia com o filtro criado
mamoVoltando = np.fft.ifftshift(mamoFiltrado) # Colocando as frequencias nos cantos da matriz para fazer FFT inverso
mamoVoltando = np.fft.ifft2(mamoVoltando) # FFT inverso para voltar para o domínio espacial
plt.figure()
plt.subplot(1,2,1)
plt.imshow(Mamo,cmap='gray')
plt.title('Mamo')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(np.abs(mamoVoltando),cmap='gray')
plt.title('Mamo Filtrada')
plt.axis('off')





plt.show()


