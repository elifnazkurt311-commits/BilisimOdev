# print ifadesi kullanıcının gördüğü ekranda bir şey yazmasını istediğimizde kullanılır
print("Hesap Makinesi")
print("Çıkmak için 'exit' yaz")
print("Örnekler: 2+3+9 , (2+6)*4 , 2**3 , 10-(2+3)")

# while True işlemde hata olmadığı sürece işlemin sürekli devamını sağlar
while True:
    islem = input("İşlemi gir: ")
    
    # Çıkış kontrolü (boşluk ve büyük-küçük harf fark etmez)
    if islem.strip().lower() == "exit":
        print("Program sonlandırıldı.")
        break

    try:
        # Burası işlemde yalnızca matematiksel ifadelerin kullanılmasına izin verildiğini gösterir
        izinli_karakterler = "0123456789+-*/(). "
        for k in islem:
            if k not in izinli_karakterler:
                raise ValueError

        sonuc = eval(islem)
        print("Sonuç:", sonuc)

    except ZeroDivisionError:
        print("Hata: 0'a bölme yapılamaz!")

    except:
        print("Hatalı giriş! Geçerli bir matematiksel ifade gir.")


 
