# -*- coding: cp1252 -*-
import sfmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

os.system("Title")

smtpServer = "";
smtpPort = ;
smtpUsername = "";
fromAddress = "";
toAddress = "";
ccAddress = "";

for x in range(3):
    try:
        mailServer = smtplib.SMTP(smtpServer , smtpPort)
        mailServer.starttls()
        if x == 2:
            exit()
        smtpPassword = raw_input("Please enter password: ") 
        mailServer.login(smtpUsername , smtpPassword)
        print("Authentication successful")
        break
    except:
        if x == 1:
            print("Password incorrect. This application will now close")
        else:
            print("Password incorrect. Please try again.")
            
# Take the day and dates from user
day=''
day2=''
date=''
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while day != days:
    day=raw_input("Please enter day of DEV patching: ")
    if day not in days:
        print("That is not a day of the week. Please try again")
    else:
        break
st=("01", "21", "31")
nd=("02", "22")
th=("04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "24", "25", "26", "27", "28", "29", "30")
rd=("03", "23") 

date=raw_input("Please enter date for " +day+": ")
if date in st:
    date += "st"
elif date in nd:
    date += "nd"
elif date in th:
    date += "th"
elif date in rd:
    date += "rd"
else:
    print
    print("Please only enter a valid date. This program will now stop")
    time.sleep(2)
    exit()
print
print
print("You have choosen " + day + " the " + date)
print


#Seperating the Ordinal indicator from the date
datesplit=date[0:2]
datesplit1=date[2:4]

while day2 != days:
    day2=raw_input("Please enter day for all remaining system patching: ")
    if day2 not in days:
        print("That is not a day of the week. Please try again")
    else:
        break
date2=raw_input("Please enter date for " +day2+": ")
if date2 in st:
    date2 += "st"
elif date2 in nd:
    date2 += "nd"
elif date2 in th:
    date2 += "th"
elif date2 in rd:
    date2 += "rd"
else:
    print
    print("Please only enter a valid date. This program will now stop")
    time.sleep(2)
    exit()
print
print("You have choosen " + day2 + " the " + date2)
print

#Seperating the Ordinal indicator from the date
datesplit2=date2[0:2]
datesplit3=date2[2:4]


confirm=raw_input("Are you sure you want to proceed. Type Y or N?: ")

if confirm == 'Y':
    pass
elif confirm == 'N':
        exit()
#else:
    #       exit()

# Create the body of the message (HTML version).

html = """\
<html>
  <head></head>
  <body>

  Insert HTML here
    
  </body>
</html>
"""




htmlDevelopment = """\
<html>
  <head></head>
  <body>


  Insert HTML here

  </body>
</html>
"""

# email object that has multiple part:
msg = MIMEMultipart()
msg['From'] = fromAddress
msg['To'] = toAddress
msg['CC'] = ccAddress
msg['Subject'] = "Enter subject here"

msg2 = MIMEMultipart()
msg2['From'] = fromAddress
msg2['To'] = toAddress
msg2['CC'] = ccAddress
msg2['Subject'] = "Enter subject here"


# Record the MIME types of both parts - text/plain and text/html.
"""part1 = MIMEText(text, 'plain')"""
part2 = MIMEText(html, 'html')
part3 = MIMEText(htmlDevelopment, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part2)
msg2.attach(part3)

mailServer = smtplib.SMTP(smtpServer , smtpPort)
#mailServer.set_debuglevel(1)    #Please only enable this if the program stops working.
mailServer.starttls()
mailServer.login(smtpUsername , smtpPassword)
mailServer.sendmail(fromAddress, toAddress.split(",") , msg.as_string())
mailServer.sendmail(fromAddress, toAddress.split(",") , msg2.as_string())
print
print("Your email has been successfully sent!. This window will now close.")
time.sleep(3)
mailServer.quit()


