from flask import Flask, request, Response
import openai
import os
import json

app = Flask(__name__)

# OpenAI ayarları
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/voice', methods=['POST'])
def voice():
    try:
        # Twilio'dan gelen aramayı işle
        response = """
        <Response>
            <Say language="tr-TR">Merhaba! Size yeni konut projemiz hakkında bilgi verebilir miyim?</Say>
            <Pause length="2"/>
            <Say language="tr-TR">Projemiz İstanbul Ataşehir'de 2+1 ve 3+1 dairelerden oluşmaktadır.</Say>
            <Pause length="1"/>
            <Say language="tr-TR">Detaylı bilgi için sizi satış temsilcimize bağlıyorum. İyi günler dilerim.</Say>
        </Response>
        """
        return Response(response, mimetype='text/xml')
    
    except Exception as e:
        print(f"Hata: {str(e)}")
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
