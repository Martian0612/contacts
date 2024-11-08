# import requests

# def send_otp_to_phone(phone_number):
#     url = ''
#     response = requests.get(url)

from django.conf import settings
from twilio.rest import Client
import random

class MessaHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        message = client.messages.create(
                        body= f'Your otp is {self.otp}',
                        from_ ='+917389560834',
                        to = self.phone_number
                    )
        print(message.sid)