#Program to delete emails.

import imaplib
import sys
import re


arguments = sys.argv


if len(sys.argv) == 4:
        my_email_addr = re.sub(r"\s+", "", arguments[1])
        if my_email_addr.find("@") != -1:
            my_email = my_email_addr
        else:
            print ("Email Not found!")
            sys.exit()
else: 
    print("\nplease enter the correct data: ('Email Password Search. \n Example: myemail@gmail.com Mypassword spam@super_spam.com')\n")
    sys.exit() 

try:
    app_password = arguments[2]
except:
    print("The Password was entered incorrectly") 
    sys.exit()
else:
    pass

try:
    del_from_value = arguments[3]
except:
    print("The search was entered incorrectly\n") 
    sys.exit()
else:
    pass




#initialize IMAP object for Gmail
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#login to gmail with credentials
imap.login(my_email, app_password)

imap.select("INBOX")

status, message_id_list = imap.search(None, 'FROM "' + del_from_value + '"')

#convert the string ids to list of email ids
messages = message_id_list[0].split(b' ')

print("Deleting mails")
count =1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1
print("All selected mails have been deleted")

# delete all the selected messages 
imap.expunge()
# close the mailbox
imap.close()

# logout from the account
imap.logout()