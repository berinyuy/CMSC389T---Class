from twilio.rest import Client 
 
account_sid = 'ACc9ffe12f6a3fdeb90d96d23aede4f1c5' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
                              to='+12404810166' 
                          ) 
 
print(message.sid)