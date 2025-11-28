from twilio.rest import Client

ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

TWILIO_NUMBER = "+12312658290"
MY_NUMBER = "+917597702550"

client = Client(ACCOUNT_SID, AUTH_TOKEN)


call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml", 
    to=MY_NUMBER,
    from_=TWILIO_NUMBER
)

print(f"Call initiated with SID: {call.sid}")
