## ----------------- Aula 2 -------------- ##

import numpy as np # importando numpy para operação com matrizes
import imageio as im # importando imageio para leitura de imagens
import matplotlib.pyplot as plt # importando pyplot para exibir imagens

# 1
Mamo = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Mamography.pgm') # lendo imagem pgm
Stent = im.imread('C:\PythonScripts\ImagensMedicas\Lab02\Stent.pgm') # lendo imagem pgm

# 2
plt.figure() # criando figura
plt.imshow(Mamo,cmap='gray') # colocando a imagem Mamo dentro da figura
plt.axis('off') # desabilitando eixo
plt.title('Mamography') # titulo

# 3 - 4
M,N = Mamo.shape # numero de linhas e de colunas da imagem Mamo
MamoNegativo1 = np.zeros([M,N],dtype = 'uint8') # alocando matriz para receber Mamo negativo, para isso criando uma matriz de zeros com o mesmo numero de linhas e de colunas de Mamo original
for i in range(0,M): # Fazendo o negativo de Mamo através de um for, é muito mais custoso (indo da primeira linha até a última)
    for j in range(0,N): # Indo da primeira coluna até a ultima coluna
        MamoNegativo1[i,j] = 255 - Mamo[i,j] # Para tornar negativo é só subtrair o valor máximo (nesse caso é 255 porque é uma imagem de 8 bits) do valor original do pixel
plt.figure() # criando figura
plt.imshow(MamoNegativo1,cmap='gray') # colocando Mamo negativo dentro da figura
plt.axis('off') # desabilitando eixo
plt.title('Mamography Negative 1') # titulo

# 5
MamoNegativo2 = 255 - Mamo # Mamo negativo através de calculo matricial, muito mais rapido
plt.figure() # criando figura
plt.imshow(MamoNegativo2,cmap='gray') # colocando Mamo negativo dentro da figura
plt.axis('off') # desabilitando eixo
plt.title('Mamography Negative 2') # titulo

# 6
from funcoesImagensMedicas import fazerHistograma # importando funcao de fazer histograma
histograma = fazerHistograma(Stent) # fazendo histograma da imagem do Stent
plt.figure() # criando figura
plt.stem(histograma) # plotando da forma stem, aquele de barras fininhas com bolinhas no topo
plt.title('Histograma') # titulo

# 7
StentBrilho = Stent + 50 # Adicionando brilho na imagem do Stent
histograma2 = fazerHistograma(StentBrilho) # fazendo histograma do Stent com brilho, histograma foi deslocado para a direita
plt.figure() # criando figura
plt.stem(histograma2) # plotando da forma stem, aquele de barras fininhas com bolinhas no topo
plt.title('Histograma 2') # titulo

# 8
from funcoesImagensMedicas import imadjust # importando a funcao para realce de contraste
plt.figure() # criando figura
plt.subplot(2,5,1) # subplot de 2 linhas e 5 colunas, 1ª posição
plt.imshow(StentBrilho,cmap = 'gray') # exibindo Stent Brilho na primeira posicao do subplot
plt.title('Stent Brilho') # titulo
plt.axis('off') # desabilitando eixo

histograma3 = fazerHistograma(StentBrilho) # fazendo histogram de Stent Brilho
plt.figure() # criando outra figura
plt.subplot(2,5,1) # subplot de 2 linhas e 5 colunas, 1ª posição
plt.stem(histograma3) # exibindo histograma nessa nova figura
plt.title('Stent Brilho') # titulo

for i in range(9): # realcando contraste com 70% superior, 20% inferior e variando alpha de 0.1 a 0.9
    StentBrilhoC = imadjust(StentBrilho,0.7,0.2,(i/10) + 0.1)
    plt.figure(6)
    plt.subplot(2,5,i+2)
    plt.imshow(StentBrilhoC,cmap = 'gray')
    alphastr = str((i/10) + 0.1)
    alphastr = alphastr[0:4]
    plt.title('Alpha ' + alphastr)
    plt.axis('off')

    histograma3 = fazerHistograma(StentBrilhoC)
    plt.figure(7)
    plt.subplot(2,5,i+2)
    plt.stem(histograma3)
    plt.title('Alpha ' + alphastr)

plt.show()

# 9
plt.figure()
plt.subplot(2,5,1)
plt.imshow(StentBrilho,cmap = 'gray')
plt.title('Stent Brilho')
plt.axis('off')

histograma3 = fazerHistograma(StentBrilho)
plt.figure()
plt.subplot(2,5,1)
plt.stem(histograma3)
plt.title('Stent Brilho')

for i in range(9): # realcando contraste com 70% superior, 20% inferior e variando alpha de 1.1 a 1.9
    StentBrilhoC = imadjust(StentBrilho,0.7,0.2,1+(i+1)/10)
    plt.figure(1)
    plt.subplot(2,5,i+2)
    plt.imshow(StentBrilhoC,cmap = 'gray')
    alphastr = str(1+(i+1)/10)
    alphastr = alphastr[0:4]
    plt.title('Alpha ' + alphastr)
    plt.axis('off')

    histograma3 = fazerHistograma(StentBrilhoC)
    plt.figure(2)
    plt.subplot(2,5,i+2)
    plt.stem(histograma3)
    plt.title('Alpha ' + alphastr)

plt.show()

