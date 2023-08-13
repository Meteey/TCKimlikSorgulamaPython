from flask import Flask, request
import requests
import json
import xmltodict


app = Flask(__name__)


@app.route('/tckimlik', methods=['POST'])
def idcheck():
    data = request.json
    if data is not None:
        name = data['name']
        surname = data['surname']
        id = data['id']
        birthyear = data['birthyear']
    else:
        name = "John"
        surname = "Doe"
        id = 123456789
        birthyear = 1000

    url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"
    # structured XML
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <TCKimlikNo>{id}</TCKimlikNo>
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
    # POST request
    response = requests.request("POST", url, headers=headers, data=payload)
    data_dict = xmltodict.parse(response.text)
    json_data = json.dumps(data_dict)
    result = data_dict['soap:Envelope']['soap:Body']['TCKimlikNoDogrulaResponse']['TCKimlikNoDogrulaResult']
    return True if result == "true" else False


if __name__ == '__main__':
    app.run()
