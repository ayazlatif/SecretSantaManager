import smtplib
import os
import random
import argparse

def send_email(subject, body, send_to):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ.get('SECRET_SANTA_EMAIL'), os.environ.get(('SECRET_SANTA_PASS')))

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(os.environ.get('SECRET_SANTA_EMAIL'), send_to, msg)

def format_email(gifter, receiver):
    """ Change this if you modified the data file (all the santa information)
    format of file would be name|email|likes
    resulting array ["name", "email", "likes"]
    gifter and reciever are both arrays like described above
    """
    gifterName = gifter[0]
    recieverName = receiver[0]
    recieverLike = receiver[2]
    #receiverDislike = receiver[3]
    #receiverOther = reciever[4]

    # Change this email however you like.
    email = "Hi " + gifterName + ",\n\n" \
        + "Your Secret Santa/Gift Exchange 2k19 Assignment is " + recieverName\
        + "! :O\n\nHere are their likes from the Secret Santa Survey:\n"\
        + recieverLike + "\n\nPlease remember the cap is $15. Your goal is to find a "\
        + "heartfelt gift, something inexpensive and thoughtful "\
        + "is the way to go.\n\n"\
        + "Happy Thanksgiving and good luck finding the perfect gift for " + recieverName + "! :)"
    return email, gifterName, recieverName

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', default='santa.txt',
                        help='name of input file (separated by |\'s)')
    parser.add_argument('--output', default='output.txt',
                        help='name of output file (list of assignments)')
    parser.add_argument('--s', help='Include this flag if you want to send',
    action='store_true')


    args = parser.parse_args()
    f = open(args.input, "r")
    santa = []
    for line in f:
        person = line.split("\t")
        santa.append(person)
    f.close()
    random.shuffle(santa)
    f = open(args.output, "w")

    i = 0
    while (i < len(santa) - 1):
        email, gifterName, recieverName = format_email(santa[i], santa[i + 1])
        gifterEmail = santa[i][1]
        subject = "Secret Santa"
        if args.s:
            send_email(subject, email, gifterEmail)
        else:
            print('gifter:%s, reciever:%s, gifterEmail%s\nemail:%s' % (gifterName, recieverName, gifterEmail, email))
        f.write(gifterName + "," + recieverName + "\n")
        print("email sent to " + gifterEmail + "\n")
        i = i + 1
    
    email, gifterName, recieverName = format_email(santa[-1], santa[0])
    gifterEmail = santa[-1][1]
    subject = "Secret Santa"
    if args.s:
        send_email(subject, email, gifterEmail)
    else:
        print('gifter:%s, reciever:%s, gifterEmail%s\nemail:%s' % (gifterName, recieverName, gifterEmail, email))
    f.write(gifterName + "," + recieverName + "\n")
    print("email sent to " + gifterEmail + "\n")
    f.close()

if __name__ == '__main__':
    main()