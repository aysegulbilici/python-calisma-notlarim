#SAYILAR VE STRINGLERE GİRİS

print("hello")
9
9.2
type(9)
type(9.2)
type("hello")

#STRİNGLERE YAKINDAN BAKALIM

123
type(123)
"123"
type("123")

"a"+"b"
"a" "b"
"a" " b"

"a"*3

#STRİNG METODLARI-len()

gel_yaz="gelecegi_yazanlar"

#	del a
b=9
c=10
b*c

len(gel_yaz)

#STRİNG METODLARI-upper() & lower()

gel_yaz="gelecegi_yazanlar"

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()

B= gel_yaz.upper()


#STRİNG METODLARI-replace()

gel_yaz="gelecegi_yazanlar"
gel_yaz.replace("e","a") 

gel_yaz
  
gel_yaz.replace("a","i")

#STRİNG METODLARI-strip()

gel_yaz=" gelecegi_yazanlar "

gel_yaz.strip()

gel_yaz="*gelecegi_yazanlar*"
gel_yaz.strip("*")

#METODLARA GENEL BAKIŞ

dir(gel_yaz) #amacımız parantez içindeki veri tipiyle neler yapabileceğimizi görmek
dir(str)

#SUBSTRİNGLER

#köşeli parantez koyduğumuz anda python parantezden önceki ifadenin içinde
#bir seçim işlemi olacağını anlar.
gel_yaz[3]
gel_yaz[0:4]

#TYPE DONUSUMLERİ

birinci_sayi=input()

toplama_bir=input()
toplama_iki=input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki) 
12
type(str(12))

#print()

print("hello ai era")

print("geleceği", "yazanlar", sep="_")


#VERİ YAPILARI
#Listeler
#Listeler farklı türden elemanları içinde barındırabilir,kapsayıcıdır.
#sıralıdır,değiştirliebilir.
#[]
#list()

notlar=[90,80,70,50]
type(notlar)

liste=["a",19.3,90]

list_genis=["a",19.3,90,notlar]

len(list_genis)

type(list_genis[0])
type(list_genis[1])
type(list_genis[3])

tum_liste=[liste, list_genis]

#del tum_liste

listte=[10,20,30,40,50]

listte[0]
listte[0:2]
listte[:2]
listte[2:]

yeni_liste=["a",10,[20,30,40,50]]
yeni_liste

yeni_liste[2]

yeni_liste[2][1]

yeni_liste[2][2]



#Listeler- Eleman DEğiştirme

liste=["ali" , "veli" , "berkcan", "ayse"]

liste[1]="velinin_babasi"

liste
liste[1]="veli"

liste[0:3]="a","b","c"
liste

liste=liste+ ["kemal"]

#del liste[2]
liste

#Listeler - Liste Metodları
liste=["ali" , "veli" , "berkcan", "ayse"]

dir(liste)

liste
#append & remove

liste.append("berkcan")
liste
#kalıcı değişiklik yaptı

liste.remove("berkcan")
liste

#insert (indekse göre eleman ekleme)

liste=["ali", "veli", "isik"]

liste

liste.insert(0, "ayse")
liste

#liste[0]= "ayse" yapsaydık eleman değiştirirdik, eklemiş olmazdık.

#sona ekleme işlemi(saymadan)

len(liste)
liste.insert(len(liste)," beren")
liste

#pop (indekse göre silme)

liste.pop(0)
liste

#count 

liste=["ali","veli","isik","ali","veli"]
liste.count("ali")
liste.count("isik")

#copy
#elimizdeki mevcut listenin ilk halini saklamak için

liste_yedek=liste.copy()

#extend
#iki listeyi birleştirmek için 

liste.extend(["a","b",10])
liste 

#index

liste.index("ali")

#reverse
#elemanları terse çevirme işlemi

liste.reverse()
liste

#sort 
#sıralama yapmak için

liste=[10,40,5,90]

liste.sort()
liste

#clear
#listeyi temizler

liste.clear()
liste

#Veri YApıları- Tuple (demet)

#Kapsayıcıdırlar, sıralıdırlar
#değiştirilemezler (listeden farkı)

t=("ali","veli", 1,2,3.2, [1,2,3,4])

t="ali","veli", 1,2,3.2, [1,2,3,4]

#tuple()

t=("eleman")
type(t)
#tupleların tek elemanlısında böyle bir şey var

t=("eleman",)
type(t)

t[1]
t[0:3]

t[2]=99 #tupple değişikliğe izin vermez hatası alıyoruz.


