from django.core.management.base import BaseCommand
import pika


class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer to process messages'

    def handle(self, *args, **kwargs):
        def callback(ch, method, properties, body):
            print(f"Received {body}")

            # Process the message here

        def start_consumer():
            credentials = pika.PlainCredentials('root', '123')
            parameters = pika.ConnectionParameters('86.48.7.247', 5672, '/', credentials)

            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # Declare the queue from which the consumer will receive messages
            channel.queue_declare(queue='my_queue')

            channel.basic_consume(
                queue='my_queue', on_message_callback=callback, auto_ack=True
            )

            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        start_consumer()
