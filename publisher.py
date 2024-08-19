import pika

def publish_message(message):
    # Establish a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue to ensure it exists
    channel.queue_declare(queue='my_queue')

    # Publish the message to the queue
    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=message)
    print(f"Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    message = "GOOD BOY"
    publish_message(message)