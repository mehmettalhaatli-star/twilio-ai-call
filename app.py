from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    print("Twilio arama geldi!")  # Log için
    
    response = """
    <Response>
        <Say language="tr-TR" voice="woman">Merhaba! Test aramasına hoş geldiniz.</Say>
        <Pause length="1"/>
        <Say language="tr-TR" voice="woman">Bu bir yapay zeka testidir. İyi günler dilerim.</Say>
    </Response>
    """
    return Response(response, mimetype='text/xml')

@app.route('/')
def home():
    return "Sunucu çalışıyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
