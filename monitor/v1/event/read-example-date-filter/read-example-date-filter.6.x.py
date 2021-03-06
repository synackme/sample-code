# Download the helper library from https://www.twilio.com/docs/python/install
from datetime import date
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

events = client.monitor.events.list(
                                   end_date=date(2015, 4, 1),
                                   start_date=date(2015, 3, 1)
                               )

for record in events:
    print(record.sid)
