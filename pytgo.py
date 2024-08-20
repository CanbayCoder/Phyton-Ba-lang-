X = 3 
print(X)
isim = "Canbay" #string
fiyat = 13.95 #float
aldımı = False #boolean
x = 3 #integer
isim = "Moby Dick"
Sayfa = 195
gram = 13.45
yenimi = True
print (isim, Sayfa, gram, yenimi)
isim = input("İsminiz Nedir ? ")
print ("Merhaba" ,isim)
yemek = input("En Sevdiğiniz Yemek Nedir ?")
isim = input("İsminiz Nedir ?")
print (isim, yemek, "sever.")
isim = "Emre"
yas = 22
print(isim, yas, "yaşında")
x = 9
y = 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
ehliyet = False
araba = False
if ehliyet and araba:
    print("Araba kullanabilir.")
    
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı.")

elif araba or not ehliyet:
    print("Sürücü Kursumuzu Tercih Ederek Ehliyet Alabilirsiniz :)")

else :
    print ("Araba kullanamazsın.")