import imaplib
import email
#Note u need to enable imap feature in google advanced settings and even low seccurity access setting
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('Enter the gmail account from where data is to be extracted','Enter the password for that account')

mail.select('Zomato')#This is the label under which you want to read all the mails from
result, data = mail.uid('search', None, "ALL")
# search and return uids instead
i = len(data[0].split()) # data[0] is a space separate string

for x in range(i):
 latest_email_uid = data[0].split()[x] # unique ids wrt label selected
 result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
 # fetch the email body (RFC822) for the given ID
 raw_email = email_data[0][1]
 
 
 #continue inside the same for loop as above
 #continue inside the same for loop as above
 raw_email_string = raw_email.decode('utf-8')
 # converts byte literal to string removing b''
 email_message = email.message_from_string(raw_email_string)
 
 
 # this will loop through all the available multiparts in mail
 for part in email_message.walk():
    
  if part.get_content_type() == "text/html": # use != to ignore attachments/html,however the data I needed to extract were in html format
   body = part.get_payload(decode=True)
   save_string = str("Dumpgmailemail_" + str(x) + ".eml")
   # location on disk
   myfile = open(save_string, 'a')
   myfile.write(body.decode('utf-8'))
   
   # body is again a byte literal
   myfile.close()
   
  else:
   continue
