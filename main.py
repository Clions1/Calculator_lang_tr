try:
    islem = input("Lütfen yapacağınız işlemi giriniz (+,-,*,/) : ")

    sayi1 = int(input("lütfen 1.Sayıyı giriniz : "))
    sayi2 = int(input("Lütfen 2.Sayıyı giriniz : "))

    sonuc=0

    if islem == "+":
        print(f"1.Sayı ve 2.Sayı'nın Toplama İşleminin Sonucu = {sayi1+sayi2}")
    elif islem == "-":
        print(f"1.Sayı ve 2.Sayı'nın Çıkarma İşleminin Sonucu = {sayi1-sayi2}")
    elif islem == "*":
        print(f"1.Sayı ve 2.Sayı'nın Çarpma İşleminin Sonucu = {sayi1*sayi2}")
    elif islem == "/":
        print(f"1.Sayı ve 2.Sayı'nın Bölme İşleminin Sonucu = {sayi1/sayi2}")
    else:
        print("Lütfen doğru bir değer giriniz.")

except:
    print("Lütfen Doğru bir değer giriniz")