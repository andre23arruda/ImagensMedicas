## ----------------- Aula 1 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens

# 4 
i1 = im.imread('raioXTorax.pgm') # lendo imagem pgm
i2 = im.imread('raioXTorax.jpg') # lendo imagem jpg (essa tem 3 canais - RGB)

# 5
M,N = i1.shape # tamanho da imagem: M é o número de linhas e N é o de colunas

# 6
valorPixel50 = i1[50,50] # valor do pixel situado na linha 50, coluna 50

# 7
maximo = np.max(i1) # maior valor da matriz // usamos np para calculo de valores de array de duas dimensões
minimo = np.min(i1) # menor valor da matriz

#8
media = np.mean(i1) # media da matriz
mediana = np.median(i1) # mediana da matriz
desvio = np.std(i1) # desvio padrão da matriz
tipo = i1.dtype # tipo do dado. Aqui é uint8, ou seja, inteiro de 8 bits sem sinal 

# 9
plt.figure() # criando figura. NÃO ESQUEÇA DO PARENTESES
plt.imshow(i1,cmap='gray') # colocando a imagem dentro de uma figura
plt.title('Raio-X') # título
plt.axis('off') # não exibindo eixos
plt.colorbar() # exibindo barra de cores
plt.show() # mostrando a figura. NÃO ESQUEÇA DO PARENTESES

# 10
from funcoesImagensMedicas import im2double # criei a função para a galera já usar
i1B = im2double(i1) # convertendo a imagem para double (valores entre 0 e 1)
maximoB = np.max(i1B) 
minimoB = np.min(i1B)
mediaB = np.mean(i1B)
medianaB = np.median(i1B)
desvioB = np.std(i1B)
tipoB = i1B.dtype # tipo agora é float

plt.figure()
plt.imshow(i1B,cmap='gray')
plt.title('Raio-X double')
plt.axis('off')
plt.colorbar()
plt.show()

# 11
i1C = i1[0:-1:2,0:-1:2] # fatiando a matriz. Pegando da primeira a ultima linha, pulando de 2 em dois. Mesma coisa da coluna
novoTamanho = i1C.shape # novo tamanho após o fatiamento
plt.figure()
plt.imshow(i1C,cmap='gray')
plt.title('Raio-X novo tamanho')
plt.axis('off')
plt.colorbar()
plt.show()




