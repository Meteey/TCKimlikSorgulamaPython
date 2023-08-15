# TCKimlikSorgulamaPython
Python ile TC Kimlik Numarası, İsim, Soyisim ve Doğum yılı kullanılarak kullanıcının Türkiye Cumhuriyeti Vatandaşı olup olmadığını kontrol etmek için yazılmıştır. Uygulamalarda kayıt olurken kontrol için kullanılabilir. Kimlik_sorgu_server.py dosyası server üzerinden çalıştırıp dışarıdan bağlantı kurulabilir. 


Localhost üzerinden örnek bir bağlantı (Postman kullanılmıştır!)

* CMD ile dosya dizinine ulaşıp python kimlik_sorgu_server.py komutunu çalıştırdık:
  
![image](https://github.com/Meteey/TCKimlikSorgulamaPython/assets/100533901/8cf9e6d2-d766-480f-9754-a8dfd063b259)

* Postman üzerinden bir POST isteği oluşturduk ve url olarak http://127.0.0.1:5000 (Localhost ip'si üzerinden bir port) verdik:
  
  ![image](https://github.com/Meteey/TCKimlikSorgulamaPython/assets/100533901/ce697eaf-2280-4447-a079-83c991f2de2c)

* Body sekmesi üzerinde raw seçeneğine tıkladık ve yazmadan önce TEXT kısmını JSON ile değiştirdik. Daha sonra gereken verileri aşağıdaki gibi girdik:
  
  ![image](https://github.com/Meteey/TCKimlikSorgulamaPython/assets/100533901/5589929f-73d4-4849-a7dd-c5ecec84aca0)

* SEND tuşuna basarak Request'imizi gönderdik ve Response alt kısımda gözüktü:
  
  ![image](https://github.com/Meteey/TCKimlikSorgulamaPython/assets/100533901/1c4f6540-d342-4c13-8bb7-2ac5f959ca18)
  
Siz de kullandığınız projeye göre uygun kütüphaneleri edinip, localhost üzerinden veya bu programı çalıştıran bir server'a doğrudan bağlanıp id, name, surname, birthyear
değişkenlerini göndererek kişinin Türkiye Cumhuriyeti Vatandaşı olup olmadığını kontrol edebilirsiniz.
