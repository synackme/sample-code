# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

service = client.sync.services.create(
                                   friendly_name="MySyncServiceInstance",
                                   webhook_url="https://example.com/sync"
                               )

print(service.sid)
