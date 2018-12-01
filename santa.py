from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
import base64
import random
from retrying import retry

# If you want the emails to send set to True
SEND = True

# Your browser will pop up asking you to authorize your
# gmail account, put your email that you authorized here
YOUR_EMAIL = "email@domain.com"

# The name of the input file separated by |
INPUT = "santa.txt"

# The name of the output file so you can keep track of who the assignments
OUTPUT = "assignments.csv"

# Change format_email if you want to change the content of the email

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.send'


def format_email(gifter, receiver):
    """ Change this if you modified the data file (all the santa information)
 format of file would be name|email|likes
 resulting array ["name", "email", "likes"]
 gifter and reciever are both arrays like described above
 """
    gifterName = gifter[0]
    recieverName = receiver[0]
    recieverLike = receiver[2]

    # Change this email however you like.
    email = "Hi " + gifterName + ",\n\n" \
        + "Your Secret Santa/Gift Exchange 2k17 Assignment is " + recieverName\
        + "! :O\n\nHere are their interests from the Catalyst Survey:\n"\
        + recieverLike + "\n\nPlease remember the cap is $20. Your goal is to find a "\
        + "heartfelt gift, something inexpensive and thoughtful "\
        + "is the way to go.\n\n"\
        + "Happy Thanksgiving and good luck finding the perfect gift for " + recieverName + "! :)"
    return email, gifterName, recieverName


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('cred/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    print(creds)

    f = open(INPUT, "r")
    santa = []
    for line in f:
        person = line.split("|")
        santa.append(person)
    f.close()
    random.shuffle(santa)
    f = open(OUTPUT, "w")

    i = 0
    while (i < len(santa) - 1):
        email, gifterName, recieverName = format_email(santa[i], santa[i + 1])
        gifterEmail = santa[i][1]
        subject = "Secret Santa"
        create_and_send_email(service, gifterEmail, subject, email)
        f.write(gifterName + "," + recieverName + "\n")
        print("email sent to " + gifterEmail + "\n")
        i = i + 1
    email, gifterName, recieverName = format_email(santa[-1], santa[0])
    gifterEmail = santa[-1][1]
    subject = "Secret Santa"
    f.write(gifterName + "," + recieverName + "\n")
    create_and_send_email(service, gifterEmail, subject, email)
    print("email sent to " + gifterEmail + "\n")
    f.close()


def create_and_send_email(service, gifterEmail, subject, email):
    if (SEND):
        message = create_message(YOUR_EMAIL,
                                 gifterEmail, subject, email)
        send_message(service, YOUR_EMAIL, message)
    else:
        print("Would have sent to " + gifterEmail)
        print(email)


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


@retry
def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """

    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    return message


if __name__ == '__main__':
    main()
