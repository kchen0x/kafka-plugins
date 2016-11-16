#!/usr/bin/env python
# encoding: utf-8
from kafka import KafkaProducer
import json


def main():
    producer = KafkaProducer(
    	value_serializer=lambda v: json.dumps(v).encode('utf-8')
    	)
    producer.send('test', {'foo': 'bar'})


if __name__ == '__main__':
    main()
