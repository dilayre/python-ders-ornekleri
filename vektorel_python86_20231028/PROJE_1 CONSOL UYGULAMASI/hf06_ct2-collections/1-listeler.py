ogrenciler = ["Doruk","Ediz","Dilara","helin"]
#print(ogrenciler)

#for item in ogrenciler:
#print(item)

for item in range(len(ogrenciler)):
    print(item,ogrenciler[item])

print("Ekleme işlemi---------")
ogrenciler.append("Hakan")
ogrenciler.append("Ahmet")

for item in ogrenciler:
    print(item)

print("silme işlemi------")
ogrenciler.pop(2)

for item in ogrenciler:
    print(item)