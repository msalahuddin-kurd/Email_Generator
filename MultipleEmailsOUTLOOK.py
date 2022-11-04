import time
from traceback import print_tb
import win32com.client
import os

load_dotenv()

TO = ""
SUBJECT = ""    
C_File = ""

emails = []
with open(C_File) as f:                                                                                                                                                                                       
    emails = f.readlines() 

count = 0
msg = ""
for email in emails:
        count += 1
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = emails
        mail.Subject = SUBJECT 
        mail.Body = msg
        mail.Send()
        print(msg)
        print("Email Sent "+ str(count))
        time.sleep(25)

print("All Messages sent")