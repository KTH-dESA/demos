import smtplib
from csv import DictReader
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    """Formulates an e-mail and sends it
    """
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def get_text(name):
    text = """
Dear {},

I am writing to you on behalf of Prof. Boffin and the MASSIVE Consortium regarding our response to the Horizon 2020 research call.

We look forward to your response.

Kind regards,

Mr. Brainiac


""".format(name)
    return text

with open("./mailing/recipients.csv") as csvfile:
    reader = DictReader(csvfile, fieldnames=['name', 'email'])

    next(reader)
    for index, row in enumerate(reader):

        email = row['email']
        print("This email will be sent to {}".format(email))
        send_mail('wusher@kth.se',
                  [email],
                  "Request for a letter of support",
                  get_text(row['name']),
                  files=[],
                  server='smtp.kth.se')