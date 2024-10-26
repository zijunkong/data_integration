from confluent_kafka import Producer
import time
import csv
import json

# Confluent Cloud api
bootstrap_servers = "xxx"     
api_key = "xxx"
api_secret = "xxx"

# Producer
producer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': api_key,
    'sasl.password': api_secret
}

producer = Producer(producer_conf)

# File to be uploaded
file_path = '/Users/kong/Downloads/project/hospital-utilization-trends.csv'

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_data_to_kafka():
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        batch = []
        
        for row in reader:
            batch.append(row)
            
            if len(batch) == 100:
                producer.produce('dataintegration', value=json.dumps(batch), callback=delivery_report)
                producer.flush()
                print("Sent 100 records to Kafka")
                batch = []
                time.sleep(10)
                
        if batch:
            producer.produce('dataintegration', value=json.dumps(batch), callback=delivery_report)
            producer.flush()
            print(f"Sent {len(batch)} remaining records to Kafka")

# Run producer
if __name__ == "__main__":
    send_data_to_kafka()
    producer.flush()
