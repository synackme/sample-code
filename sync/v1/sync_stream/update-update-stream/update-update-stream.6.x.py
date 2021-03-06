# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

sync_stream = client.sync.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                         .sync_streams("MyStream") \
                         .update(ttl=864000)

print(sync_stream.unique_name)
