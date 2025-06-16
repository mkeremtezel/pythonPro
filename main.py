import random
uzunluk="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Lütfen şifrenizin uzunluğunu giriniz: "))
sifre = ""
for i in range(length):
    sifre += random.choice(uzunluk)
print("Oluşturulan şifre: ", sifre)
# Bu kod, kullanıcıdan şifre uzunluğunu alır ve belirtilen uzunlukta rastgele bir şifre oluşturur.
# Kullanıcıdan alınan uzunlukta rastgele karakterlerden oluşan bir şifre üretir.
