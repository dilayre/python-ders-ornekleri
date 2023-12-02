sozluk = {
    "fil":"elephant",
    "kedi":"cat",
    "köpek":"dog",
    "kelebek":"butterfly"
}

arabaListesi = {
    "markası":"toyota",
    "fiyatı":"400000"
}
print(arabaListesi["markası"])



for zz in sozluk:
    print("index yerine",zz,"var ve değeri: ",sozluk[zz])

arabalar = {
    "araba1": {"marka":"toyota","fiyatı":400000},
    "araba2": {"marka":"opel","fiyatı":500000},
    "araba3": {"marka":"mercedes","fiyatı":600000}
}
print(arabalar["araba3[marka]"])