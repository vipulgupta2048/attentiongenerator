import random
import os
from flask import Flask, render_template
from twilio.rest import Client
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/attention')
def attention():
    random_code = random.randint(10000000, 93452300)
    random_code = str(random_code)
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token = ""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="whatsapp:",
        from_="whatsapp:+14155238886",
        body="Your {{1}} code is {{2}}")
    return render_template("attention.html", random_code=random_code)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
