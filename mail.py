from pygmail import Mail
import argparse

sender = "email address of the sender"
app_pass = "app password for gmail"
receiver = "email address of the receiver"
subject = "Some subject"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sub", help = "Subject")
    parser.add_argument("--body", help = "Body")
    parser.add_argument("--sendafter", help = "Time Interval to Send the mail After (format HhMmSs)")

    args = parser.parse_args()

    m = Mail(sender, app_pass, receiver, subject, "HELLOWORLD")

    if args.sub:
        m.subject = args.sub
    if args.body:
        m.body = args.body
    if args.sendafter:
        m.sendafter(args.sendafter)
    else:
        m.send()


