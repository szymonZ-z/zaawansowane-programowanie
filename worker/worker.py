import pika
import json
import os
from worker.detector import detect_people
from shared.storage import update_task
import time


RABBIT_HOST = "rabbitmq"
QUEUE_NAME = "tasks"

for i in range(10):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')
        )
        break
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ nie jest jeszcze gotowy, retry za 2s...")
        time.sleep(2)
else:
    raise Exception("Nie udało się połączyć z RabbitMQ")

channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)

print("🟢 Worker uruchomiony, czekam na zadania...")


def callback(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["task_id"]
    image_path = task["image_path"]

    print(f"🔵 Przetwarzam task {task_id}")

    update_task(task_id, "processing")

    output_path = f"results/{task_id}.jpg"
    os.makedirs("results", exist_ok=True)

    try:
        count = detect_people(image_path, output_path)
        update_task(
            task_id,
            "done",
            count=count,
            image=output_path
        )
        print(f"✅ Task {task_id} zakończony: {count} osób")

    except Exception as e:
        update_task(task_id, "error")
        print(f"❌ Błąd w tasku {task_id}: {e}")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

channel.start_consuming()
