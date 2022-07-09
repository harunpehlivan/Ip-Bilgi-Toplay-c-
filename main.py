import requests #! Requests kütüphanesini dosyamıza dahil ediyoruz.

def check(): #!Eğerki site çevrimdışı değilse sıkıntı çıkmasın diye serverın online olup olmadığını kontrol edeceğimiz bir fonksiyon belirliyoruz.
    r = requests.get("https://ipinfo.io/") #! Veri çekeceğimiz siteye get isteği atıyoruz.
    if r.status_code == 200: #! Eğerki dönen response(cevap) kodu 200 olur ise bunları yap diyen bir if kontrolü yazıyoruz.
        print("\n[+] Sunucu Çevrimiçi!\n") #! İf kontrolü olumlu olursa bu mesajı yazdırıyoruz.
    else: #! Tam dersi durumunda ise aşağıdaki kodları uygula diyoruz.
        print("\n[!] Sunucu Çevrimdışı!\n") #! İf kontrolü olumsuz ise çevrimdışı yazdırıyoruz.
        exit() #! Çıkış yapıyoruz

ip = input("Lütfen hedef ip giriniz: ") #! Kullanıcıdan ip adresini istiyoruz.

check() #! Web site kontrol fonksiyonumuzu çağırıyoruz.

country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text #! {} kullanarak ip adresini yazdırıp hedeften .text fonksiyonu ile yazıyı çekiyoruz.
city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text #! Aynı işlemleri uyguluyoruz.
region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text

#! Alt tarafta ise verileri yazdırıyoruz.
print("İp: "+ip)
print("Ülke: "+country)
print("Şehir: "+city)
print("Bölge: "+region)
print("Posta Kodu: "+postal)
print("Zaman Dilimi: "+timezone)
print("Organizasyon: "+orgination)
print("Lokasyon: "+location)