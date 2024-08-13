import pika

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Process the message here

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue from which the consumer will receive messages
    channel.queue_declare(queue='my_queue')

    channel.basic_consume(
        queue='my_queue', on_message_callback=callback, auto_ack=True
    )

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()