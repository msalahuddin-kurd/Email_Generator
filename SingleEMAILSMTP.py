import smtplib

server = ""
port = ""

to = 'sender'
user = 'receiver'
smtpserver = smtplib.SMTP(server,port)
smtpserver.ehlo()
smtpserver.ehlo
header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:testing \n'
print (header)
msg = header + '\n this is test msg  \n\n'
smtpserver.sendmail(user, to, msg)
print ('done!')
smtpserver.close()
