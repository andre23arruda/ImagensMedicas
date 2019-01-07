def im2double(im): # função que converte imagem para formato double
    import numpy as np
    maximo = np.max(im)
    im2 = im.astype(np.float)/maximo
    return im2

def fazerHistograma(im): # função que calcula o histograma de uma imagem de 8 bits (uint8)
    import numpy as np
    histograma = np.zeros(256)
    for i in range(0,256):
        histograma[i] = np.sum(im == i)
    return histograma
        
        
def imadjust(im,a,b,alfa = 1): # função que realiza o ajuste de contraste de uma imagem
    import numpy as np
    m = 255/(255*a-255*b)
    im2 = im + 0
    im2 = np.round(im2 * (m** alfa))
    im2[im <= int(255*b)] = 0
    im2[im >= int(255*a)] = 255
    im2[im2>255] = 255
    return im2

def xcorr2(f,w): # função que calcula a correlação entre uma imagem e uma mascara
    import numpy as np
    Mw,Nw = w.shape
    Mf,Nf = f.shape
    c = np.zeros([Mf,Nf], dtype = 'uint8')
    inicio = int(((Mw + 1)/2 ) - 1)
    for i in range(inicio,Mf-inicio):
        for j in range(inicio,Nf-inicio):
            c[i,j] = np.sum(f[i-inicio:i+Mw-inicio,j-inicio:j+Mw-inicio]*w)
    return c


def medianFilter(im,window): # função que aplica o filtro mediana em uma imagem
    import numpy as np
    imFilter = np.zeros(im.shape)
    inicio = int((window+1)/2)
    for i in range(inicio,(im.shape[0])-inicio):
        for j in range(inicio,(im.shape[1])-inicio):
            janela = im[i-inicio:i+inicio+1,j-inicio:j+inicio+1]
            imFilter[i,j] = np.median(janela.reshape(1,-1))
    return imFilter


def meanFilter(im,window): # função que aplica o filtro media em uma imagem
    import numpy as np
    imFilter = np.zeros(im.shape)
    inicio = int((window+1)/2)
    for i in range(inicio,(im.shape[0])-inicio):
        for j in range(inicio,(im.shape[1])-inicio):
            janela = im[i-inicio:i+inicio+1,j-inicio:j+inicio+1]
            imFilter[i,j] = np.mean(janela)
    return imFilter


def gaussmf(x, u, s, A = 1): # função que gera os resultados de uma função gaussiana
    import numpy as np
    gx = x.copy()
    gx = A*np.exp(-0.5*((gx - u)/s)**2)
    return gx
    
def conv2(f,w): # função de convolução entre um sinal (imagem) e uma mascara
    import numpy as np
    w = np.flip(w)
    Mw,Nw = w.shape
    Mf,Nf = f.shape
    c = np.zeros([Mf,Nf])
    inicio = int(((Mw + 1)/2 ) - 1)
    for i in range(inicio,Mf-inicio):
        for j in range(inicio,Nf-inicio):
            c[i,j] = np.sum(f[i-inicio:i+Mw-inicio,j-inicio:j+Mw-inicio]*w)
    c[c<0] = 0
    c[c>1] = 1
    return c

def fazerMascaraGauss2D(u,s): # Função para gerar uma mascara gaussiana em 2D
    import numpy as np
    x = np.arange(1,2*u)
    x = np.exp(-0.5*((x - u)/s)**2)
    mascara = np.kron(x,x).reshape(x.size,x.size)
    mascara = mascara * 1/(np.sum(mascara))
    return mascara
    
    
def filter(imagem,x): # Função de filtragem de uma imagem a partir da frequencia de corte
    import numpy as np
    M,N = imagem.shape
    altura_centro = M/2
    largura_centro = N/2
    filtro = np.zeros([M,N])
    r = M/N
    for i in range(M):
        for j in range(N):
            if (i-altura_centro)**2 + r*((j-largura_centro)**2) <= altura_centro*largura_centro*x*x:
                filtro[i,j] = 1
    return filtro

def maskGauss2D(tamanho,s): # função que cria um filtro gaussiano a partir da frequencia de corte
    import numpy as np
    s = s * (tamanho+1)/2
    u = (tamanho)/2
    x = np.arange(1,tamanho+1)
    x = np.exp(-0.5*((x - u)/s)**2)
    mascara = np.kron(x,x).reshape(x.size,x.size)
    mascara = mascara * 1/(np.sum(mascara))
    return mascara

def maskButter2D(tamanho,s,n): # função que cria um filtro butterworth a partir da frequencia de corte
    import numpy as np
    s = s * (tamanho+1)/2
    u = (tamanho)/2
    x = np.arange(1,tamanho+1)
    x = 1/(1+((x-u)/s)**(2*n))
    mascara = np.kron(x,x).reshape(x.size,x.size)
    #mascara = mascara * 1/(np.sum(mascara))
    return mascara    
 
 
def getInformations(dcmInfo): # função que coleta algumas informações sobre um arquivo dicom
    try:
        informations = {'Rows': dcmInfo.Rows}
        informations['Columns'] =  dcmInfo.Columns
        try:
            informations['Pixel Spacing'] =  dcmInfo.PixelSpacing
        except:
            informations['Pixel Spacing'] =  'Não há'
        informations['Number of Frames'] =  dcmInfo.NumberOfFrames
        informations['Modality'] =  dcmInfo.Modality
        informations['Manufacturer'] =  dcmInfo.ManufacturerModelName
        imagem = dcmInfo.pixel_array
        for k,v in informations.items():
            print(f'{k}: {v}')
    except:
        print('Deu ruim, falta de informação')
        informations = {}
        imagem = []
    return informations,imagem
    
    
    
    