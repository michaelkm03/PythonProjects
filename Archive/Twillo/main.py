from twilio.rest import TwilioRestClient

phone_num = '9494669781'
words = raw_input('Enter Text to Send:  ')
c = 0
with open("upload.txt") as f:
    body = f.readlines()
    bulk = ''.join(body)

# put your own credentials here
ACCOUNT_SID = 'ACf2d831024466da45edecc9408e380d81'
AUTH_TOKEN = 'e1886aeb94f772eaea637a0c56197564'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# client.messages.create(
#     to = phone_num,
#     from_ = '19495369381',
#     body = bulk,
# )
count = 0
while count < 5:
    client.messages.create(
        to = phone_num,
        from_ = '19495369381',
        body = words ,"this is number %s" % count,
    )
    count+=1