import pika
import json
def publish_message(message):
    credentials = pika.PlainCredentials('root', '123')
    parameters = pika.ConnectionParameters('86.48.7.247', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare the queue to ensure it exists
    channel.queue_declare(queue='user_registration',durable=True)

    # Publish the message to the queue
    channel.basic_publish(exchange='',
                          routing_key='user_registration',
                          body=message)
    print(f"Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    message = {'email':"bekzsfod@gmail.com",'uuid':"9cf8b01d-a273-45a5-aeaa-1ce88a198cc7"}
    publish_message(message)