# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

address = @client.addresses.create(
                              friendly_name: 'Billing - Customer 123',
                              city: 'Berlin',
                              customer_name: 'Customer 123',
                              iso_country: 'DE',
                              postal_code: '10875',
                              region: 'Berlin',
                              street: '1 Hasselhoff Lane'
                            )

puts address.sid
