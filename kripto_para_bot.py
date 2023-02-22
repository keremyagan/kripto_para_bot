import ccxt 
import socket
from tkinter import *
from tkinter import messagebox
import datetime
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

    
ip_adress=get_ip()
lisans_bilgisi="DENEME" #lisans kodu
tarih_bilgisi=datetime.datetime(3020,12,27,23,59) #kullanım süresi
"""
eğer botun sadece bir bilgisayarda çalıştırılması istenirse
kullanici_ip="(kullanicinin ip adresi)" şeklinde parantez olmadan
tanımlama yapıp 178.satırdaki ip_address==ip_address kısmını
ip_address==kullanici_ip şeklinde değiştirmeniz gerekir
"""

simdiki_tarih=datetime.datetime.now()

def ana_menu() :
        simdiki_tarih=datetime.datetime.now()
        while tarih_bilgisi > simdiki_tarih :
            simdiki_tarih=datetime.datetime.now()
            pencere = Tk()
            pencere.title(f"Kripto Para Botu.Uygulamayı {tarih_bilgisi} Kadar Kullanabilirsiniz. ")
            pencere.geometry("1500x1200")

            label=Label(pencere)
            label.config(text="Geliştirici Bilgileri",bg="cyan",font=("Arial",13))
            label.place(x=20,y=200)

            label=Label(pencere)
            label.config(text="KEREM YAĞAN",font=("Arial",13))
            label.place(x=20,y=230)

            label=Label(pencere)
            label.config(text="İletişim E-Posta:keremyagann@gmail.com",font=("Arial",13))
            label.place(x=20,y=250)

            label=Label(pencere)
            label.config(text="Binance Referans Kimliği:59067923",font=("Arial",13))
            label.place(x=20,y=275)

            label=Label(pencere)
            label.config(text="Yeni Lisans Kodu Almak İçin Lütfen İletişime Geçiniz.",font=("Arial",13))
            label.place(x=20,y=300)

            label=Label(pencere)
            label.config(text="Banka Hesap Bilgileri",bg="yellow",font=("Arial",13))
            label.place(x=20,y=330)

            label=Label(pencere)
            label.config(text="Hesap Adı:Kerem YAĞAN",font=("Arial",13))
            label.place(x=20,y=360)

            label=Label(pencere)
            label.config(text="Banka:Ziraat Bankası",font=("Arial",13))
            label.place(x=20,y=380)

            label=Label(pencere)
            label.config(text="IBAN:TR11 1111 1111 1111 1111 11",font=("Arial",13))
            label.place(x=20,y=400)


            label=Label(pencere)
            label.config(text="İşlem Yapacağınız Site Adını Küçük Harflerle Giriniz(binance):",font=("Arial",10))
            label.place(x=20,y=20)
            islem_yapilacak_site_adi=Entry(pencere)
            islem_yapilacak_site_adi.place(x=450,y=20)

            label=Label(pencere)
            label.config(text="İşlem Yapacağınız Coin Adını Tamamını Büyük Harf İle Giriniz(XRP):",font=("Arial",10))
            label.place(x=20,y=40)
            coin_name=Entry(pencere)
            coin_name.place(x=450,y=40)


            label=Label(pencere)
            label.config(text="İşlem Yapılacak Coin Çift Adını Tamamını Büyük Harf İle Giriniz(TRY):",font=("Arial",10))
            label.place(x=20,y=60)
            coin_cifti=Entry(pencere)
            coin_cifti.place(x=450,y=60)

            label=Label(pencere)
            label.config(text="Kâr Miktarını Nokta İle Giriniz(0.05):",font=("Arial",10))
            label.place(x=20,y=80)
            kar_miktari=Entry(pencere)
            kar_miktari.place(x=450,y=80)

            label=Label(pencere)
            label.config(text="Api Bilginizi Giriniz:",font=("Arial",10))
            label.place(x=20,y=100)
            api_key=Entry(pencere)
            api_key.place(x=450,y=100)

            label=Label(pencere)
            label.config(text="Secret Api Bilgisini Giriniz:",font=("Arial",10))
            label.place(x=20,y=120)
            secret_api=Entry(pencere)
            secret_api.place(x=450,y=120)

            liste=[]
            def bilgiler():
                liste.append(islem_yapilacak_site_adi.get())
                liste.append(coin_name.get())
                liste.append(coin_cifti.get())
                liste.append(kar_miktari.get())
                liste.append(api_key.get())
                liste.append(secret_api.get())
                
                
            simdiki_tarih=datetime.datetime.now()
            buton=Button(pencere)
            buton.config(text="Onayla",bg="black",fg="white",command=bilgiler)
            buton.place(x=450,y=160)
            pencere.mainloop()
            simdiki_tarih=datetime.datetime.now()
            islem_yapilacak_site_adi=liste[0]
            coin_name=liste[1]
            coin_cifti=liste[2]
            kar_miktari=float(liste[3])
            api_key=liste[4]
            secret_api=liste[5]
            simdiki_tarih=datetime.datetime.now()
            while tarih_bilgisi > simdiki_tarih :
                simdiki_tarih=datetime.datetime.now()
                exchange_id = islem_yapilacak_site_adi
                exchange_class = getattr(ccxt, exchange_id)
                exchange = exchange_class({
                    'apiKey': api_key,
                    'secret': secret_api,
                    'timeout': 30000,
                    'enableRateLimit': True,})
                exchange_price=exchange.fetch_ticker(coin_name+'/'+coin_cifti)["info"]["lastPrice"]
                anlik_kur=float(exchange_price)
                exchange_account_balance=exchange.fetchBalance()
                hesaptaki_para=float(exchange_account_balance[coin_cifti]["free"])
                hesaptaki_coin=float((exchange_account_balance[coin_name]["free"]))
                son_siparis_dict=exchange.fetchClosedOrders(coin_name+"/"+coin_cifti)
                son_siparis=dict(list(son_siparis_dict)[-1])
                son_islem_adi=son_siparis["info"]["side"]
                son_islem_fiyati=son_siparis["price"]
                son_islem_miktari=son_siparis["amount"]
                if son_islem_adi == "SELL" : 
                    simdiki_tarih=datetime.datetime.now()
                    if (anlik_kur < son_islem_fiyati) or (anlik_kur == son_islem_fiyati) :
                        simdiki_tarih=datetime.datetime.now()
                        alim_miktari=(hesaptaki_para/anlik_kur)*99/100
                        market_alis=exchange.create_market_buy_order(coin_name+'/'+coin_cifti,alim_miktari)
                        print(f"Alım Gerçekleşti.Alınan Miktar:{alim_miktari}{coin_name} Harcanan Miktar:{hesaptaki_para}{coin_cifti} .".format(alim_miktari,coin_name,hesaptaki_para,coin_cifti))
                        simdiki_tarih=datetime.datetime.now()
                    else :
                        simdiki_tarih=datetime.datetime.now()
                        print(f"Alış İşlemi Bekleniyor.Anlık Kur:{anlik_kur} Hedeflenen Kur:{son_islem_fiyati} veya Daha Az.".format(anlik_kur,son_islem_fiyati))
                elif son_islem_adi == "BUY" :
                    simdiki_tarih=datetime.datetime.now()
                    if (anlik_kur > son_islem_fiyati+kar_miktari) or (anlik_kur == son_islem_fiyati+kar_miktari):
                        market_satis=exchange.create_market_sell_order(coin_name+'/'+coin_cifti,hesaptaki_coin)
                        print(f"Satış Gerçekleşti.Satılan Miktar:{hesaptaki_coin}{coin_name} Kazanılan Miktar:{hesaptaki_para}{coin_cifti} ".format(hesaptaki_coin,coin_name,hesaptaki_para,coin_cifti))
                        simdiki_tarih=datetime.datetime.now()
                    else :
                        print(f"Satış İşlemi Bekleniyor.Anlık Kur:{anlik_kur} Hedeflenen Kur:{son_islem_fiyati+kar_miktari} veya Daha Fazla.".format(anlik_kur,son_islem_fiyati+kar_miktari))
                        simdiki_tarih=datetime.datetime.now()
            break


