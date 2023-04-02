print("Hesap Makinesi")

while True:
    # Kullanıcıdan sayı girişleri alınır
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    # Kullanıcıdan işlem seçimi alınır
    print("Yapılacak işlemi seçin:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    secim = input("Seçiminiz (1/2/3/4): ")

    # Seçime göre ilgili işlem yapılır
    if secim == '1':
        sonuc = sayi1 + sayi2
        print("Toplama sonucu:", sonuc)
    elif secim == '2':
        sonuc = sayi1 - sayi2
        print("Çıkarma sonucu:", sonuc)
    elif secim == '3':
        sonuc = sayi1 * sayi2
        print("Çarpma sonucu:", sonuc)
    elif secim == '4':
        if sayi2 == 0:
            print("Sıfıra bölme hatası!")
        else:
            sonuc = sayi1 / sayi2
            print("Bölme sonucu:", sonuc)
    else:
        print("Geçersiz işlem seçimi!")

    # Yeniden hesap yapılıp yapılmayacağı sorulur
    devam = input("Başka bir hesap yapmak istiyor musunuz? (E/H): ")
    if devam.lower() == 'h':
        break

print("Hesap makinesi kapatıldı.")
