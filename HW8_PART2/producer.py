import pika
import connection
from faker import Faker
from models import Contacts

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='marketing_campaign_email')

def generate_contacts(num_contacts):
    faker = Faker()
    for i in range(num_contacts):
        full_name = faker.name()
        email = faker.email()
        contact = Contacts(fullname=full_name, email=email)
        contact.save()
        message = str(contact.id)
        channel.basic_publish(exchange='', routing_key='marketing_campaign_email', body=message)
        print(f'Contact {i+1} added to the queue')

generate_contacts(40)

connection.close()