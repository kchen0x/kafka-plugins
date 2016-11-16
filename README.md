This repo is for testing Kafka plugins.

## Preparation

`kafka 0.9.0 +` installed([Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/0.10.1.0/kafka_2.11-0.10.1.0.tgz) 0.10.0 here and un-tar it).

ZooKeeper is listenning on `2181` port.

## Get Test Environment

```bash
git clone https://github.com/quentin-chen/kafka-plugins.git $$ cd kafka-plugins
vim env.sh
```

change exact directory of `KAFKA_HOME` on you machine:

```bash
export KAFKA_HOME="<kafka_dir>"
```

add this at the end of your `~/.bashrc` file:

```bash
source <kafka-plugin-dir>/env.sh
```

## Start Kafka Server

```bash
kafka-start-server
```

in new terminal, let create new topic called `test` in Kafka:

```bash
kafka-topic-create test
```

to see this topic, use:

```bash
kafka-topic-list
```

to delete this topic, use:

```bash
kafka-topic-delete test
```

### Simple Console Prod-Cons

In new terminal, run this to create a new Console Consumer who subscribe topic `test`:

```bash
kafka-console-consumer test
```

and we can start a Console Producer in another new terminal to topic `test`:

```bash
kafka-console-producer test
```

then, you can send data from Console Producer by typing something and press `enter` as one message and see them in Console Consumer.

## Python Kafka Plugin

Python kafka plugin test samples are under `script` directory, make sure you have the python environment `2.7+` or `3.5+`:

```bash
python -V
```

then, use `pip` to install the dependencies:

```bash
pip install kafka-python

#python3 may use
pip3 install kafka-python
```

### Python Interpreter

```python
>>> from kafka import KafkaProducer
>>> producer = KafkaProducer(bootstrap_servers='localhost:1234')
>>> for _ in range(10):
...     producer.send('foobar', b'some_message_bytes')
>>> # Block until all pending messages are sent
>>> producer.flush()
>>> # Block until a single message is sent (or timeout)
>>> producer.send('foobar', b'another_message').get(timeout=60)
>>> # Use a key for hashed-partitioning
>>> producer.send('foobar', key=b'foo', value=b'bar')
>>> # Serialize json messages
>>> import json
>>> producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
>>> producer.send('fizzbuzz', {'foo': 'bar'})
>>> # Serialize string keys
>>> producer = KafkaProducer(key_serializer=str.encode)
>>> producer.send('flipflap', key='ping', value=b'1234')
>>> # Compress messages
>>> producer = KafkaProducer(compression_type='gzip')
>>> for i in range(1000):
...     producer.send('foobar', b'msg %d' % i)
```

### Producer

```bash
python script/producer.py
```

then, massage will be sent to Kafka bus on topic `test`.

### Prodocer and Consumer

```bash
python script/prod_cons_example.py
```

sample messages will be sent to Kafka bus on topic `test` continuously and the application will also subscribe this topic as a consumer.

## TODO

//TODO