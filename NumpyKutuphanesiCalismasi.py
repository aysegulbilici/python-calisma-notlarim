#%% numpy
"""
-matrisler için hesaplama kolaylığı sağlar
"""

import numpy as np

#1*15 boyutunda bir array
dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) #arrayin boyutu

dizi2=dizi.reshape(3, 5)

print("şekil: " ,dizi2.shape)
print("boyut: ",dizi2.ndim)
print("veri tipi: ", dizi2.dtype.name)
print ("boy: ", dizi2.size)

#array type
print("Type ", type(dizi2))

#2 boyutlu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

#sıfırlardan oluşan bir array
sifir_dizi=np.zeros((3,4))
print(sifir_dizi)

#birlerden oluşan bir array
bir_dizi=np.ones((3,4))
print(bir_dizi)

#bos array
bos_dizi=np.empty((3,4))
print(bos_dizi)

#arange (x,y,basamak)
dizi_aralik=np.arange(10,50,5)
print(dizi_aralik)

#linspace(x,y,basamak)
dizi_bosluk=np.linspace(10, 20,5) #10 ve 20 arasını 5 e bölüyor
print(dizi_bosluk)

#float array
float_array=np.float32([[1,2],[3,4]])
print(float_array)

#♦matematiksel işlmeler
a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a**2)

#dizi elemanı toplama
print(np.sum(a))
#max değer
print(np.max(a))

#mean ortalama
print(np.mean(a))

#median ortalama
print(np.median(a))

#rastgele sayı üretme(0,1) arasında sürekli uniform 3*3
rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)

#indeks
dizi=np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin il 4 elemanı
print(dizi[0:4])

#dizinin tersi
print(dizi[::-1])

#
dizi2D=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1. satır ve 1. sütünunda bulunan elemanı
print(dizi2D[1,1])

#1. sütun ve tüm satırlar
print(dizi2D[:,1])

#satır 1 ,sütun 1 ,2 ,3 
print(dizi2D[1,1:4])

#dizinin son satır ve tüm sütunları
print(dizi2D[-1,:])

#
dizi2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

#vektor haline getirme
vektor=dizi2D.ravel()
print(vektor)

maksimum_sayinin_indeksini=vektor.argmax()
print(maksimum_sayinin_indeksini)











