import cv2

imagem = cv2.imread("saida.jpg")

(b,g,r) = imagem[0,0] #Veja que a ordem BGR  e não RGB

print('O pixel (0,0) tem as seguintes cores: ')
print('Vermelho:',r, 'Verde: ',g, 'Azul: ', b)

cv2.imshow("aee", imagem)
cv2.waitKey(0)