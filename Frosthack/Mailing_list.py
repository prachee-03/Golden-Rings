import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

class mailing :

    def read_template(self,filename):
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    """def get_contacts(filename,e_id):
        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                if a_contact[5]==e_id:
                    names.append(a_contact.split()[0])
                    emails.append(a_contact.split()[1])
        return names, emails  """


    def mail_part_reg (self,pname,ename,d,t,p_id,e_id,hmail,pmail,hname) :
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("goldenrings.2020@gmail.com","straightofthecouch")
        
        message_template = self.read_template('part_reg_msg.txt')
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=pname,Event_name=ename,Date=d,time=t,part_id=p_id,
        event_id=e_id,host_email=hmail)
        msg['From']="goldenrings.2020@gmail.com"
        msg['To']=pmail
        msg['Subject']="Registration successful"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg

        message_template = self.read_template('part_enroll.txt')
        msg2 = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=hname,par_name=pname,Event_name=ename)
        msg2['From']="goldenrings.2020@gmail.com"
        msg2['To']=hmail
        msg2['Subject']="New registration for your event"
        msg2.attach(MIMEText(message, 'plain'))
        s.send_message(msg2)
        del msg2

        

    """def mail_host_reg (hname,ename,e_id,hmail) :
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("goldenrings.2020@gmail.com","straightofthecouch")
        message_template = read_template('org_reg_msg.txt')

        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=hname,Event_name=ename,event_id=e_id)
        msg['From']="goldenrings.2020@gmail.com"
        msg['To']=hmail
        msg['Subject']="Event registered successfully"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg

    def mail_meetlink (ename,d,t,slink,e_id) :
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("goldenrings.2020@gmail.com","straightofthecouch")
        message_template = read_template('meetlink_msg.txt')
        names, emails = get_contacts('part_record.txt',e_id)

        for name, email in zip(names, emails):
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=name,Event_name=ename,Date=d,time=t,stream_link=slink)
            msg['From']="goldenrings.2020@gmail.com"
            msg['To']=email
            msg['Subject']="Stream link for your registered event"
            msg.attach(MIMEText(message, 'plain'))
            s.send_message(msg)
            del msg
    """


