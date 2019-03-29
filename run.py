# /usr/bin/python3

# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("I got your message!")
    
    inbound_message = request.form.get("Body")
    print(type(request))
    for key in request.form:
        print(key)
    print("AFTER LOOP")
    #print(request.form.keys)

    return str(resp)
    """
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message("I got your message!")
    print(request.form)
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)"""

if __name__ == "__main__":
    app.run(debug=True)