if ip_adress == ip_adress : #ip bilgileri
    pencere = Tk()
    pencere.title("Lisans Onaylama")
    pencere.geometry("600x300")

    label=Label(pencere)
    label.config(text="Sistemin Çalışma Süresi Boyunca Lütfen Bilgisayarınızı Kapatmayın.",font=("Arial",13))
    label.place(x=20,y=20)

    label=Label(pencere)
    label.config(text="Lisans Kodunu Giriniz:",bg="blue",font=("Arial",10))
    label.place(x=20,y=100)
    lisans_kod=Entry(pencere)
    lisans_kod.place(x=170,y=100)
    buton=Button(pencere)

    def lisans_onaylama():
        if (lisans_kod.get() == lisans_bilgisi) and (tarih_bilgisi < simdiki_tarih) :
            label=Label(pencere)
            label.config(text="Kodun Süresi Dolmuştur.",font=("Arial",20))
            label.place(x=20,y=130)
            
        elif (lisans_kod.get() == lisans_bilgisi) and (tarih_bilgisi > simdiki_tarih) :
            pencere.destroy()
            ana_menu()

        elif not (lisans_kod.get() == lisans_bilgisi) :
            label=Label(pencere)
            label.config(text="\nGeçersiz Kod.Lütfen Tekrar Deneyiniz",font=("Arial",20))
            label.place(x=20,y=130)
            

    buton.config(text="Onayla",bg="black",fg="white",command=lisans_onaylama)
    buton.place(x=350,y=220)
    pencere.mainloop()
    

else :
    pencere = Tk()
    pencere.title(f"Kripto Para Botu")
    pencere.geometry("500x300")

    label=Label(pencere)
    label.config(text="IP Adresi Geçerli Değil.Lütfen Geliştirici İle İletişime Geçiniz.",font=("Arial",13))
    label.place(x=20,y=20)

    label=Label(pencere)
    label.config(text="Geliştirici Bilgileri",bg="cyan",font=("Arial",13))
    label.place(x=20,y=50)

    label=Label(pencere)
    label.config(text="KEREM YAĞAN",font=("Arial",13))
    label.place(x=20,y=80)

    label=Label(pencere)
    label.config(text="İletişim E-Posta:keremyagann@gmail.com",font=("Arial",13))
    label.place(x=20,y=100)

    label=Label(pencere)
    label.config(text="Binance Referans Kimliği:59067923",font=("Arial",13))
    label.place(x=20,y=125)

    pencere.mainloop()


      




    
