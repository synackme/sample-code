# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

media = client.messages("MM800f449d0399ed014aae2bcc0cc2f2ec").media.list()

for record in media:
    print(record.sid)
