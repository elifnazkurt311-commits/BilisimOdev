print("Hesap Makinesi")
print("Çıkmak için 'exit' yaz")

while True:
    islem = input("İşlemi gir (örnek: 3+4): ")

    if islem.lower() == "exit":
        print("Program sonlandırıldı.")
        break

    try:
        if "+" in islem:
            a, b = islem.split("+")
            sonuc = float(a) + float(b)

        elif "-" in islem:
            a, b = islem.split("-")
            sonuc = float(a) - float(b)

        elif "*" in islem:
            a, b = islem.split("*")
            sonuc = float(a) * float(b)

        elif "/" in islem:
            a, b = islem.split("/")
            if float(b) == 0:
                print("Hata: 0'a bölme yapılamaz!")
                continue
            sonuc = float(a) / float(b)

        else:
            print("Hata: Sadece +, -, *, / işlemleri yapılabilir.")
            continue

        print("Sonuç:", sonuc)

    except:
        print("Hatalı giriş! Lütfen 3+4 gibi bir işlem gir.")
