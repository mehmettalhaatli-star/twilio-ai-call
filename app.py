from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
    print("Türkçe arama geldi!")  # Log için
    
    response = """
    <Response>
        <Say language="tr-TR" voice="Polly.Filiz">
            Merhaba! Ben yapay zeka asistanınızım. Yeni konut projemiz hakkında bilgi vermek için arıyorum.
        </Say>
        <Pause length="2"/>
        <Say language="tr-TR" voice="Polly.Filiz">
            Projemiz İstanbul Ataşehir'de yer alıyor. 2 artı 1 ve 3 artı 1 daire seçeneklerimiz mevcut.
        </Say>
        <Pause length="1"/>
        <Say language="tr-TR" voice="Polly.Filiz">
            Detaylı bilgi için sizi satış temsilcimize bağlıyorum. İyi günler dilerim.
        </Say>
    </Response>
    """
    return Response(response, mimetype='text/xml')

@app.route('/')
def home():
    return "Sunucu çalışıyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
