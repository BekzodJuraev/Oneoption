from django.core.management.base import BaseCommand
import pika
from broker.models import Userbroker
import json

class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer to process messages'

    def handle(self, *args, **kwargs):
        def callback(ch, method, properties, body):
            message = json.loads(body)
            email = message.get('email')
            if email:
                try:
                    Userbroker.objects.create(email=email)
                    print(f"Created Userbroker record with email: {email}")
                except:
                    print("user has")

            else:
                print("No email field found in message")

            # Process the message here

        def start_consumer():
            credentials = pika.PlainCredentials('root', '123')
            parameters = pika.ConnectionParameters('86.48.7.247', 5672, '/', credentials)

            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # Declare the queue from which the consumer will receive messages
            channel.queue_declare(queue='user_registration',durable=True)

            channel.basic_consume(
                queue='user_registration', on_message_callback=callback, auto_ack=True
            )

            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        start_consumer()
