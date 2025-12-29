import pika
import json
import time

def publish_task(task: dict):
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host="rabbitmq")
            )
            channel = connection.channel()
            channel.queue_declare(queue="tasks", durable=True)

            channel.basic_publish(
                exchange='',
                routing_key='tasks',
                body=json.dumps(task),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # persistent
                )
            )
            connection.close()
            break
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ nie gotowy, retry za 2s...")
            time.sleep(2)