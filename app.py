from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

# Configure a API Key do OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg:
        # Chamada para a API da OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=incoming_msg,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()
        msg.body(reply)
    else:
        msg.body('Desculpe, não entendi sua mensagem.')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
