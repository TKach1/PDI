import numpy as np
import cv2

INPUT_IMAGE = 'image.jpg'
BOX_HEIGHT = 21 ## quanto menor, maior o arrendonmdamento e consequentemente mais escura a imagem
BOX_WIDTH = 21

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- INGENUO
def ingenuous(img, h, w):
    for y in range(int(h/2), len(img)-int(h/2)):
        for x in range(int(w/2), len(img[0])-int(w/2)):
            soma = 0
            for dy in range(y-int(h/2), y+int(h/2)):
                for dx in range(x-int(w/2), x+int(w/2)):
                    soma += img[dy, dx]
            img[y, x] = soma / (h*w)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SEPARAVEL

def separable(img, h, w):
    sepVertical(img, h, w)
    sepHorizontal(img, h, w)
    
def sepVertical(img, h, w):
    imgbkp = img.copy()
    for y in range(int(h/2), len(imgbkp)-int(h/2)):
        for x in range(int(w/2), len(imgbkp[0])-int(w/2)):
            soma = 0
            for cy in range(y-int(h/2), y+int(h/2)):
                soma += imgbkp[cy][x]
            img[y][x] = soma / h

def sepHorizontal(img, h, w):
    imgbkp = img.copy()
    for y in range(int(h/2),len(imgbkp)-int(h/2)):
        for x in range(int(w/2),len(imgbkp[0])-int(w/2)):
            soma = 0
            for cx in range(x-int(w/2), x+int(w/2)):
                soma += imgbkp[y][cx]
            img[y][x] = soma / w

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- IMAGEM INTEGRAL

def integral(img, h, w):
    integral = integralImage(img)
    for y in range(int(h/2),len(img)-int(h/2)):
        for x in range(int(w/2),len(img[0])-int(w/2)):
            img[y][x] = (integral[y+int(h/2)][x+int(w/2)] - integral[y+int(h/2)][x-int(w/2)-1] - integral[y-int(h/2)-1][x+int(w/2)] + integral[y-int(h/2)-1][x-int(w/2)-1]) / (h*w)

def integralImage(window):
    windowbkp = window.copy()
    for y in range(len(window)):
        windowbkp[y, 0] = window[y, 0]
        for x in range(1, len(window[0])):
            windowbkp[y,x] = window[y,x] + windowbkp[y, x-1]
    
    for y in range(1, len(window)):
        for x in range(len(window[0])):
            windowbkp[y,x] += windowbkp[y-1,x]

    return windowbkp

def main ():

    img = cv2.imread (INPUT_IMAGE)
    img = img.astype (np.float32) / 255
    img = np.tile(img, (3,3,1))

    upCut = int(len(img)/3 - BOX_HEIGHT)
    downCut = int(len(img) - len(img)/3 + BOX_HEIGHT)
    leftCut = int(len(img[0])/3 - BOX_WIDTH)
    rightCut = int(len(img[0]) - len(img[0])/3 + BOX_WIDTH)
    img = img[upCut:downCut, leftCut:rightCut]

    print("Escolha um algoritmo")
    print("1 - Ingenuous")
    print("2 - Separável")
    print("3 - Integral")

    choice = input("> ")

    if choice in ['1', '2', '3']:
        print("Calculando...")
    
    if choice == '1':
        ingenuous(img, BOX_HEIGHT, BOX_WIDTH)
    elif choice == '2':
        separable(img, BOX_HEIGHT, BOX_WIDTH)
    elif choice == '3':
        integral(img, BOX_HEIGHT, BOX_WIDTH)
    else:
        print("Opção inválida!")
        return
    
    img = img[BOX_HEIGHT:len(img) - BOX_HEIGHT, BOX_WIDTH:len(img[0]) - BOX_WIDTH]

    cv2.imshow('blur', img)

    cv2.waitKey ()
    cv2.destroyAllWindows ()


if __name__ == '__main__':
    main ()