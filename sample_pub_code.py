import time
import json
import random
from datetime import datetime
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

# AWS IoT Core Configuration
ENDPOINT = "change this"
CLIENT_ID = "sample_client"
TOPIC = "temp"

ROOT_CA_PATH = "AmazonRootCA1.pem"    # Root CA certificate file
CERTIFICATE_PATH = "devicecert.crt"   # Device certificate file
PRIVATE_KEY_PATH = "private.key"      # Private key file

# Callback for messages (if needed)
def on_message_received(topic, payload, **kwargs):
    print(f"Received message on topic '{topic}': {payload.decode()}")

# Main function to publish messages
def main():
    # MQTT Connection setup
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=CERTIFICATE_PATH,
        pri_key_filepath=PRIVATE_KEY_PATH,
        ca_filepath=ROOT_CA_PATH,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30,
        bootstrap=client_bootstrap
    )

    print("Connecting to AWS IoT Core...")
    connect_future = mqtt_connection.connect()
    connect_future.result()
    print("Connected!")

    # Publish 10 sample messages
    for i in range(10):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = 25 + random.randint(0, 5)
        message = {"time": now, "temp": temperature}
        payload = json.dumps(message)

        mqtt_connection.publish(
            topic=TOPIC,
            payload=payload,
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print(f"Published: {payload}")
        time.sleep(2)

    # Disconnect
    print("Disconnecting...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected!")

if __name__ == "__main__":
    main()
