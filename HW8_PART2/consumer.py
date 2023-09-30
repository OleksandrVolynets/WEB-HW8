import pika
from models import Contacts
import connection

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='marketing_campaign_email')

def send_email(email):
    print(f'Sending email to {email}...')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contacts.objects.get(id=contact_id)
    if not contact.email_sent:
        send_email(contact.email)
        contact.email_sent = True
        contact.save()
        print(f'Email sent to {contact.email}')

channel.basic_consume(queue='marketing_campaign_email', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')

channel.start_consuming()