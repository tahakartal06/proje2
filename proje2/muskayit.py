def muskayitd():
    def türüekle():
        print("yolluk")
        print("dokuma")
        print("kilim")
        türler = ["yolluk","dokuma","kilim"]
        tür = input("Türünü giriniz:")
        if tür in türler:

            print(tür)
            
            return tür
        
        else:
            print(f"Girdiğin tür{türler}den birisi olmak zorunda.")
            return "x"
    adsoyad= input("Ad soyad giriniz:").upper()
    telefon = input("Telefon numaranızı giriniz:")
    ebatı = input("Metrekare giriniz:").upper()
    adres = input("Adres giriniz:").upper()
    türü = türüekle()

    mus = open("veri1.txt","a",encoding="utf8")
    mus.write(f"{adsoyad}___{telefon}___{türü}___{ebatı}m2___{adres}\n")