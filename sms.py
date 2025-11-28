from twilio.rest import Client

ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

TWILIO_NUMBER = "+12312658290"
MY_NUMBER = "+917597702550"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello from Twilio!",
    from_=TWILIO_NUMBER,
    to=MY_NUMBER
)

print(message.sid)

