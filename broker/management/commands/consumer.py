from django.core.management.base import BaseCommand
import pika
from broker.models import Userbroker
from backend.models import Referral,Click_Referral
import json

class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer to process messages'

    def handle(self, *args, **kwargs):
        def callback(ch, method, properties, body):
            message = json.loads(body)
            email = message.get('email')
            uuid = message.get('uuid')

            # Validate UUID
            if not uuid:
                print("UUID not found in the message")
            else:
                ref_broker = Referral.objects.filter(code=uuid).first()


                # Check if ref_broker exists
                if not ref_broker:
                    print("Referral with the provided UUID not found")
                elif email:
                    # Validate email by checking if a Userbroker record already exists
                    if Userbroker.objects.filter(email=email, ref_broker=ref_broker).exists():
                        print("Userbroker record with this email already exists")
                    else:
                        Click_Referral.objects.create(referral_link=ref_broker)
                        Userbroker.objects.create(email=email, ref_broker=ref_broker)
                        print(f"Created Userbroker record with email: {email}")
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
