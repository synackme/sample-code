# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url="http://demo.twilio.com/docs/voice.xml",
                        from_="+15005550006",
                        to="+14108675310"
                    )

print(call.sid)
