# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

binding = @client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                        .bindings
                        .create(
                           endpoint: 'XXXXXXXXXXXXXXX',
                           tag: 'premium',
                           address: 'gcm_device_token',
                           binding_type: 'gcm',
                           identity: '00000001'
                         )

puts binding.sid
