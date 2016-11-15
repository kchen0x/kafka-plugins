echo "===Begin to set kafka test environment.==="

export $KAFKA_HOME=/home/cloudera/opt/kafka_2.10-0.9.0.1

alias kafka-start-server="$KAFKA_HOME/bin/kafka-server-start.sh ./config/server.properties"
alias kafka-topic-list="$KAFKA_HOME/bin/kafka-topics.sh --list --zookeeper localhost:2181"
alias kafka-topic-create="$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic"
alias kafka-topic-delete="$KAFKA_HOME/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic"
alias kafka-console-producer="$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic"
alias kafka-console-consumer="$KAFKA_HOME/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic"

echo "===Environment done.==="