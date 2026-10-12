import time
print("YKS Net-Puan HESAPLAMA")


obp= input("OPB Puanı: ")
matD = input("Matematik Doğru Sayısı: ")
matY = input("Matematik Yanlış Sayısı: ")
trD = input("Türkçe Doğru Sayısı: ")
trY = input("Türkçe Yanlış Sayısı: ")
sosD = input("Sosyal Bilimleri Doğru Sayısı: ")
sosY = input("Sosyal Bilimleri Yanlış Sayısı: ")
fenD = input("Fen Bilimleri Doğru Sayısı: ")
fenY = input("Fen Bilimleri Yanlış Sayısı: ")

bilgiler = [matD, matY, trD, trY, sosD, sosY, fenD, fenY,obp]

print("Hesaplanıyor...")
time.sleep(1.5)

matnet = int(matD) - (int(matY) / 4)

trnet = int(trD) - (int(trY) / 4)

sosnet = int(sosD) - (int(sosY) / 4)

fennet = int(fenD) - (int(fenY) / 4)

print("Matemetik Neti: {}\nTürkçe Neti: {}\nSosyal Bilimeri Neti:{}\nFen Bilimleri: {}\n".format(matnet, trnet, sosnet, fennet))

toplam = float(matnet)+float(trnet)+float(sosnet)+float(fennet)

print("Toplam Net:", toplam)

ham=int(100)+(float(toplam)*3.33)

print(f"TYT Ham Puanı: {ham}")

obp=float(obp)*float(0.6)

yer= float(ham)+float(obp)

print("Yeleştirme Puanı: {}".format(yer))
