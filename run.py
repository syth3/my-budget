# /usr/bin/python3

# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    
    number = request.form['From']
    message_body = request.form['Body']
    
    # Start our response
    resp = MessagingResponse()
    #resp.message("I got your message!")
    for key in request.form:
        print(key + ": " + request.form[key])
    print("REQUEST:", request)
    resp.message("Hello {}, you said: \n\n{}".format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
