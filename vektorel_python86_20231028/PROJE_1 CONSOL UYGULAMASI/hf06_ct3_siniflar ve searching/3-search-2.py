import random
vMaaslari = []
for a in range(100000):
    vMaaslari.append(random.randint(10,99))

maasAlanlar20 = 0
sonuc="yok"

# for xx in vMaaslari:
#     if xx == 20: maasAlanlar20+=1
#     print(xx)

# print("20 maas alan sayısı:", maasAlanlar20)

# for xx in vMaaslari:
#     if xx < 20: maasAlanlar20+=1
#     print(xx)

# print("20 maas alan sayısı:", maasAlanlar20)

for xx in vMaaslari:
    if xx == 99: sonuc="var"
    print(xx)

print("20 maas alan sayısı:", maasAlanlar20)
print("99k maas alan:",sonuc)