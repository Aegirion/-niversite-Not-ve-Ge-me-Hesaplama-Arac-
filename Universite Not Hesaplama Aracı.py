print("Hoşgeldiniz \nLütfen yapmak isteğiniz işlemi seçiniz. \n 1)Finalden kaç almam gerek? \n 2)Dersten geçer miyim?")
print()
talep=int(input("İstediğiniz işlemi tuşlayınız:"))

if talep==1:
    gn=int(input("Geçme notunuzu yazınız:"))
    vize=int(input("Vize notunu yazınız:"))
    vko=int(input("Vize puanı oranını yazınız(Orn.30):"))
    fko=int(input("Final puanı oranını yazınız(Orn.70):"))
    orn= (vko/100)
    forn=(fko/100)
    final=((50-(vize*orn))/forn)
    print()
    print(int(final), "almanız gerek")

elif talep==2:
    gec=int(input("Geçme notunu yazınız:"))
    vn=int(input("Vize notunu yazınız:"))
    fn=int(input("Final notunu yazınız:"))
    x=int(input("Vize puanı oranını yazınız(Orn.30):"))
    y=int(input("Final puanı oranını yazınız(Orn.70):"))
    xe=(x/100)
    ye=(y/100)
    hsp=(vn*xe)+(fn*ye)
    print()
    if hsp > gec:
        print(int(hsp),"ile geçtiniz.Tebrikler.")

    elif hsp == gec:
        print(int(hsp),"tam sınırda geçtiniz.")

    else:
        print(int(hsp),"maalesef geçemediniz")




