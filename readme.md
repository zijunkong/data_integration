# Data Integration Project - Step 3

This project focuses on data integration and streaming, utilizing Kafka to transfer and manage data effectively. We have completed **Step 3**, where we implement data transfer from a CSV file into Kafka using Confluent Cloud and the `confluent_kafka` Python library.

## Step 3 Summary

### Tools and Technology Stack
- **Kafka**: We use Confluent Cloud for managed Kafka services, which simplifies setup and provides reliable data streaming capabilities.
- **Python**: We chose the `confluent_kafka` Python library to interact with Confluent Cloud, allowing us to produce data to Kafka from a local CSV file in real time.

### Implementation

1. **File Transfer**: The process reads data from a CSV file in batches of 100 records at a time.
2. **Streaming to Kafka**: Using Confluent Cloud, we create a topic (`dataintegration`) and stream the data, ensuring data integrity and reducing load by adding a delay after each batch.
3. **Configuration**: Authentication and connection details are securely managed through the `client.properties` file, which includes parameters like `bootstrap.servers`, `API key`, and `API secret`.

### Steps Taken

1. **Confluent Cloud Setup**: We created an account on Confluent Cloud, set up a Kafka cluster, and generated the necessary API credentials for secure access.
2. **Python Script**: We implemented a Python script to read CSV data and produce it to Kafka. Each record in the CSV file corresponds to one message in Kafka, where records are grouped and sent in batches of 100 messages to optimize performance.
3. **Testing**: The `confluent_kafka` consumer was used to verify that data is successfully received and processed in Kafka.
