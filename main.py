import smtplib
import ssl
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "guptamahak1702@gmail.com"
sender_password = "mbkotxmhoqgdpgtw"
subject = "CodeSpire mail sending"  



# df = pd.DataFrame(
#     {
#         "email": [
#             "mahakgupta210013@acropolis.in",
#             "yashhguptaa.917@gmail.com",
#         ],
#         "phone": [
#             8768646,
#             87498546,
#         ],
#     }
# )



# print(df['email'][0])
# df.to_csv('email.csv',index=False)

info = pd.read_excel('email.xlsx')
li=info["email"].tolist()
print(li)

# info = pd.read_csv('email.csv')
# li=info['email'].tolist()
# print(li)


message = MIMEMultipart("alternative")
message['Subject'] = subject
message['From'] = sender_email
# message['To'] = li

with open('message.txt',encoding='utf-8') as m:
    msg = m.read()
part1 = MIMEText(msg,"plain")
# part2 = MIMEText(html,"html")

message.attach(part1)
# message.attach(part2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,li,message.as_string())

print("send successful")