#Veri Yapıları - Dictionary(Sözlük)
#kapsayıcıdır
#sırasızdır ve değiştirilebilir.

#anahtar ifadeler ve karşılıklarının bir arada tutulduğu veri yapısı

#Sozluk Olusturma
sozluk={"REG":"Regresyon Modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}

sozluk
len(sozluk)

sozluk={"REG":10,
        "LOJ":20,
        "CART":30}
sozluk

sozluk={"REG":["RMSE",10],
        "LOJ":20,
        "CART":30}


#Sozluk Eleman İSimleri

sozluk={"REG":"Regresyon Modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}

sozluk[0]
#sırasız olduğu için hata verir 

sozluk["REG"]

sozluk={"REG":["RMSE",10],
        "LOJ":20,
        "CART":30}

sozluk["REG"]
#sozluk içinde sozluk yapısı
sozluk={"REG":{"RMSE":10,
               "MSE":20,
               "SSE":30},
        
        "LOJ":{"RMSE":10,
               "MSE":20,
               "SSE":30},
        
        "CART":{"RMSE":10,
                "MSE":20,
                "SSE":30}}

sozluk
sozluk["REG"]["SSE"]

#Sozluk- Eleman Ekleme ve DEğiştirme

sozluk={"REG":"Regresyon Modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}

sozluk["GBM"]="Gradient Boosting Mac"

sozluk

sozluk["REG"]="Çoklu Doğrusal Regresyon"

sozluk

sozluk[1]="Yapay Sinir Ağları"
sozluk

l=[1]
l

sozluk[l]="yeni bir sey"
#key değerleri ancak sabit veri yapılarıyla oluşturulabilir
#string ve sayılar sabit veri yapılarıdır.
#keyler sabitliğinden endişe etmememiz gereken sabit yapılardır

t=("tuple",)
sozluk[t]="yeni bir sey"

sozluk

#sol taraf olan key yapısına istediğimiz her şeyi koyamıyoruz çünkü
#referans noktası.


#Veri Yapıları - Setler
#sırasızdır (indexsizdir)
#tekrar eden değerlerden oluşamaz
#değiştirilebilir

l=[1,"a","ali","123"]
s=set(l)
s

t=("a","ali")

s=set(t)
s

ali="lutfen_ata_bakma_uzaya_git"
type(ali)

s=set(ali)
s
#her bir karakter bir defa feçiyor.mattaki kümeler gibi

len(s)
l[0]

s[0]
#set nesnesi index işlemini desteklemiyor, sırasızdır.

#eleman ekleme ve çıkarma

l=["gelecegi","yazanlar"]

s=set(l)
s

dir(s)

s.add("ile")
s

s.add("ile")
s

s.remove("ile")
s

s.discard("ile")
s

#Setler- klasik küme işlemleri

# =============================================================================
# # difference() ile iki kümenin farkını ya da "-" ifadesi 
# # intersection() iki kume kesişimi ya da "&" ifadesi
# # symmetric_difference() ikisinde de olmayanları.
# 
# =============================================================================
#difference

set1=set([1,3,5])
set2=set([1,2,3])

set1.difference(set2)
#☻set1de olup set2 de olmayan değerler
 
set1.symmetric_difference(set2)

set1-set2


#intersection & union

set1=set([1,3,5])
set2=set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

set1&set2

kesisim=set1&set2 #saklama işlemi

set1.union(set2)
#her bir eleman bir defa yer alacak


#Set sorhu işlemleri

set1=set([7,8,9])
set2=set([5,6,7,8,9,10])

#♠iki kümenin bos olup olmadıhının sorgusu

set1.isdisjoint(set2)
#iki kümenin kesişimi boş mu?

#bir kümenin bütün elemanlrının başka bir küme içerisinde yer alıp almadığı
set1.issubset(set2)
#set1 set2 nin alt kümesi midir

#bir kümenin diğer kümeyi kapsayıp kapsamadığı
set2.issuperset(set1)






#FONKSİYONLARA GİRİS VE FONKSİYON OKURYAZARLIĞI

print()
print

?print
#fonksiyonun dokumantasyonu gelir.
#kulllanım ve detaylarını veriyor.

#argümanlar fonk genel amacını birdiren alt ayarlardır.

len()
#bir argüman alır, o olmadan çalışmıyor.


#Fonksiyon Nasıl Yazılır?

#fonksiyon tanımlama def ile yapılır.
def kare_al(x):
    print(x**2)
    
kare_al(3)    

#Bİlgi Notuyla Çıktı Üretmek

def kare_al(x):
    print(x**2)
    
kare_al(5)    


def kare_al(x):
    print("Girilen sayının karesi:"+ str(x**2))
    
kare_al(5)




def kare_al(x):
    print("Girilen sayı: "+ str(x)+ " Girilen sayının karesi: "+ str(x**2))
    
kare_al(5)

#İki Argümanlı Fonksiyon Tanımlamak

def kare_al(x):
    print(x**2)
    
def carpma_yap(x,y):
    print(x*y)

carpma_yap(2, 3)


#Ön Tanımlı Argümanlar

def carpma_yap(x,y=1):
    print(x*y)
 #y ye 1 değerini vererek ön argüman tanımladık.
 
carpma_yap(3,4)


#Argümanların Sıralaması

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(y=2,x=3)


#Ne zaman fonksiyon yazılır?

#tekrar eden görevleri yerine getirmek ve var olan ihtiyaçları daha programatik şekle getirmek.

#isi,nem,sarj

(40+25)/90

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)


direk_hesap(30, 40, 70)

#Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)


cikti=direk_hesap(25, 40, 70)
cikti
print(cikti)
#fonksiyonun ciktisini işleyemedik.

direk_hesap(25, 40, 70)*9


def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

direk_hesap(25, 40, 70)*9

cikti=direk_hesap(25, 40, 70)
cikti

#Local ve Global Değişkenler

#Global DEğişkenler
x=10
y=20

#Local Değişkenler
#fonksiyonların içinde,etki alanındaki değişkenlerdir.
def carpma_yap(x,y):
    return x*y

carpma_yap(2, 3)

#Local etki alanından Global etki alanını değiştirmek

x=[]

def eleman_ekle(y):
    x.append(y)
    print(str(y)+ " ifadesi eklendi")

eleman_ekle(1)
eleman_ekle("ali")

x

#Karar ve Kontrol Yapıları

#True-False sorgulamaları

sinir=5000

sinir==4000
#eşit mi?

5==4

#if

sinir=50000

gelir=40000

if gelir<sinir:
    print("gelir sinirdan küçük")
    print(gelir*2)

#else


if gelir<sinir:
    print("gelir sinirdan küçük")
    print(gelir*2)
else :
    print("gelir sinirdan büyük")

#elif

 sinir=50000
 gelir1=60000
 gelir2=50000
gelir3=35000

if gelir1>sinir:
    print("tebrikler hediye kazandınız")
elif gelir1<sinir:
    print("uyarı!")
else:
    print("takibe devam")

#mini uygulama
sinir=50000
magaza_adi=input("Magaza Adı Nedir")
gelir=int(input("Gelirinizi Giriniz"))

if gelir>sinir:
    print("tebrikler"+ magaza_adi+ " promosyon kazandınıız.")
elif gelir<sinir:
    print("uyarı! Cok düşük gelir: "+ str(gelir))
else:
        print("takibe devam")

#DONGÜLER-- for

ogrenci=["ali","veli","isik","berk"]

for i in ogrenci:
    print (i)
    
    

maaslar=[1000,2000,3000,4000,5000]

for i in maaslar:
    print(i*2)


#dongu ve fonksiyonları birlikte kullanmak

def kare_al(x):
    print(x**2)

kare_al(2)

for i in maaslar:
    print(i)

#maaslara yuzde 20 zam

1000*20/100+1000

maaslar[0]*20/100+maaslar[0]
maaslar[1]*20/100+maaslar[1]
maaslar[2]*20/100+maaslar[2]

#dongu yazilacak

def yeni_maas(x):
    print(x*20/100+x)
    
for i in maaslar:
    yeni_maas(i)


#mini uygulama

maaslar=[1000,2000,3000,4000,5000]

#maasi 3000den yüksek olanlara yüzde 10zam az olanlara yuzde 20 zam

def zamli_maas_ust(x):
    print(x*10/100+x)

def zamli_maas_alt(x):
    print(x*20/100+x)
    
for i in maaslar:
  if i>=3000:
      zamli_maas_ust(i)
  else:
      zamli_maas_alt(i)
     
#break and continue

maaslar=[8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)


for i in maaslar:
    if i==3000:
       continue
    print(i)

#While (bu sart sağlandıı sürece)

sayi=1

while sayi<10:
    sayi+=1
    print(sayi)


#NESNE YÖNELİMLİ PROGRAMLAMA

#Temelini sınıflar oluşturur.

#Sinif nedir?
#benzer özellikler ortak amaçlar taşıyan gruplar oluşturmak için kullanılır.



#sınıf özellikleri (class attributes)

class VeriBilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildigi_diller=[]
    
#sınıfların özelliklerine erişmek
VeriBilimci.sql
VeriBilimci.bolum

#sınıfların özelliklerini değiştirmek
VeriBilimci.sql='hayır'
VeriBilimci.sql

#Sİnif Örneklendirmesi (instantiation)

ali=VeriBilimci()

ali.sql
ali.deneyim_yili

ali.bildigi_diller.append("python") #burada yapılan bir değişiklik tüm sınıfa mal oldu
ali.bildigi_diller

veli=VeriBilimci()
veli.sql
veli.bildigi_diller


#ÖRnek ÖZellikleri

#her bir orneğin kendi içinde değişen özelliklerden oluşabildiği bilgisi
class VeriBilimci():
    bolum=''
    sql=''
    deneyim_yili=0
    bildigi_diller=["R","PYTHON",]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''
ali=VeriBilimci()
ali.bildigi_diller


veli=VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller

VeriBilimci.bildigi_diller
 
VeriBilimci.bolum
ali.bolum="istatistik"
ali.bolum

#Ornek Metodları

class VeriBilimci():
    calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali=VeriBilimci()
ali.bildigi_diller
ali.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

#Miras Yapıları (Inheritance)

#Yeni tanımladığımız class daha önce tanımladığımız classın
#özelliklerini barındırıyorsa ve onları biz kullanmak istiyorsak
#işte bu classın  özelliklerini miras olarak kullanabilyoruz.

class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.Address=""
        

class DataScience(Employees):
    def __init__(self):
        self.Programming=""
   
veribilimci1=DataScience()
veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling=""
        


#☺Fonksiyonel yapıda tanımlamak
class Employees_yeni():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Address=Address

ali=Employees_yeni("a", "b", "c")
ali.FirstName


#Pythonda Fonksiyonel Programlama

#Fonksiyonlar Dİlin bastacidir.
#(Birinci Sınıf Nesnelerdir.)
#Yan etkisiz fonksiyonlar(stateless, girdi-çıktı)
#Yüksek seviye fonksiyonlar
##Vektorel Operasyonlar


#Yan Etkisiz Fonksiyonlar (Pure Funcions)

#Örnek1:yan etki - bagımsızlık

A=5

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

impure_sum(6)
#A değerini değiştirdiğimizde fonk. aynı değere girsek bile sonuç farklı gelecektir
#yan etki durumu, fonksiyonun dışarıda bi bağımlılığı var

pure_sum(3, 4)
#♦bu fonksiyonun sonucu değişmez

#ornek2:olumcul yan etkiler
#OOP

class LineCounter:
    def __init__(self,filename):
        self.file=open(filename, "r")
        self.lines=[]
        
    def read(self):
        self.lines=[line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc=LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines= read('deneme.txt')
lines_count=count(example_lines)
lines_count

#İsmimsiz Fonksiyonlar (Anonymous Functions)
#OOP
def old_sum(a,b):
    return a+b

old_sum(4, 5)

new_sum=lambda a,b:a+b
new_sum (4,5)


sirasiz_liste=[('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste,key=lambda x:x[1])

#☺Vektorel operasyonlar 

a=[1,2,3,4]
b=[2,3,4,5]

ab=[]
range(0,len(a))
for i in range(0,len(a)):
    ab.append(a[i]*b[i])
 
ab

#FP

import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

a*b


#map, filter and reduce

liste=[1,2,3,4,5]

for i in liste:
    print(i+10)



list(map(lambda x:x+10, liste))

#map: verilen bir vektörün içerisinde bir fonk. çalışma imkanı verir.


#filter (iteratif bir nesne alır,bu nesne üzerinden başka bir iteratif nesne 
#oluşturulur ve iteratif nesne içerisinde aradığı şartın sağlandığı tüm elemanlar
# filtrelenir)


liste=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x:x%2==0,liste))

#reduce
#indirgeme işlemi yapar. 

from functools import reduce

liste[1,2,3,4]

reduce(lambda a,b:a+b, liste)


#modul oluşturmak

#belşirli amaçları yerine getirmek için bir arada bulıunan fonk topluluğudur.


#"Hatalar -İstisnalar (exceptions)
#ZeroDivisionError hatası

a=10
b=0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("paydada sıfır olmaz")

a/b



#tip hatası

a=10
b="2"

a/b


try:
    print(a/b)
except TypeError:
    print("sayi ve string problemi")













