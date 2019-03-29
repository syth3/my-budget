#! /usr/bin/python3

"""
file: send_sms.py
language: python3
author: Jacob Brown https://github.com/ew0k
description: functions used to send sms
"""

import sys
import os
from twilio.rest import Client

def send_sms(body_text, sender, reciever):
    """
    Send SMS to an approved phone number (per twilio's allowance).
    NOTE: sender and receiver should be 11 digits long (country code +
    area code + 7 digit phone number) with NO extra characters (such as a dash).
    An example would be 14745852962
    :param body_text: string, text to send in the text message
    :param sender: int, phone number to send text message from
    :param receiver: int, phone number to send text message to
    """
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(body=body_text, from_=sender, to=reciever)
    return message

if __name__ == "__main__":
    # Test Input
    if len(sys.argv) != 4:
        print(sys.argv)
        if sys.argv[1] == "help" or sys.argv[1]  == "--help" or sys.argv[1] == "--h" or sys.argv[1] == "-h":
            print("Usage: ./send-sms.py \"Text to send goes in quotes\" send_num recv_num")
            print("Example: ./send-sms.py \"Send me!\" 16871295324 12847628462")
            exit(0)
        else:
            print("Error, did not send")
            print("Usage: ./send-sms.py \"Text to send goes in quotes\" send_num recv_num")
            print("Example: ./send-sms.py \"Send me!\" 16871295324 12847628462")
            exit(1)
    if str.isdigit(sys.argv[1]) or not str.isdigit(sys.argv[2]) or not str.isdigit(sys.argv[3]):
        print("Error, did not send")
        print("Usage: ./send-sms.py \"Text to send goes in quotes\" send_num recv_num")
        print("Example: ./send-sms.py \"Send me!\" 16871295324 12847628462")
        exit(1)
    if len(sys.argv[2]) != 11 or len(sys.argv[3]) != 11:
        print("ERROR: send_num, recv_num, or both are not the proper amount of digits. Did not send")
        print("Format: country code + area code + 7-digit phone number")
        print("Example: 16865973392")
        exit(1)

    # Send Message
    body_text = sys.argv[1]
    send_num = sys.argv[2]
    recv_num = sys.argv[3]
    message = send_sms(body_text, send_num, recv_num)
    print(message.sid)
