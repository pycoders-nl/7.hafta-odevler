print("""
      =============================================="
      |                                            |
      |                                            |
      |             TELEFON REHBERI                |
      |               HOSGELDINIZ                  |
      |                                            |
      ==============================================\n""")

print("""
    1. Kisi Ekleme
    2. Kisi Silme
    3. Kisi Yada Numara Guncelleme
    4. Rehberi Listeleme\n""")


rehber={}

while True:
    secim=input("Yapacaginiz Islemi Seciniz:")
    if secim=="1":
        tel_no=input("Olusturulacak kisinin telefon numarasini giriniz: ")
        adı_soyadı=input("Olusturulacak kisinin Adini veSoyadini Giriniz: ")
        rehber[adı_soyadı]=tel_no
        print(adı_soyadı," kisisi kaydedildi..")

    if secim=="2":
        sil=input("silmek istediginiz kişi'nin ad-soyad giriniz:")
        a=(input("adlı kişi silinsin mi?\nsilmek için 2'ye basınız:\nvazgeçmek için 1'e basınız:")).lower()

        if a =="2":
            print(rehber.pop(sil,"kisisi bulunamadı"))

        elif a=="1":
            print(sil,"silmekten vazgeçtiniz")

        else:

            print("yanlış giriş yaptınız tekrar deneyin...")
        continue

    if secim=="3":
        güncel=input("güncellemek istediğiniz kişinin ad soyadını giriniz:")
        for y in rehber.keys():
            if y == güncel:
                adı_soyadı1=input("yeni ad-soyad:")
                tel_no1=input("yeni telefon numarası:")
                rehber[adı_soyadı1]=tel_no1
                rehber.pop(güncel)
                print(rehber)
                print(güncel,"kişi güncellendi")

            else:
                print("böyle bir kişi telefon rehberinde bulunamadı")
        break

    if secim=="4":
        rehber.items()
        for anahtar,değer in rehber.items():
            print("{}={}".format(anahtar,değer))
            continue

    if secim=="5":
        çıkış=input("çıkmak için q'basınız:")
        print("çıkılıyor....")

        break
        
dosya_kayıt=open("telefon\trehberi.txt","w")
dosya_kayıt.write("adı_soyadı\tnel_no\n")
for k,v in rehber.items():
    dosya.write(a)
dosya.close()



