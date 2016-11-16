#!/usr/bin/env python
import threading, logging, time
from kafka import KafkaConsumer, KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        message = "Test message from python-kafka-plugin."

        while True:
            producer.send('test', message)
            print("Sent:" + message)
            time.sleep(5)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='latest')
        consumer.subscribe(['test'])

        for message in consumer:
            print ("Get:" + message)


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(10)


if __name__ == "__main__":
    main()
