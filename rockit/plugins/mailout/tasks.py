import smtplib

from celery import task

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from rockit.plugins.mailout import models
from rockit.plugins.mailout import serializers

from smtplib import SMTPException

@task(name='mailout.settings')
def settings(holder):
    for setting in models.Setting.objects.all():
      holder.add(**{
        'key': setting.id,
        'name': setting.name,
        'value': setting.value
      })

    return holder

@task(name='mailout.mixes')
def mixes(holder):
    holder.add_finish(**{ 'identifier': 'mailout', 'name': 'Send out mail' })
    return holder

@task(name='mailout.mixes.details')
def mixes_details(identifier, holder):

    holder.add_post(**{
        'identifier': 'recipients',
        'type': 'text',
        'label': 'Recipients',
        'required': True
    })

    holder.add_post(**{
        'identifier': 'subject',
        'type': 'text',
        'label': 'Subject',
        'required': True
    })

    holder.add_post(**{
        'identifier': 'message',
        'type': 'textarea',
        'label': 'Message',
        'required': True
    })

    return holder

@task(name='mailout.mixes.finish.create')
def mixes_create(uuid, criterias):

    if criterias:

        subject = criterias['subject']['value']
        message = criterias['message']['value']

        mailout = models.Mailout.objects.create(subject=subject, message=message)

        for recipient in criterias['recipients']['value'].split(','):
            models.MailoutRecipient.objects.create(mailout=mailout, recipient=recipient)

        return mailout.id

    return None

@task(name='mailout.mixes.finish.run')
def mixes_run(identifier):
    logger = mixes_run.get_logger()

    mailout = models.Mailout.objects.get(id=identifier)

    sender = "rockitserver@acreations.se"

    # Get all receivers
    receivers = []

    for recipient in models.MailoutRecipient.objects.filter(mailout=mailout):
        receivers.append(recipient.recipient)

    body = mailout.message.encode('utf-8')

    message = MIMEMultipart()

    message['From'] = sender
    message['To']   = ','.join(receivers)
    message['Subject'] = mailout.subject
    message.attach(MIMEText(body, 'plain'))

    try:
        smtpObj = smtplib.SMTP("mailout.comhem.se:587")
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.close()

        logger.info("Successfully sent email")

        return True
    except SMTPException, e:
        logger.error("Unable to send email %s", e)

    return False

@task(name='mailout.mixes.finish.validate')
def mixes_validate(identifier, criterias, holder):

    if criterias:

        if criterias['recipients'] and criterias['recipients']['value']:
            for recipient in criterias['recipients']['value'].split(','):
                try:
                    validate_email(recipient)
                except ValidationError:
                    holder.add_error(recipient, 'Is not a valid email')
        else:
            holder.add_error('recipients', 'Value must be provided')

    else:
        holder.add_error('mailout', 'Value must be provided')

    return holder