from django.core.management.base import BaseCommand
import pika
from broker.models import Userbroker
from backend.models import Referral
import json

class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer to process messages'

    def handle(self, *args, **kwargs):

        def callback(ch, method, properties, body):

            print(f"Received: {body}")

            try:
                # Decode the byte string into a regular string
                decoded_message = body.decode('utf-8')

                message = eval(decoded_message)

                print(f"Decoded Message: {message}")

                id=message.get('id')
                email = message.get('email')
                token = message.get('token')
                uuid=message.get('uuid')
                if token:
                    try:
                        token=Referral.objects.get(code=token)
                    except:
                        token=None
                        print("Token not exist")
                if email and uuid and id:
                    Userbroker.objects.get_or_create(id=id,email=email,uuid=uuid,broker_ref=token)



                else:
                    print("Not provided")

            except Exception as e:
                print(f"Error processing message: {e}")

        def transaction(ch, method, properties, body):
            print(f"Received: {body}")



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
            channel.queue_declare(queue='transactions',durable=True)
            channel.basic_consume(
                queue='transactions', on_message_callback=transaction, auto_ack=True
            )



            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        start_consumer()
