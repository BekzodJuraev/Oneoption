import pika
import json
def publish_message(message):
    credentials = pika.PlainCredentials('root', '123')
    parameters = pika.ConnectionParameters('86.48.7.247', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare the queue to ensure it exists
    channel.queue_declare(queue='transactions',durable=True)

    # Publish the message to the queue
    channel.basic_publish(exchange='',
                          routing_key='transactions',
                          body=json.dumps(message))
    print(f"Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    message = {'email':"bekzsfod@gmail.com",'uuid':"83fecee4-1d2b-476f-bf8d-f616e521b8de"}
    publish_message(message)