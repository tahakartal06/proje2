def proje2anasayfad():

    print("╔"+"═"*30+"╗")
    print("║         Halı Yıkama V1       ║")
    print("║                              ║")
    print("║        1-Müşteri Kayıt       ║")
    print("║        2-Müşteri Ara         ║")
    print("║        3-Bilgi Güncelle      ║")
    print("║        4-Bilgi Sil           ║")
    print("║                              ║")
    print("║      Seçiminizi Yapınız      ║")
    print("╚"+"═"*30+"╝")

    bilgi = input("")

    if bilgi == "1":
        import proje2.muskayit
        proje2.muskayit.muskayitd()
    if bilgi == "2":
        import proje2.musara
        proje2.musara.musarad()
    if bilgi == "3":
        import proje2.bilgün
        proje2.bilgün.bilgünd()
    if bilgi == "4":
        import proje2.bilsil
        proje2.bilsil.bilsild()

    proje2anasayfad()


proje2anasayfad()
