#düz fonksiyon
def selamla(): 
    print("merhaba")
    print("nasılsın")

selamla()

#değer alan fonksiyon
def soyle(xxx="değer gönderilmedi!"): 
    print(xxx)
soyle()
#soyle("napıyorsun?")


#değer döndüren fonksiyon
def topla(aaa,bbb): 
   return aaa + bbb

sonuc = topla(8,9)
print(sonuc)