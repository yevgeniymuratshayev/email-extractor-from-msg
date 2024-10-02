# pip install extract-msg
# pip install imapclient
import extract_msg
import os
import re
from os import listdir
from os.path import isfile, join

mypath = 'C:/Users/username/Downloads/mail0'  # Replace with yours
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
arEmails = []
n = 0
for f in onlyfiles:
    email_file_splt = f.split(".")
    if email_file_splt[1] != "msg":
        continue
    msg = extract_msg.Message(f)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = format(msg.body)
    msg.close()

    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", msg_message)
    arEmails.append(emails)

text = ""

for i in arEmails:
    for j in i:
        text += j + "\n"

file = open("emails.txt", "w")
file.write(text)
file.close()