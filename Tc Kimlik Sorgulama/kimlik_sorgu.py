import requests
import xmltodict
import json

tcid = input("Tc Kimlik Numarası: ")
name = input("İsim: ")
surname = input("Soy isim: ")
birthyear = input("Doğum yılı :")


url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"
payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <TCKimlikNo>{tcid}</TCKimlikNo>
          <Ad>{name}</Ad>
          <Soyad>{surname}</Soyad>
          <DogumYili>{birthyear}</DogumYili>
        </TCKimlikNoDogrula>
      </soap12:Body>
    </soap12:Envelope>"""
    # headers
headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8',
        'Host': 'tckimlik.nvi.gov.tr',

    }

response = requests.request("POST", url, headers=headers, data=payload)
data_dict = xmltodict.parse(response.text)

result = data_dict['soap:Envelope']['soap:Body']['TCKimlikNoDogrulaResponse']['TCKimlikNoDogrulaResult']
print("Kayıtlı") if result == "true" else print("Kayıtlı değil")