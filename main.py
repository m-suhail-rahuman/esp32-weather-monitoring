import time
import json
import random
from umqtt.simple import MQTTClient

# AWS IoT Core Config
BROKER_ENDPOINT = "a2hahzzp49dpz0-ats.iot.us-east-1.amazonaws.com"  # Replace with your endpoint
CLIENT_ID = "esp8266_client"
TOPIC = "temp"  # Your AWS IoT topic

# Certificate paths (files stored on ESP8266 root)
CERT_FILE = "/devicecert.crt"
KEY_FILE = "/private.key"
ROOT_CA = "/AmazonRootCA1.pem"

# Function to publish temperature data
def publish_to_aws():
    # Setup MQTT Client
    client = MQTTClient(
        client_id=CLIENT_ID,
        server=BROKER_ENDPOINT,
        port=8883,
        ssl=True,
        ssl_params={"certfile": CERT_FILE, "keyfile": KEY_FILE, "ca_certs": ROOT_CA}
    )
    
    # Connect to AWS IoT
    print("Connecting to AWS IoT Core...")
    client.connect()
    print("Connected!")

    # Publish temperature data
    for i in range(10):  # Publish 10 messages
        temperature = 25 + random.randint(0, 5)
        timestamp = time.time()
        message = {"time": timestamp, "temp": temperature}
        payload = json.dumps(message)

        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(2)  # Wait 2 seconds between messages

    # Disconnect
    client.disconnect()
    print("Disconnected from AWS IoT Core.")

# Start the publish process
publish_to_aws()
